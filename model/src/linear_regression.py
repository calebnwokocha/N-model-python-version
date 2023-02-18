import math
import random
import Multitask
import Network

def main(args):

    # Create an instance of Multitask
    multitask = Multitask()

    # Create an array of 10 networks
    networks = [None] * 10

    # Create an array of network objectives
    network_objectives = [[None] * 10 for i in range(10)]

    # Create an array of training sets
    train_sets = [[[None] * 1 for j in range(8)] for i in range(10)]

    # Create an array of test sets
    test_sets = [[[None] * 1 for j in range(20)] for i in range(10)]

    # Set network objectives
    for i in range(1, len(network_objectives)):
        network_objectives[i] = [i * 10.0]

    # Set training sets
    for i in range(1, len(train_sets)):
        for j in range(len(train_sets[i])):
            train_sets[i][j][0] = random.random() + i

    # Set test sets
    for i in range(1, len(test_sets)):
        for j in range(len(test_sets[i])):
            test_sets[i][j][0] = random.random() + i

    def square(x):
        return math.power(x[0], 2.0)

    # Initialize the networks
    for i in range(1, len(networks)):
        networks[i] = Network(2, 1)
        networks[i].set_c_function("square", 2.0, square)
        networks[i].set_power(-6.0)
        networks[i].set_coverage(4.0)

    print("\nNETWORK TRAINING....................................................................")
    print()
    print()
    k = 0
    for i in range(1, len(networks)):
        # add the current network to the multitask
        multitask.add_network(networks[i])
        for j in range(train_sets[i].shape[0]):
            k += 1
            # train the current network with the current train set
            multitask.train(j + 1, network_objectives[i], train_sets[i][j])
            print("Example {}:".format(k))
            print()
            # print the network objective
            print("Network objective is {}".format(network_objectives[i]))
            print()
            # print the network input
            print("Network input is {}".format(train_sets[i][j]))
            print()
            # print the network hypothesis
            print("Network hypothesis is {}".format(multitask.get_networks()[i-1].get_hypothesis()[networks[i].get_length() - 1]))
            print()
            # print the network thesis
            print("Network thesis is {}".format(multitask.get_networks()[i-1].get_thesis()[networks[i].get_length() - 1]))
            print()


if __name__ == "__main__":
    import sys
   
