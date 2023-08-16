import numpy as np

def Calculate_standard_deviation(prices):
    mean = np.mean(prices)
    standard_deviation = np.std(prices)
    
    return mean, standard_deviation
