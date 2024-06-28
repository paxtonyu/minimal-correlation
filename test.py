import pandas as pd
import numpy as np
from scipy.io import loadmat
import os
from itertools import combinations  # C(n,m)
import heapq

file_path = "./datasets/Val_ManufacturerA.xlsx"  # change to your actual file path
input_num = 10  # assuming the original data is 10 rows
output_num = 5  # number of rows to be selected


# Get the first ten original data
def load_data(file_path, input_num):
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

    original_data = data.iloc[:input_num, 1:]  # the first column is the label
    return original_data


# Compute the average correlation for a given set of rows
def compute_average_correlation(data, comb):
    correlations = []
    for i, j in combinations(comb, 2):  # combine each 2 rows in comb
        # if comb == (0,1,2), combinations(comb, 2) --> (0,1), (0,2), (1,2)
        row_i = data.iloc[i, :].values  # 0~9 rows, all columns
        row_j = data.iloc[j, :].values
        corr = np.corrcoef(row_i, row_j)[0, 1]
        correlations.append(corr)
    average_correlation = np.mean(correlations)
    return average_correlation


# Find the combination of 5 rows with the lowest average correlation
def find_lowest_correlation_combinations(data, output_num):
    row_numbers = list(range(data.shape[0]))
    the_combinations = list(combinations(row_numbers, output_num))
    # combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
    lowest_combinations = []

    for comb in the_combinations:  # comb = (0,1,2,3,4) etc..
        avg_corr = compute_average_correlation(data, comb)
        abs_avg_corr = abs(avg_corr)
        if len(lowest_combinations) < 3:
            heapq.heappush(lowest_combinations, (-abs_avg_corr, avg_corr, comb))
        else:
            heapq.heappushpop(lowest_combinations, (-abs_avg_corr, avg_corr, comb))
            # heapq.heappushpop(heap, (key, value,value2)) only the key is used to compare
            # heappushpop leaves smallest (key, value,value2) in the heap by comparing the key

    # Convert the heap to a sorted list
    lowest_combinations = [
        (-abs_corr, corr, comb) for abs_corr, corr, comb in lowest_combinations
    ]
    lowest_combinations.sort()

    return lowest_combinations


if __name__ == "__main__":
    original_data = load_data(file_path, input_num)
    lowest_combinations = find_lowest_correlation_combinations(
        original_data, output_num
    )
print(f"The 3 combinations with the smallest absolute average correlations are:")
for abs_corr, corr, comb in lowest_combinations:
    print(
        f"Combination {comb} with average correlation {corr:.6f} (absolute correlation {abs_corr:.6f})"
    )
