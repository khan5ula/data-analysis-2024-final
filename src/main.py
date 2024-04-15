import sys
import pandas as pd
from data_cleaning import clean_data
from price_distribution import show_price_distribution
from correlation import calculate_correlation
from misc_stats import analyze

separator = "------------"
file_path = "data/laptops.csv"

data = pd.read_csv(file_path)


correlation_attributes = [
    "Price",
    "Rating",
    "Cores",
    "Threads",
    "RAM",
    "Primary_Storage_Capacity",
    "Display_Size",
]

# Create a heatmap of the key values of the dataset
# calculate_correlation(data_clean, correlation_attributes)

# Show price distribution
# show_price_distribution(data_clean)

# Save output to a file
original_stdout = sys.stdout  # Save a reference to the original standard output
with open(
    "/home/kristian/oulun_yliopisto/courses/2024/data-analis/final-assignment/output.txt",
    "w",
) as f:
    sys.stdout = f  # Change the standard output to the file we created.

    # Clean the data before conducting analysis
    data_clean = clean_data(data, separator)

    # Conduct a series for miscellaneous analysis
    analyze(data_clean, separator)

    sys.stdout = original_stdout  # Reset the standard output to its original value
