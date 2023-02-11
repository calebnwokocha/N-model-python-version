import math

class StatUtil:
    """
    The StatUtil class is a collection of methods for manipulating and interacting with data.
    It includes methods for calculating the dynamic power mean, variance, and standard deviation
    of a given array of data. It also includes methods for calculating the dynamic power mean of
    a given mean and datum, and a given array of means and data, and a given 2D array of means
    and data, all using the specified power and iteration. Additionally, it includes a constructor
    for the StatUtil class.
    """

    def __init__(self):
        """
        Constructor for the StatUtil class.
        """
        pass

    def dynamic_power_mean(self, mean, datum, power, iteration):
        """
        This method calculates the dynamic power mean of a given mean and datum using the specified power and iteration.

        Parameters:
        mean (float): The current mean of the data.
        datum (float): The new data point to be added to the mean.
        power (float): The power to be used in the calculation of the dynamic power mean.
        iteration (int): The number of iterations for which the mean has been calculated.

        Returns:
        float: The dynamic power mean of the data.
        """
        mean = (1.0 / iteration) * (math.pow(datum, power) + (math.pow(mean, power) * (iteration - 1)))**(1.0 / power)
        return mean

    def dynamic_power_mean(self, mean, data, power, iteration):
        """
        This method calculates the dynamic power mean of a given array of means and data using the specified power and iteration.

        Parameters:
        mean (List[float]): The current mean of the data in the form of an array.
        data (List[float]): The new data points to be added to the mean in the form of an array.
        power (float): The power to be used in the calculation of the dynamic power mean.
        iteration (int): The number of iterations for which the mean has been calculated.

        Returns:
        List[float]: The dynamic power mean of the data in the form of an array.
        """
        for i in range(len(data)):
            try:
                mean[i] = self.dynamic_power_mean(mean[i], data[i], power, iteration)
            except TypeError:
                pass
        return mean

def dynamic_power_mean(mean, data, power, iteration):
    """
    This function calculates the dynamic power mean of a given 2D array of means and data using the specified power and iteration.

    Parameters:
    mean (List[List[float]]): The current mean of the data in the form of a 2D array.
    data (List[List[float]]): The new data points to be added to the mean in the form of a 2D array.
    power (float): The power to be used in the calculation of the dynamic power mean.
    iteration (int): The number of iterations for which the mean has been calculated.

    Returns:
    List[List[float]]: The dynamic power mean of the data in the form of a 2D array.
    """
    for i in range(len(data)):
        try:
            mean[i] = dynamic_power_mean(mean[i], data[i], power, iteration)
        except IndexError:
            break
    return mean

def variance(data, expected_value):
    """
    This function calculates the variance of a given array of data using the specified expected value.

    Parameters:
    data (List[float]): The array of data for which the variance is to be calculated.
    expected_value (float): The expected value of the data.

    Returns:
    float: The variance of the data.
    """
    squared_sum = 0.0
    variance = None
    try:
        for datum in data:
            squared_sum += (datum - expected_value)**2
    except TypeError:
        pass
    if squared_sum == 0 or (len(data) - 1) == 0:
        variance = squared_sum
    else:
        variance = squared_sum / (len(data) - 1)
    return variance

def standard_deviation(data, expected_value):
    """
    This function calculates the standard deviation of a given array of data using the specified expected value.

    Parameters:
    data (List[float]): The array of data for which the standard deviation is to be calculated.
    expected_value (float): The expected value of the data.

    Returns:
    float: The standard deviation of the data.
    """
    return math.sqrt(variance(data, expected_value))

def is_between(data, minimum, maximum):
    """
    This function checks if a given data point is between a specified minimum and maximum value.

    Parameters:
    data (float): The data point to be checked.
    minimum (float): The lower bound of the range.
    maximum (float): The upper bound of the range.

    Returns:
    bool: True if data is between minimum and maximum, false otherwise.
    """
    return minimum <= data <= maximum

def is_outlier(data, data_lower_bound, data_upper_bound):
    """
    This method checks if a given array of data points is an outlier based on the specified lower and upper bounds of the data.
    
    Args:
    data (list[float]): The array of data points to be checked for outliers.
    dataLowerBound (list[float]): The lower bounds of the data.
    dataUpperBound (list[float]): The upper bounds of the data.

    Returns:
    bool: True if data is an outlier, False otherwise.
    """
    try:
        for i in range(len(data)):
            if data[i] >= data_lower_bound[i] and data[i] <= data_upper_bound[i]:
                return False
    except TypeError:
        return True

    return True

