import pandas as pd

FILE_PATH = "data/raw/olist_customers_dataset.csv"


def profiling_customer():
    df = pd.read_csv(FILE_PATH)

    print("\n========== CUSTOMER DATA PROFILE ==========")

    print("Shape:")
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

    print("\nUnique customer_id:")
    print(df["customer_id"].nunique())

    print("\nUnique customer_unique_id:")
    print(df["customer_unique_id"].nunique())

    print("\nDuplicate customer_id:")
    print(df["customer_id"].duplicated().sum())

    print("\nDuplicate customer_unique_id:")
    print(df["customer_unique_id"].duplicated().sum())

    customer_mapping = (
        df.groupby("customer_unique_id")["customer_id"]
          .nunique()
    )

    print(customer_mapping.value_counts().sort_index())


profile_customer = profiling_customer

if __name__ == "__main__":
    profiling_customer()
