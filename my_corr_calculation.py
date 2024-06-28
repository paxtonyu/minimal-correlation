import numpy as np


def pearson_correlation(X, Y):
    n = len(X)

    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_x_sq = np.sum(X**2)
    sum_y_sq = np.sum(Y**2)
    sum_xy = np.sum(X * Y)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt((n * sum_x_sq - sum_x**2) * (n * sum_y_sq - sum_y**2))

    if denominator == 0:
        return 0  # To handle division by zero if variance is zero

    correlation = numerator / denominator
    return correlation


np.random.seed(0)  # Fixed random number seed to ensure repeatable results
X = np.random.rand(741)
Y = np.random.rand(741)

correlation = pearson_correlation(X, Y)
corr = np.corrcoef(X, Y)[0, 1]
print(f"my correlation coefficient is {correlation:.6f}")
print(f"numpy correlation coefficient is {corr:.6f}")
