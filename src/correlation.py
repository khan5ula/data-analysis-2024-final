import seaborn as sns
import matplotlib.pyplot as plt


def calculate_correlation(df):
    """
    Calculate and plot the correlation matrix as a heatmap for the specific key features in the dataset.

    This function computes the correlation matrix for the given DataFrame and plots it using
    seaborn's heatmap function. The features included in the correlation calculation are
    CPU frequency, RAM in GB, SSD storage in GB, weight in kg, price, and screen size in cm.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data. Must include the following columns:
    'CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'Weight_kg', 'Price', 'Screen_Size_cm'.

    Returns:
    None. Displays a heatmap of the correlations directly via matplotlib.

    Raises:
    KeyError: If any of the required columns are missing in the input DataFrame.
    """

    # Calculate correlations
    corr = df[
        [
            "CPU_frequency",
            "RAM_GB",
            "Storage_GB_SSD",
            "Weight_kg",
            "Price",
            "Screen_Size_cm",
        ]
    ].corr()

    # Plot heatmap of correlations
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.show()
