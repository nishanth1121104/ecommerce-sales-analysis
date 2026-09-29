import pandas as pd

FILE_PATH = "data/raw/olist_order_items_dataset.csv"


def profile_order_items():
    df = pd.read_csv(FILE_PATH)

    print("\n========== ORDER ITEMS PROFILE ==========")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nUnique order_id:")
    print(df["order_id"].nunique())

    print("\nUnique product_id:")
    print(df["product_id"].nunique())

    print("\nUnique seller_id:")
    print(df["seller_id"].nunique())


profiling_order_items = profile_order_items

if __name__ == "__main__":
    profile_order_items()