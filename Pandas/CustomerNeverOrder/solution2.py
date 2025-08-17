import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    not_in_customers = customers[~customers["id"].isin(orders["customerId"])]
    not_in_customers = not_in_customers.rename(columns={"id": "id", "name": "Customers"})
    return not_in_customers[["Customers"]]
