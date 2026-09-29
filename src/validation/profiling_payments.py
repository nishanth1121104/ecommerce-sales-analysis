import pandas as pd

FILE_PATH = "data/raw/olist_order_payments_dataset.csv"


def profile_payments():
    df = pd.read_csv(FILE_PATH)

    print("\n========== PAYMENTS PROFILE ==========")

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

    print("\nPayment types:")
    print(df["payment_type"].value_counts())

    print("\nPayment installments:")
    print(df["payment_installments"].value_counts().sort_index())


profiling_payments = profile_payments

if __name__ == "__main__":
    profile_payments()