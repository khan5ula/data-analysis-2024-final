import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


def regression_analysis(df, target_col, *feature_cols):
    """
    Performs linear regression analysis on provided dataset to predict prices based on desired attributes.

    Parameters:
    df (pandas.DataFrame): The DataFrame
    target_col (int or float): The target column of the DataFrame
    *feature_cols (int or float): The feature columns of the DataFrame.

    Outputs:
    None. Prints the Mean Squared Error (MSE) and R-squared values of the model to the console and displays a
    scatter plot of actual vs. predicted prices.

    Returns:
    None. The function is used for performing the analysis and visualizing the results.

    Raises:
    KeyError: If any of the required columns ('RAM_GB', 'Storage_GB_SSD', 'Price') are missing.
    ValueError: If there are non-numeric entries in the required columns.
    """

    # Selecting the features and the target
    X = df[[col for col in feature_cols]]
    y = df[target_col]

    # Splitting the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Creating the regression model
    model = LinearRegression()

    # Fitting the model
    model.fit(X_train, y_train)

    # Making predictions
    y_pred = model.predict(X_test)

    # Evaluating the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    # Plotting the results for visualization
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual Prices vs. Predicted Prices")
    plt.show()
