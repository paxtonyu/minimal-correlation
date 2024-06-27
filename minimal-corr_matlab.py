import pandas as pd
import numpy as np
from scipy.io import loadmat


# Get the first ten spectral data
def load_data(file_path):
    mat = loadmat(file_path)
    # Assuming the spectral data is stored in a variable named 'Spectral_data' in the MATLAB file
    Spectral_data = pd.DataFrame(mat["Spectral_data"])
    Spectral_data = Spectral_data.iloc[:10, :]
    return Spectral_data


# Select the 5 filters with the lowest correlation among the 10 filters
def compute_lowest_correlations(data, N):
    rows, cols = data.shape
    correlations = []

    for i in range(rows):
        for j in range(i + 1, rows):
            row_i = data.iloc[i, :].values
            row_j = data.iloc[j, :].values
            corr = np.corrcoef(row_i, row_j)[0, 1]
            correlations.append(((i, j), corr))

    lowest_correlations = sorted(correlations, key=lambda item: abs(item[1]))[:N]
    return lowest_correlations


file_path = "./datasets/Val_ManufacturerA.mat"
Spectral_data = load_data(file_path)
lowest_correlations = compute_lowest_correlations(Spectral_data, 5)
print("The 5 pairs of rows with the lowest correlations are:")
for (i, j), corr in lowest_correlations:
    print(f"Rows {i+1} and {j+1} with correlation {corr:.4f}")
