import Layer as layer

class Network:
    """
    The Network class represents a comprehensive network and provides methods for creating and
    manipulating the network. The class has a private field called 'layers' which is a
    list of Layer objects. Users can create a new network by specifying the number
    of layers and the width of each layer. The class also provides methods for getting
    and setting the layers in the network, adding and removing layers, getting the number
    of layers, getting the width of each layer, and setting the comprehensive function for all
    layers in the network. The class also provides methods for setting the
    degree for each layer in the layers list.
    """

    def __init__(self, length, width):
        """
        Creates a new network with the specified number of layers and a width of each layer.
        :param length: The number of layers in the network
        :param width: The width of each layer in the network
        """
        self.layers = [layer.Layer(width) for i in range(length)]

    def __init__(self, length, widths):
        """
        Creates a new network with the specified number of layers and a width of each layer.
        :param length: The number of layers in the network
        :param widths: The width of each layer in the network as a list
        """
        self.layers = [layer.Layer(widths[i]) for i in range(length)]

    def get_layers(self):
        """
        Returns the layers in the network.
        :return: A list of the layers in the network
        """
        return self.layers

    def set_layers(self, layers):
        """
        Sets the layers in the network.
        :param layers: A list of layers to be set in the network
        """
        self.layers = layers

    def add_layer(self, layer):
        """
        Adds a new layer to the network.
        :param layer: The new layer to be added to the network
        """
        self.layers.append(layer)

    def remove_layer(self, index):
        """
        Removes a layer at the specified index from the network.
        :param index: The index of the layer to be removed
        """
        self.layers.pop(index)

    def get_length(self):
        """
        Returns the number of layers in the network.
        :return: The number of layers in the network
        """
        return len(self.layers)

    def get_widths(self):
        """
        Returns the width of each layer in the network as a list.
        :return: A list of the width of each layer in the network
        """
        return [layer.get_width() for layer in self.layers]

    def set_c_function(self, c_function_name, degree, c_function):
        """
        Sets the comprehensive function for all layers in the network.
        :param c_function_name: The name of the comprehensive function
        :param degree: The degree of the comprehensive function
        :param c_function: The comprehensive function to be set
        """
        for layer in self.layers:
            layer.set_c_function(c_function_name, degree, c_function)

    def set_c_function(self, c_function_name, degree, c_function):
        """
        This method sets the cFunction, degree, and cFunctionName for each layer in the layers list.
        :param c_function_name: a list of strings representing the names of the cFunctions for each layer
        :param degree: a list of floats representing the degrees of the cFunctions for each layer
        :param c_function: a list of functions that take in an array of floats and return a float
        :return: None
        """
        for i in range(len(self.layers)):
            self.layers[i].set_c_function(c_function_name[i], degree[i], c_function[i])

    def set_c_function(self, c_function_name, degree, c_function):
        """
        This method sets the cFunction, degree, and cFunctionName for each layer in the layers list.
        :param c_function_name: a 2D list of strings representing the names of the cFunctions for each layer
        :param degree: a 2D list of floats representing the degrees of the cFunctions for each layer
        :param c_function: a 2D list of functions that take in an array of floats and return a float
        :return: None
        """
        for i in range(len(self.layers)):
            self.layers[i].set_c_function(c_function_name[i], degree[i], c_function[i])

    def get_c_function_name(self):
        """
        This method returns a 2D list of strings representing the names of the cFunctions for each layer
        :return: a 2D list of strings representing the names of the cFunctions for each layer
        """
        c_function = [None] * len(self.layers)
        for i in range(len(c_function)):
            c_function[i] = self.layers[i].get_c_function_name()
        return c_function

    def get_degree(self):
        """
        This method returns a 2D list of floats representing the degrees of the cFunctions for each layer
        :return: a 2D list of floats representing the degrees of the cFunctions for each layer
        """
        degree = [None] * len(self.layers)
        for i in range(len(degree)):
            degree[i] = self.layers[i].get_degree()
        return degree

    def set_power(self, power):
        """
        This method sets the power for each layer in the layers list.

        Parameters:
        - power (Union[float, List[float]]): a float representing the power for each layer,
            or an array of floats representing the power for each layer

        Returns:
        None
        """
        if isinstance(power, float):
            for layer in self.layers:
                layer.set_power(power)
        elif isinstance(power, list):
            for layer in self.layers:
                layer.set_power(power)

    def set_power(self, power):
        """
        This method sets the power for each layer in the layers list.

        Parameters:
        - power (List[List[float]]): a 2D array of floats representing the power for each layer and each node

        Returns:
        None
        """
        for i in range(len(self.layers)):
            self.layers[i].set_power(power[i])

    def get_power(self):
        """
        Get the power of each layer.

        Returns:
        - power (List[List[float]]): a 2D array of floats representing the power for each layer and each node
        """
        power = [[] for i in range(len(self.layers))]
        for i in range(len(power)):
            power[i] = self.layers[i].get_power()
        return power

    def set_coverage(self, coverage):
        """
        Set the coverage of each layer.

        Parameters:
        - coverage (Union[float, List[float]]): a float value representing the coverage for all layers,
            or an array of float values representing the coverage for each layer

        Returns:
        None
        """
        if isinstance(coverage, float):
            for layer in self.layers:
                layer.set_coverage(coverage)
        elif isinstance(coverage, list):
            for layer in self.layers:
                layer.set_coverage(coverage)

    def set_coverage(self, coverage):
        """
        Set the coverage of each layer.

        Parameters:
        - coverage (List[List[float]]): a 2D array of float values representing the coverage for each layer and each node

        Returns:
        None
        """
        for i in range(len(self.layers)):
            self.layers[i].set_coverage(coverage[i])

    def get_coverage(self):
        """
        Get the coverage of each layer.
        :return: a 2D array of floats representing the coverage for each layer and each node.
        """
        coverage = [[] for _ in range(len(self.layers))]
        for i, layer in enumerate(self.layers):
            coverage[i] = layer.get_coverage()
        return coverage

    def get_error_mean(self):
        """
        Get the mean error of each layer.
        :return: a 2D array of floats representing the error mean for each layer and each node.
        """
        error_mean = [[] for _ in range(len(self.layers))]
        for i, layer in enumerate(self.layers):
            error_mean[i] = layer.get_error_mean()
        return error_mean

    def set_error_mean(self, error_mean):
        """
        Set the mean error of each layer.
        :param error_mean: a 2D array of floats representing the error mean for each layer and each node.
        """
        for i, layer in enumerate(self.layers):
            layer.set_error_mean(error_mean[i])

    def get_hypothesis(self):
        """
        Get the hypothesis of all the layers in the network.
        :return: a 2D array of floats representing the hypothesis of each layer and each node.
        """
        hypothesis = [[] for _ in range(len(self.layers))]
        for i, layer in enumerate(self.layers):
            hypothesis[i] = layer.get_hypothesis()
        return hypothesis

    def get_thesis(self):
        """
        Get the thesis of all the layers in the network.
        :return: a 2D array of floats representing the thesis of each layer and each node.
        """
        thesis = [[] for _ in range(len(self.layers))]
        for i, layer in enumerate(self.layers):
            thesis[i] = layer.get_thesis()
        return thesis

