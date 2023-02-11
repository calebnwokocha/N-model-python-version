from model.src.Node import Node

class Layer:
    """
    The Layer class represents a collection of Node objects and provides methods for manipulating
    and interacting with those nodes. It contains an ArrayList of Node objects, as well as methods
    to add, remove, and get the Nodes in the list. It also has methods to set and get the
    cFunction, cFunctionName, and degree variables of all the nodes in the layer, as well as
    the power variable. It also has methods to get the width of the layer and an array of
    cFunctionName of all the nodes in the layer. Additionally, it has a method to train and
    test all the nodes in the layer and a method to check if the layer is null.
    """
    def __init__(self, width: int):
        """
        Constructor for the Layer class.
        :param width: The number of nodes to be created in the layer.
        """
        self.nodes = []
        for i in range(width):
            self.nodes.append(Node())

    def get_nodes(self):
        """
        Getter method for the nodes variable.
        :return: The value of the nodes variable.
        """
        return self.nodes

    def set_nodes(self, nodes):
        """
        Setter method for the nodes variable.
        :param nodes: The new value of the nodes variable.
        """
        self.nodes = nodes

    def add_node(self, node):
        """
        This method adds a node to the nodes variable.
        :param node: The node to be added to the nodes variable.
        """
        self.nodes.append(node)

    def remove_node(self, index: int):
        """
        This method removes a node from the nodes variable.
        :param index: The index of the node to be removed.
        """
        self.nodes.pop(index)

    def get_width(self):
        """
        Getter method for the width of the layer.
        :return: The width of the layer.
        """
        return len(self.nodes)

    def set_c_function(self, c_function_name: str, degree: float, c_function):
        """
        This method sets the cFunction, cFunctionName and degree variables of all the nodes in the layer.
        :param c_function_name: The new value of the cFunctionName variable.
        :param degree: The new value of the degree variable.
        :param c_function: The new value of the cFunction variable.
        """
        for node in self.nodes:
            node.set_c_function(c_function_name, degree, c_function)

    def set_power(self, power: float):
        """
        This method sets the power variable of all the nodes in the layer.
        :param power: The new value of the power variable.
        """
        for node in self.nodes:
            node.set_power(power)

    def get_c_function_name(self):
        """
        This method returns a list of cFunctionName of all the nodes in the layer.

        Returns:
        -------
        list: A list of cFunctionName of all the nodes in the layer.
        """
        c_function_name = [node.get_c_function_name() for node in self.nodes]
        return c_function_name

    def set_c_function(self, c_function_name, degree, c_function):
        """
        This method sets the comprehensive function for each node in the layer.

        Parameters:
        ----------
        c_function_name: list
            A list of strings representing the names of the comprehensive functions.
        degree: list
            A list of floats representing the degrees of the comprehensive functions.
        c_function: list
            A list of functions representing the comprehensive functions.
        """
        for i, node in enumerate(self.nodes):
            node.set_c_function(c_function_name[i], degree[i], c_function[i])

    def get_degree(self):
        """
        This method returns a list of the degree of each node in the layer.

        Returns:
        -------
        list: A list of floats representing the degrees of the nodes.
        """
        degree = [node.get_degree() for node in self.nodes]
        return degree

    def get_weight(self):
        """
        This method returns a list of the weight of each node in the layer.

        Returns:
        -------
        list: A list of floats representing the weight of the nodes.
        """
        weight = [node.get_weight() for node in self.nodes]
        return weight

    def get_power(self):
        """
        This method returns a list of the power of each node in the layer.

        Returns:
        -------
        list: A list of floats representing the power of the nodes.
        """
        power = [node.get_power() for node in self.nodes]
        return power

    def set_power(self, power):
        """
        This method sets the power of each node in the layer.

        Parameters:
        ----------
        power: list
            A list of floats representing the desired power of the nodes.
        """
        for i, node in enumerate(self.nodes):
            node.set_power(power[i])

    def set_coverage(self, coverage):
        """
        Set the coverage of each node in the layer.
        :param coverage: float - the coverage to be set for each node.
        """
        for node in self.nodes:
            node.set_coverage(coverage)

    def set_coverage(self, coverage_array):
        """
        Set the coverage of each node in the layer.
        :param coverage_array: list of floats - an array of doubles representing the desired coverage of the nodes.
        """
        for i in range(len(self.nodes)):
            self.nodes[i].set_coverage(coverage_array[i])

    def get_coverage(self):
        """
        Return an array of the coverage of each node in the layer.
        :return: list of floats - an array of doubles representing the coverage of the nodes.
        """
        coverage = [0.0 for i in range(len(self.nodes))]
        for i in range(len(coverage)):
            coverage[i] = self.nodes[i].get_coverage()
        return coverage

    def get_error_mean(self):
        """
        Return an array of the error mean of each node in the list of nodes.
        :return: list of floats - an array of the error mean of each node in the list of nodes.
        """
        error_mean = [0.0 for i in range(len(self.nodes))]
        for i in range(len(error_mean)):
            error_mean[i] = self.nodes[i].get_current_error_mean()
        return error_mean

    def set_error_mean(self, error_mean):
        """
        Set the error mean of each node in the list of nodes.
        :param error_mean: list of floats - an array of error means that will be set to each node in the list of nodes.
        """
        for i in range(len(self.nodes)):
            self.nodes[i].set_current_error_mean(error_mean[i])

    def get_hypothesis(self):
        """
        Returns an array of the hypothesis of each node in the list of nodes.
        :return: list of hypothesis of each node in the list of nodes.
        """
        hypothesis = [node.get_hypothesis() for node in self.nodes]
        return hypothesis

    def get_thesis(self):
        """
        Returns an array of the thesis of each node in the list of nodes.
        :return: list of thesis of each node in the list of nodes.
        """
        thesis = [node.get_thesis() for node in self.nodes]
        return thesis

    def train(self, iteration, objectives, input):
        """
        Method to train the nodes in the layer.

        :param iteration: Number of iterations to train the layer.
        :param objectives: list of objectives for each node.
        :param input: list of input data for each node.
        """
        for i, node in enumerate(self.nodes):
            try:
                node.train(objectives[i], iteration, input[i])
            except IndexError:
                # if there are more nodes than objectives or input data, break the loop.
                break

    def test(self, input):
        """
        Method to test the nodes in the layer.

        :param input: list of input data for each node.
        """
        null_count = 0
        for i, node in enumerate(self.nodes):
            try:
                node.test(input[i])
            except IndexError:
                # if there are more nodes than input data, break the loop.
                break
            except TypeError:
                # if the input data is null, pass None to the node.
                node.test(None)
            if node.get_thesis() is None and node.get_coverage() is not None:
                # counts the number of nodes with null thesis and non-null coverage
                null_count += 1
        self.isNull = null_count > len(self.nodes) / 3

    def get_gradient(self, iteration):
        """
        Returns an array of the gradient of each node in the list of nodes.

        :param iteration: iteration number for computing the gradient
        :return: list of gradient of each node in the list of nodes.
        """
        gradient = [node.get_gradient(iteration) for node in self.nodes]
        return gradient

    def is_null(self):
        """
        Method to check if the layer is null.

        :return: boolean value indicating if the layer is null.
        """
        return self.isNull


