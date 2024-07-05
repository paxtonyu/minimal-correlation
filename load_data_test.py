from time import sleep
from scipy.io import loadmat
import pandas as pd

file_path = "./datasets/original_data.mat"

mat = loadmat(file_path)

data = pd.DataFrame(mat["original_data"])
print(data[0:0, 0:0])
sleep(10)
