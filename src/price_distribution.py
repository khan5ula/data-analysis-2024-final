import seaborn as sns
import matplotlib.pyplot as plt


def show_price_distribution(df, distribution_file, range_file):
    sns.histplot(df["Price"], kde=True)
    plt.title("Price Distribution")
    plt.savefig(distribution_file, format="png", dpi=300)

    sns.boxplot(x=df["Price"])
    plt.title("Price Range")

    # Save the figure
    plt.savefig(range_file, format="png", dpi=300)
