import seaborn as sns
import matplotlib.pyplot as plt


def show_price_distribution(df):
    sns.histplot(df["Price"], kde=True)
    plt.title("Price Distribution")
    plt.show()

    sns.boxplot(x=df["Price"])
    plt.title("Price Range")
    plt.show()
