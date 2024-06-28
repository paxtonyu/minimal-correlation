import pandas as pd
import numpy as np
from scipy.io import loadmat
import os
from itertools import combinations  # C(n,m)


# Get the first ten original data
def load_data(file_path):
    file_extension = os.path.splitext(file_path)[1]

    if file_extension == ".xlsx":
        data = pd.read_excel(file_path)
    elif file_extension == ".mat":
        mat = loadmat(file_path)
        # Assuming the original data is stored in a variable named 'original_data' in the MATLAB file
        data = pd.DataFrame(mat["original_data"])
    else:
        raise ValueError(
            "Unsupported file format. Please provide a .xlsx or .mat file."
        )

    original_data = data.iloc[:10, :]
    return original_data


# Compute the average correlation for a given set of rows
def compute_average_correlation(data, comb):
    correlations = []
    for i, j in combinations(comb, 2):
        row_i = data.iloc[i, 1:].values  # 0~9 rows, 1~end columns
        row_j = data.iloc[j, 1:].values  # the first column is the label
        corr = np.corrcoef(row_i, row_j)[0, 1]
        correlations.append(corr)
    average_correlation = np.mean(correlations)
    return average_correlation


# Find the combination of 5 rows with the lowest average correlation
def find_lowest_correlation_combination(data):
    row_numbers = list(range(data.shape[0]))
    combinations_of_five = list(combinations(row_numbers, 5))
    # combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
    lowest_correlation = float("inf")  # set the initial lowest correlation to infinity
    best_combination = None

    for comb in combinations_of_five:
        avg_corr = compute_average_correlation(data, comb)
        if avg_corr < lowest_correlation:
            lowest_correlation = avg_corr
            best_combination = comb

    return best_combination, lowest_correlation


file_path = "./datasets/Val_ManufacturerA"  # change to your actual file path
original_data = load_data(file_path)
best_combination, lowest_correlation = find_lowest_correlation_combination(
    original_data
)
print("The combination of 5 rows with the lowest average correlation is:")
for i in best_combination:
    print(f"Row {i+1}")
print(f"With an average correlation of {lowest_correlation:.4f}")
