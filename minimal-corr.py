import pandas as pd
import numpy as np
from scipy.io import loadmat
import os


# Get the first ten original data
def load_data(file_path):
    file_extension = os.path.splitext(file_path)[1]

    if file_extension == ".xlsx":
        data = pd.read_excel(file_path)
    elif file_extension == ".mat":
        mat = loadmat(file_path)
        # Assuming the original data is stored in a variable named 'Original_data' in the MATLAB file
        data = pd.DataFrame(mat["Original_data"])
    else:
        raise ValueError(
            "Unsupported file format. Please provide a .xlsx or .mat file."
        )

    original_data = data.iloc[:10, :]  # 0~9row, all column
    return original_data


# Select the 5 filters with the lowest correlation among the 10 filters
def compute_lowest_correlations(data, N):
    rows, cols = data.shape
    correlations = []

    for i in range(rows):
        for j in range(i + 1, rows):
            row_i = data.iloc[i, 1:].values  # 0~9 rows, 1:end columns
            row_j = data.iloc[j, 1:].values  # the first column is the label
            corr = np.corrcoef(row_i, row_j)[0, 1]
            correlations.append(((i, j), corr))

    lowest_correlations = sorted(correlations, key=lambda item: abs(item[1]))[:N]
    return lowest_correlations


file_path = "./datasets/Val_ManufacturerA.xlsx"  # change to your actual file path
Original_data = load_data(file_path)
lowest_correlations = compute_lowest_correlations(Original_data, 5)
print("The 5 pairs of rows with the lowest correlations are:")
for (i, j), corr in lowest_correlations:
    print(f"Rows {i+1} and {j+1} with correlation {corr:.4f}")
