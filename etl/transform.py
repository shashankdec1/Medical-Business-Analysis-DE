
def transform_data(sales, treatments):
    merged = sales.merge(
        treatments,
        on=["hospital","year"],
        how="left"
    )
    return merged
