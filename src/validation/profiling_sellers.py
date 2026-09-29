import pandas as pd

FILE_PATH = "data/raw/olist_sellers_dataset.csv"


def profile_sellers():
    df = pd.read_csv(FILE_PATH)

    print("\n========== SELLERS PROFILE ==========")

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

    print("\nUnique seller_id:")
    print(df["seller_id"].nunique())


profiling_sellers = profile_sellers

if __name__ == "__main__":
    profile_sellers()