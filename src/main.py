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


# Save output to a file
original_stdout = sys.stdout  # Save a reference to the original standard output
with open(
    "/home/kristian/oulun_yliopisto/courses/2024/data-analis/final-assignment/code/results/output.txt",
    "w",
) as f:
    try:
        sys.stdout = f  # Change the standard output to the file we created.

        # Clean the data before conducting analysis
        data_clean = clean_data(data, separator)

        # Create a heatmap of the key values of the dataset
        corr_filepath = "/home/kristian/oulun_yliopisto/courses/2024/data-analis/final-assignment/code/results/heatmap.png"
        calculate_correlation(data_clean, correlation_attributes, corr_filepath)

        # Display price range distribution
        pr_range_filepath = "/home/kristian/oulun_yliopisto/courses/2024/data-analis/final-assignment/code/results/price_range.png"
        pr_dist_filepath = "/home/kristian/oulun_yliopisto/courses/2024/data-analis/final-assignment/code/results/price_distribution.png"
        show_price_distribution(data_clean, pr_range_filepath, pr_dist_filepath)

        # Conduct a series for miscellaneous analysis
        analyze(data_clean, separator)

        sys.stdout = original_stdout  # Reset the standard output to its original value
    except Exception as e:
        print("An error occurred:", e)
