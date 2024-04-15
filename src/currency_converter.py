from forex_python.converter import CurrencyRates

c = CurrencyRates()


def convert(amount_in_inr, rate):
    amount_in_eur = amount_in_inr * rate
    return amount_in_eur


def convert_inr_to_eur(df, col):
    rate = c.get_rate("INR", "EUR")
    df[col] = df[col].apply(lambda x: convert(x, rate))
    return df
