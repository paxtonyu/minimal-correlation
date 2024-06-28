import numpy as np
import math


def calculate_corr(X, Y):
    X_avg = sum(X) / len(X)
    Y_avg = sum(Y) / len(Y)

    # 计算分子，协方差————按照协方差公式，本来要除以n的，由于在相关系数中上下同时约去了n，于是可以不除以n
    cov_XY = sum([(x - X_avg) * (y - Y_avg) for x, y in zip(X, Y)])

    # 计算分母，方差乘积————方差本来也要除以n，在相关系数中上下同时约去了n，于是可以不除以n
    sq = math.sqrt(
        sum([(x - X_avg) ** 2 for x in X]) * sum([(x - Y_avg) ** 2 for x in Y])
    )

    corr_factor = cov_XY / sq

    return corr_factor


row_i = [1, 2, 3, 4, 5]
row_j = [6, 7, 8, 9, 10]
corr = np.corrcoef(row_i, row_j)[0, 1]

print(corr)
