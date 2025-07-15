# Universal-DataSet-Cleaner
Import datasets to this script to clean it up with ease

Overview
This project provides a general-purpose Python script for cleaning CSV files. It is designed to automate and standardize the preprocessing of tabular datasets by handling missing values, duplicate entries, inconsistent formatting, and outliers. The goal is to prepare real-world data for downstream analysis or machine learning workflows with minimal manual effort.

Skills and Tools Utilized
Programming Language:

Python

Libraries:

Pandas – for reading, cleaning, and transforming tabular data.

NumPy – for numerical computations and handling missing data.

SciPy – for statistical operations, particularly outlier detection using the Z-score method.

Data Processing Concepts:

Data type inference and handling

Duplicate removal

Null value management

Column name normalization

Outlier detection and removal

Data type conversion (to integers)

Functionality Summary
The script automates the following data cleaning steps:

Reading the dataset: Loads a CSV file into a structured DataFrame.

Standardizing column names: Strips whitespace, converts to lowercase, and replaces spaces with underscores to ensure uniformity.

Removing duplicate rows: Ensures there are no redundant data entries.

Dropping columns with excessive null values: Any column with 65% or more missing data is removed.

Filling remaining missing values:

For numeric columns: missing values are filled with the column's mean.

For non-numeric (categorical) columns: missing values are filled with the most frequent value (mode), or "Unknown" if no mode exists.

Rounding and converting numeric values: All numeric columns are rounded and cast to integers to simplify the dataset and reduce memory usage.

Outlier removal using Z-score:

The Z-score is a measure of how many standard deviations a value is from the mean.

Rows with Z-scores above a configurable threshold (default = 3.0) are removed as statistical outliers.

Saving the cleaned data: The cleaned dataset is saved as a new CSV file.
