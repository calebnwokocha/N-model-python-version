import StatUtil

class Multitask:
    """
    The Multitask class is used to hold multiple instances of the Network class,
    allowing for training and testing of multiple networks at once. It also allows
    for knowledge transfer between networks and keeps track of the non-null thesis frequency
    of each network. The class has various methods such as adding and removing networks,
    getting the coverage and thesis of all networks, and training and testing all the
    networks in the multitask network. It also has a variable to keep track of the index
    of the last network added to the multitask network.
    """
    def __init__(self):
        """
        Creates an empty instance of the multitask class
        """
        self.networks = []
        self.error_mean_mean = []
        self.last_network_index = None
        self.null_frequency_per_network = []
    
    def __init__(self, networks):
        """
        Creates an instance of the multitask class with the specified networks
        @param networks: the networks to be included in the multitask object
        """
        self.networks = networks
        
    def get_task_count(self):
        """
        Returns the number of networks in the multitask object
        @return: the number of networks
        """
        return len(self.networks)
        
    def set_networks(self, networks):
        """
        Sets the networks in the multitask object
        @param networks: the networks to be set in the multitask object
        """
        self.networks = networks
        
    def get_networks(self):
        """
        Returns the networks in the multitask object
        @return: the networks in the multitask object
        """
        return self.networks
        
    def add_network(self, network):
        """
        Adds a new network to the multitask object and transfers knowledge from the previous network
        @param network: the new network to be added
        """
        if len(self.networks) >= 1:
            self.transfer_knowledge_to(network)
        self.networks.append(network)
        
    def remove_network(self, index):
        """
        Removes a network at the specified index from the multitask object
        @param index: the index of the network to be removed
        """
        self.networks.pop(index)
        
    def get_coverage(self):
        """
        Returns the coverage of all networks in the multitask object as a 3D array
        @return: the coverage of all networks
        """
        coverage = []
        for i in range(len(self.networks)):
            coverage.append(self.networks[i].get_coverage())
        return coverage
    
    def get_thesis(self):
        """
        Returns the thesis of all networks in the multitask object as a 2D array
        @return: the thesis of all networks
        """
        thesis = []
        for i in range(len(self.networks)):
            current_network = self.networks[i]
            output_layer_index = current_network.get_length() - 1
            thesis.append(current_network.get_thesis()[output_layer_index])
        return thesis
        
    def train(self, iteration, objective, input):
        """
        Train the last network added to the multitask network.
        
        Parameters:
        iteration (int): The number of iterations the network should be trained for.
        objective (list): The expected output for the given input.
        input (list): The input to be trained on.
        """
        self.lastNetworkIndex = len(self.networks) - 1
        self.networks[self.lastNetworkIndex].train(iteration, objective, input)
        
    def test(self, iteration, input):
        """
        Test all the networks in the multitask network and print the null frequency per network of the multitask network.
        
        Parameters:
        iteration (int): The number of iterations the network should be tested for.
        input (list): The input to be tested on.
        """
        for network in self.networks:
            network.test(input)
            
        thesis = self.getThesis()
        null_non_null_as_10 = self.convert_null_to_1_and_non_null_to_0(thesis)
        null_count_per_network = self.count_nulls_per_network(null_non_null_as_10)
        
        if iteration == 0:
            for count in null_count_per_network:
                self.nullFrequencyPerNetwork.append(count)
        else:
            for i in range(len(null_count_per_network)):
                self.nullFrequencyPerNetwork[i] += null_count_per_network[i]
        
    def transfer_knowledge_to(self, network):
        """
        Transfer knowledge from the last network to the current network.
        
        Parameters:
        network (Network): The current network that knowledge is being transferred to.
        """
        if len(self.networks) > 0:
            self.lastNetworkIndex = len(self.networks) - 1
            last_network_error_mean = self.networks[self.lastNetworkIndex].get_error_mean()
            stat = StatUtil()
            
            if self.has_only_one_network():
                self.errorMeanMean = self.networks[self.lastNetworkIndex].get_error_mean()
            else:
                self.errorMeanMean = stat.dynamic_power_mean(self.errorMeanMean, last_network_error_mean, 1.0, len(self.networks))
                
            network.set_error_mean(self.errorMeanMean)
            
    def has_only_one_network(self):
        """
        The has_only_one_network method checks if the multitask network has only one network.

        Returns:
            A boolean indicating if the multitask network has only one network.
        """
        return len(self.networks) == 1

    def convert_null_to_1_and_non_null_to_0(self, thesis):
        """
        convert_null_to_1_and_non_null_to_0 is a helper function that converts all the null values in a 2D Double array to 0
        and all non-null values to 1.

        Args:
            thesis (List[List[float]]): a 2D Double array containing the thesis of the network

        Returns:
            List[List[int]]: an int[][] where all the null values in the input thesis are converted to 0 and all non-null values to 1.
        """
        null_non_null_as_01 = [[0 if item is None else 1 for item in row] for row in thesis]
        return null_non_null_as_01

    def count_nulls_per_network(self, null_non_null_as_01):
        """
        count_nulls_per_network is a helper function that counts the number of non-null values in each network

        Args:
            null_non_null_as_01 (List[List[int]]): a 2D int array where all the null values are converted to 0 and all non-null values to 1

        Returns:
            List[int]: an int[] where the i-th element represents the number of non-null values in the i-th network
        """
        non_null_count_per_network = [sum(row) for row in null_non_null_as_01]
        return non_null_count_per_network

    def forget_network(self):
        """
        This function forgets a network.
        """
        pass
