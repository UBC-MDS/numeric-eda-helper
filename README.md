# numeric-eda-helper

Data scientists often spend alot of time preprocessing data to extract useful parts for their analysis. The numeric-eda-helper package is a package that aims to streamline Exploratory Data Analysis, specifically for numeric data in datasets. The goal is to simplify some common and repetitive tasks during EDA and data preprocessing for data analysts, as well as add value to their workflow by presenting some useful insights in a quick manner (just calling our functions), such as displaying highly-correlated variables and outliers. 

The package includes functions which can complete the following tasks:

- Display some useful statistics
- Detect outliers
- Deal with missing values
- Check for correlation between features  

## Function descriptions

- `flag_outliers`: This function helps to display numeric variables which contain outliers that exceed a certain user-specified threshold percentage, using the interquartile range method. Users can then take note of these variables with high percentage of outliers and decide what to do with the variable(s). 

## Similar Work

In the Python open-source ecosystem, there exists some useful packages that already  tackle EDA and preprocessing, but our goal is to make it even more light-weighted, fast and specifically tailored to present numeric EDA insights. One popular and useful package that can generate EDA reports is: 

- [`pandasprofiling`](https://github.com/pandas-profiling/pandas-profiling)


## Contributors

We welcome all contributions and the current main contributors are:

-   Anupriya Srivastava 
-   Jiwei Hu 
-   Michelle Wang 
-   Samuel Quist


## License

Licensed under the terms of the MIT license.

## Credits

`numeric-eda-helper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
