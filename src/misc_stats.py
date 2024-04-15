def mean_compare(df, col_1, col_2, title, separator, eur, sort_by=None, ascending=True):
    corr = df.groupby(col_1)[col_2].mean().reset_index()
    col_2_avg = col_2 + " Average"
    if eur:
        col_2_avg += " (EUR)"  # Append the currency suffix if needed

    # Rename columns with the new header
    corr.columns = [col_1, col_2_avg]

    # Ensure `col_1` maintains proper formatting
    corr[col_1] = corr[col_1].apply(
        lambda x: x.strip().title() if isinstance(x, str) else x
    )

    # Format the price as currency if applicable
    if eur:
        corr[col_2_avg] = corr[col_2_avg].apply(lambda x: f"€{x:,.2f}")

    # Sort the results if a sort column is provided
    if sort_by is not None:
        corr = corr.sort_values(by=sort_by, ascending=ascending)

    print(f"\n{separator} {title} {separator}\n")
    print(corr.to_string(index=False) + "\n")


def analyze(df, separator):
    mean_compare(
        df,
        "Rating",
        "Price",
        "Rating/Price analysis",
        separator,
        eur=True,
        sort_by="Rating",
        ascending=False,
    )
    mean_compare(
        df,
        "Brand",
        "Price",
        "Brand/Price analysis",
        separator,
        eur=True,
        sort_by="Brand",
        ascending=True,
    )
    mean_compare(
        df,
        "Brand",
        "Rating",
        "Brand/Rating analysis",
        separator,
        eur=False,
        sort_by="Rating Average",
        ascending=False,
    )
    mean_compare(
        df,
        "Warranty_Years",
        "Price",
        "Warranty/Price analysis",
        separator,
        eur=True,
        sort_by="Price Average (EUR)",
        ascending=False,
    )
