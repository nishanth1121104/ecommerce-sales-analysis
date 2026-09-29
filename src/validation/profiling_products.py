import pandas as pd

FILE_PATH = "data/raw/olist_products_dataset.csv"


def profile_products():
    df = pd.read_csv(FILE_PATH)

    print("\n========== PRODUCTS PROFILE ==========")

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

    print("\nUnique product_id:")
    print(df["product_id"].nunique())


profiling_products = profile_products

if __name__ == "__main__":
    profile_products()