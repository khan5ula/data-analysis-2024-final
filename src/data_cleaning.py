import pandas as pd


def clean_data(df):
    """
    Cleans the input DataFrame by handling missing values, filtering outliers, and removing duplicates.

    This function performs several data cleaning operations: it imputes missing values in the 'Screen_Size_cm'
    and 'Weight_kg' columns, identifies and filters out price outliers using the Interquartile Range (IQR)
    method, and removes any duplicate rows. Throughout the process, it provides console outputs to show the
    number of missing values, outliers, and duplicates.

    Parameters:
    df (pandas.DataFrame): A DataFrame containing the data to be cleaned. Requires the following columns:
    'Screen_Size_cm', 'Weight_kg', and 'Price'.

    Returns:
    pandas.DataFrame: A cleaned DataFrame with outliers and duplicates removed.

    Raises:
    KeyError: If the required columns are missing in the input DataFrame.
    ValueError: If the operations encounter a type mismatch or other calculation errors related to data types.
    """

    # Check for missing values
    print(df.isnull().sum())

    # Impute missing values for 'Screen_Size_cm' with the median
    df.fillna({"Screen_Size_cm": df["Screen_Size_cm"].median()}, inplace=True)

    # Impute missing values for 'Weight_kg' with the mean
    df.fillna({"Weight_kg": df["Weight_kg"].mean()}, inplace=True)

    # Identify outliers in 'Price' - Example using IQR (Interquartile Range)
    Q1 = df["Price"].quantile(0.25)
    Q3 = df["Price"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter to keep only outliers in order to see how many of them there are
    outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]

    # Printing the number of outliers
    print("Number of outliers found: ", outliers.shape[0])

    # Filter out outliers
    df_clean = df[(df["Price"] >= lower_bound) & (df["Price"] <= upper_bound)]

    # Check for duplicates
    duplicate_rows = df_clean.duplicated().sum()
    print("Number of duplicate rows: {duplicate_rows}")

    # Drop duplicates
    df_clean = df_clean.drop_duplicates()

    # Final check
    print(df_clean.info())
    print()

    return df_clean
