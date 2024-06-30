# minimal-correlation-group

Select the 5 filters with the lowest average correlation coefficient among the 10 filters

$$\rho_{X Y}=\frac{\operatorname{Cov}(X, Y)}{\sqrt{D(X)} \sqrt{D(Y)}}=\frac{n \sum x y-\sum x \sum y}{\sqrt{n \sum x^{2}-\left(\sum x\right)^{2}} \sqrt{n \sum y^{2}-\left(\sum y\right)^{2}}}$$

the main program is [minimal_corr.py](minimal_corr.py)

you can change the `input_num` and `output_num` to change the number of rows you want to select

change the `file_path` variable to your actual file path

the mat data should be sorted in  a variable named `original_data` in the `.mat` file