def train(self, iteration, objective, input):
    """
    Trains the network using the input and objective provided.
    Args:
        iteration (int): the number of iterations to train the network.
        objective (List[float]): the objective/expected output of the network.
        input (List[List[float]]): the input to the network.
    """
    for i in range(len(self.layers)):
        if i == 0:
            self.layers[i].train(iteration, objective, input)
        else:
            previous_layer_thesis = self.layers[i - 1].getThesis()
            self.layers[i].train(iteration, objective, self.vector_to_matrix(previous_layer_thesis))

def test(self, input):
    """
    Test the network using the given input.
    Args:
        input (List[List[float]]): The input values to test the network with.
    """
    for i in range(len(self.layers)):
        if i == 0:
            self.layers[i].test(input)
            if self.layers[i].is_null():
                self.nullify_net_output()
        else:
            previous_layer_thesis = self.layers[i - 1].getThesis()
            self.layers[i].test(self.vector_to_matrix(previous_layer_thesis))
            if self.layers[i].is_null():
                self.nullify_net_output()

def get_gradient(self, iteration):
    """
    Gets the gradient for the network.
    Args:
        iteration (int): The iteration number to get the gradient for.
    Returns:
        List[List[float]]: The gradient for the network.
    """
    gradient = [[None] * self.get_length() for _ in range(self.get_length())]
    for i in range(len(gradient)):
        gradient[i] = self.layers[i].getGradient(iteration)
    return gradient

def vector_to_matrix(self, vector):
    """
    Utility function to convert a vector to a matrix.
    Args:
        vector (List[float]): The vector to convert.
    Returns:
        List[List[float]]: The converted matrix.
    """
    matrix = [[None] * 1 for _ in range(len(vector))]
    for i in range(len(matrix)):
        matrix[i][0] = vector[i]
    return matrix

def nullify_net_output(self):
    """
    Set the output of the last layer to None.
    """
    self.layers[self.get_length() - 1].test(None)

               



