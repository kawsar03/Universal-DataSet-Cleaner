import pandas as pd  # pandas helps us handle spreadsheet-like data
import numpy as np   # numpy helps us work with numbers
from scipy import stats  # scipy helps us detect outliers using statistics

def clean_csv_data(file_path, output_path="cleaned_data.csv", zscore_threshold=3.0):
    # Step 1: Load your spreadsheet (CSV file) into a table-like format
    df = pd.read_csv(file_path)

    # Step 2: Make column names clean and consistent
    # This lowers all letters, removes extra spaces, and replaces spaces with underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Step 3: Get rid of any duplicate rows in the data
    # This prevents counting the same record more than once
    df = df.drop_duplicates()

    # Step 4: Drop columns with 65% or more missing data
    # If too much data is missing in a column, it may not be useful
    missing_percent = df.isnull().mean()  # find how much data is missing per column
    df = df.loc[:, missing_percent < 0.65]  # keep only columns that are mostly filled

    # Step 5: Fill in the missing values in each column
    for col in df.columns:
        if df[col].dtype in [np.float64, np.int64, 'float64', 'int64']:
            # If the column has numbers, fill blanks with the average of that column
            df[col] = df[col].fillna(df[col].mean())
        else:
            # If the column has words or categories, fill blanks with the most common value
            # If that doesn’t exist, fill with “Unknown”
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")

    # Step 6: Round and convert all numeric values to whole numbers
    numeric_cols = df.select_dtypes(include=[np.number]).columns  # find columns with numbers
    for col in numeric_cols:
        df[col] = df[col].round().astype(int)  # round numbers and turn them into integers

    # Step 7: Remove extreme values (outliers) using Z-score method
    # Z-score tells how far a value is from the average
    # If it's too far (e.g., 3 standard deviations), it's likely an error or extreme case
    for col in numeric_cols:
        z_scores = np.abs(stats.zscore(df[col]))  # how extreme each number is
        df = df[z_scores < zscore_threshold]  # keep only "normal" values

    # Step 8: Save the cleaned data to a new CSV file
    df.to_csv(output_path, index=False)
    print(f"Data cleaned and saved to {output_path}")
