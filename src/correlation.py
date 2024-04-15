import seaborn as sns
import matplotlib.pyplot as plt


def calculate_correlation(df, attributes):
    # Calculate correlations
    corr = df[attributes].corr()

    # Plot heatmap of correlations
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.show()
