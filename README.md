# minimal-correlation-group

Select the 5 filters with the lowest average correlation coefficient among the 10 filters

$$\rho_{X Y}=\frac{Cov(X, Y)}{\sqrt{D(X)} \sqrt{D(Y)}}=\frac{n \sum x y-\sum x \sum y}{\sqrt{n \sum x^{2}-\left(\sum x\right)^{2}} \sqrt{n \sum y^{2}-\left(\sum y\right)^{2}}}$$

the main program is [minimal_corr.py](minimal_corr.py)

you can change the `input_num` and `output_num` to change the number of rows you want to select

change the `file_path` variable to your actual file path

the first column is automatically ignored by the program if it is an id.

because of the reading mechanism of panda, the first row of the excel file should be the label, and the second row should be the data, while the first row of the mat file is the data.

the mat data should be sorted in  a variable named `original_data` in the `.mat` file
