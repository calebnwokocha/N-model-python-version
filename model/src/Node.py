import math
import StatUtil as stat
import numpy as np
from typing import Callable, Tuple

class Node:
    """
    The Node class is a representation of a node in a comprehensive layer model.
    It has several fields such as cFunctionName, hypothesis, thesis, errorMean,
    coverage, power, degree, inputMean, inputUpperBound, inputLowerBound, and an
    instance of the StatUtil class. The class contains several getter and
    setter methods for the fields, a method to set the comprehensive function,
    a method to train the node, a method to test the node, a method to get the rule of the
    node and a method to get the coverage of the node. The train method sets the
    value of the objective, inputMean and errorMean variable, while the test
    method sets the value of the thesis variable. The class also contains a
    method to check if the node is null.
    """

    def __init__(self):
        self.cFunctionName = None
        self.cFunction = None
        self.hypothesis = None
        self.thesis = None
        self.currentErrorMean = 0.0
        self.previousErrorMean = 0.0
        self.coverage = None
        self.power = None
        self.objective = 0.0
        self.degree = None
        self.inputMean = None
        self.inputUpperBound = None
        self.inputLowerBound = None

    def get_hypothesis(self):
        """
        Getter method for the hypothesis variable.
        :return: The value of the hypothesis variable.
        """
        return self.hypothesis

    def get_thesis(self):
        """
        Getter method for the thesis variable.
        :return: The value of the thesis variable.
        """
        return self.thesis

    def get_current_error_mean(self):
        """
        Getter method for the errorMean variable.
        :return: The value of the errorMean variable.
        """
        return math.sqrt(self.currentErrorMean)

    def get_degree(self):
        """
        Getter method for the degree variable.
        :return: The value of the degree variable.
        """
        return self.degree

    def get_power(self):
        """
        Getter method for the power variable.
        :return: The value of the power variable.
        """
        return self.power

    def set_power(self, power):
        """
        Setter method for the power variable.
        :param power: The new value of the power variable.
        """
        self.power = power

    def set_coverage(self, coverage: float):
        """
        Setter method for the coverage variable.
        :param coverage: The new value of the coverage variable.
        """
        self.coverage = coverage
    
    def get_coverage(self) -> float:
        """
        Getter method for the coverage variable.
        :return: The value of the coverage variable.
        """
        return self.coverage
    
    def get_c_function_name(self) -> str:
        """
        Getter method for the c_function_name variable.
        :return: The value of the c_function_name variable.
        """
        return self.c_function_name
    
    def set_c_function(self, c_function_name: str, degree: float, c_function: Callable[[np.ndarray], float]):
        """
        This method sets the value of the c_function_name, degree, and c_function variables.
        :param c_function_name: The new value of the c_function_name variable.
        :param degree: The new value of the degree variable.
        :param c_function: The new value of the c_function variable.
        """
        self.c_function_name = c_function_name
        self.degree = degree
        self.c_function = c_function

    def train(self, objective, iteration, *input):
        """
        This method trains the node with a given objective, iteration and input data.
        It sets the values of the objective, inputMean and errorMean variables.
        :param objective: The objective value for the training.
        :param iteration: The iteration number for the training.
        :param input: The input data for the training.
        """
        self.objective = objective
        self.activate(*input)
        try:
            error = (self.hypothesis - self.objective)**2
            if iteration == 1:
                self.inputMean = [0.0] * len(input)
                self.currentErrorMean = error
            if iteration > 1:
                self.previousErrorMean = self.currentErrorMean
                self.currentErrorMean = self.stat.dynamic_power_mean(self.currentErrorMean, error, self.power, iteration)
        except Exception:
            pass
        if self.coverage is not None:
            self.set_input_bounds(input, iteration)

    def test(self, *input):
        """
        This method tests the input by activating the function
        and determining if it is an outlier.
        :param input: The input to be tested.
        """
        if self.coverage is None:
            self.activate(*input)
        else:
            if self.stat.isOutlier(input, self.inputLowerBound, self.inputUpperBound):
                self.thesis = None
            else:
                self.activate(*input)

    def get_gradient(self, iteration):
        """
        This method returns the gradient of the node.
        :param iteration: The iteration number for which the gradient is to be calculated.
        :return: The gradient of the node.
        """
        return (self.currentErrorMean**self.power) - (self.previousErrorMean**self.power)

    def activate(self, *input):
        """
        This method activates the cFunction with the input,
        sets the hypothesis and thesis variables.
        
        Args:
        - input (Tuple[float]): The input to be used in activating the function.
        """
        try:
            self.hypothesis = self.degree_root(abs(self.cFunction(*input)), self.degree)
            self.thesis = self.hypothesis + (self.currentErrorMean / (math.pow(self.currentErrorMean, 0.5) + 1))
        except TypeError:
            pass

    def set_input_bounds(self, input, iteration):
        """
        This method sets the input bounds based on the input and iteration number.
        It sets the inputMean, inputUpperBound and inputLowerBound variables.
        
        Args:
        - input (List[float]): The input data to be used in setting the bounds.
        - iteration (int): The iteration number for the input data.
        """
        if iteration == 1:
            self.inputMean = input
        else:
            self.inputMean = self.stat.dynamic_power_mean(self.inputMean, input, self.power, iteration + 1)
        self.inputUpperBound = [None] * len(input)
        self.inputLowerBound = [None] * len(input)
        for i in range(len(input)):
            try:
                input_deviation = self.stat.standard_deviation(input, self.inputMean[i])
                self.inputUpperBound[i] = self.inputMean[i] + (self.coverage * input_deviation)
                self.inputLowerBound[i] = self.inputMean[i] - (self.coverage * input_deviation)
            except TypeError:
                break

    def degree_root(self, c_value, degree):
        """
        This method calculates the degree root of a given value.
        
        Args:
        - c_value (float): The value for which the degree root is to be calculated.
        - degree (float): The degree of the root to be calculated.
        
        Returns:
        - float: The degree root of the given value.
        """
        return math.pow(c_value, 1 / degree)


