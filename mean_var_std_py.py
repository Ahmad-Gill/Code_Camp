# -*- coding: utf-8 -*-
"""mean_var_std.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16ZOVTzxr3U_tIU3FR5-FhCJ3p1amhp5d
"""

import numpy as np

def calculate(numbers):
    # Verify that the input list contains exactly 9 elements
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the input list into a 3x3 NumPy array
    matrix = np.array(numbers).reshape(3, 3)

    # Calculate statistics
    mean = [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)]
    variance = [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)]
    std_deviation = [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)]
    max_value = [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)]
    min_value = [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)]
    sum_value = [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]

    # Return the statistics in the specified format
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }