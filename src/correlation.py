import seaborn as sns
import matplotlib.pyplot as plt


def calculate_correlation(df, attributes, output_file):
    # Calculate correlations
    corr = df[attributes].corr()

    # Plot heatmap of correlations
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")

    # Save the figure
    plt.savefig(output_file, format="png", dpi=300)

    # Optionally clear the plot after saving if further plotting is to be done
    plt.close()
