def transform_data(sales, treatments):

    # sort for consistent merge
    sales = sales.sort_values("sale_id").reset_index(drop=True)
    treatments = treatments.sort_values("patient_id").reset_index(drop=True)

    # merge datasets
    merged = sales.merge(
        treatments,
        left_index=True,
        right_index=True
    )

    # remove duplicate columns from merge
    merged = merged.drop(columns=["hospital_y", "year_y"])

    # rename remaining columns
    merged = merged.rename(columns={
        "hospital_x": "hospital",
        "year_x": "year"
    })

    return merged