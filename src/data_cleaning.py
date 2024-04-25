import pandas as pd
from currency_converter import convert_inr_to_eur


def clean_data(df, separator):
    print(separator + " Data cleaning results " + separator + "\n")

    # Convert currency from INR to EUR
    df = convert_inr_to_eur(df, "Price")

    # Ensure that 'Warranty_Years' column is numeric, coerce non-numeric to NaN
    df["Warranty_Years"] = pd.to_numeric(df["Warranty_Years"], errors="coerce")

    # Drop rows with NaN in 'Warranty_Years'
    df.loc[:, "Brand"] = df["Brand"].str.title()

    # Make Brand column Proper Case
    df["Brand"] = df["Brand"].str.title()

    # Identify outliers in 'Price' - Example using IQR (Interquartile Range)
    Q1 = df["Price"].quantile(0.25)
    Q3 = df["Price"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter to keep only outliers in order to see how many of them there are
    outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]

    # Printing the number of outliers
    if not outliers.empty:  # Check if the outliers dataframe is not empty
        print(
            f"Found and removed {outliers.shape[0]} outliers from the data using IQR (Interquartile Range)"
        )

    # Filter out outliers
    df_clean = df[(df["Price"] >= lower_bound) & (df["Price"] <= upper_bound)]

    # Check for duplicates
    duplicate_rows = df_clean.duplicated().sum()

    # Printing the number of duplicate rows
    if duplicate_rows > 0:
        print(f"Number of duplicate rows: {duplicate_rows}")

    # Drop duplicates
    df_clean = df_clean.drop_duplicates()

    return df_clean
