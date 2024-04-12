import pandas as pd
from data_cleaning import clean_data
from correlation import calculate_correlation
from regression_analysis import regression_analysis

file_path = "../data/laptop_pricing_dataset.csv"

data = pd.read_csv(file_path)

# Clean the data before conducting analysis
data_clean = clean_data(data)

# Create a heatmap of the key values of the dataset
calculate_correlation(data_clean)

# Conduct linear regression analysis to predict prices based on key attributes
regression_analysis(
    data_clean,
    "Price",
    *["RAM_GB", "Storage_GB_SSD", "GPU", "CPU_core", "CPU_frequency"],
)
