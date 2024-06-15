# 导入前10条excle数据
import pandas as pd
import numpy as np

file_path = ".\datasets\Val_ManufacturerA.xlsx"


def load_data(file_path):
    data = pd.read_excel(file_path)
    Spectral_data = data.iloc[:10, :]
    return Spectral_data


Spectral_data = load_data(file_path)
print(Spectral_data)
