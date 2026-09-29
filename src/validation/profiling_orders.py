import pandas as pd


# Location of our raw orders dataset
FILE_PATH = "data/raw/olist_orders_dataset.csv"


def profile_orders():

    # 1. Read the CSV file
    df = pd.read_csv(FILE_PATH)

    print("\n========== ORDER DATA PROFILE ==========")

    # 2. Check the size of the dataset
    print("\nShape:")
    print(df.shape)

    # 3. Check what columns exist
    print("\nColumns:")
    print(df.columns.tolist())

    # 4. Check the type of data in each column
    print("\nData types:")
    print(df.dtypes)

    # 5. Look at the first 5 records
    print("\nFirst 5 rows:")
    print(df.head())

    # 6. Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # 7. Check completely duplicated rows
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    # 8. Check how many different orders exist
    print("\nUnique order_id:")
    print(df["order_id"].nunique())

    # 9. Check how many different customer IDs exist
    print("\nUnique customer_id:")
    print(df["customer_id"].nunique())

    # 10. Check the different order statuses
    print("\nOrder status:")
    print(df["order_status"].value_counts())

    # 11. Count how many orders each customer_id has
    print("\nCustomer order distribution:")

    order_counts = df["customer_id"].value_counts()

    print(
        order_counts
        .value_counts()
        .sort_index()
    )


# Alias for compatibility
profiling_orders = profile_orders

if __name__ == "__main__":
    profile_orders()