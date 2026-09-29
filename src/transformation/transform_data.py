import pandas as pd
import os


RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"


def create_processed_folder():
    os.makedirs(PROCESSED_PATH, exist_ok=True)


def transform_customers():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_customers_dataset.csv"
    )

    # Remove completely duplicated rows
    df = df.drop_duplicates()

    # Standardize text
    df["customer_city"] = (
        df["customer_city"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df["customer_state"] = (
        df["customer_state"]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    # Required IDs cannot be missing
    df = df.dropna(
        subset=["customer_id", "customer_unique_id"]
    )

    df.to_csv(
        f"{PROCESSED_PATH}/customers_clean.csv",
        index=False
    )

    print(f"Customers processed: {len(df)} rows")


def transform_orders():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_orders_dataset.csv"
    )

    df = df.drop_duplicates()

    # Convert date columns
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

    # Required IDs
    df = df.dropna(
        subset=["order_id", "customer_id"]
    )

    df.to_csv(
        f"{PROCESSED_PATH}/orders_clean.csv",
        index=False
    )

    print(f"Orders processed: {len(df)} rows")


def transform_order_items():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_order_items_dataset.csv"
    )

    df = df.drop_duplicates()

    df["shipping_limit_date"] = pd.to_datetime(
        df["shipping_limit_date"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "order_id",
            "product_id",
            "seller_id"
        ]
    )

    df.to_csv(
        f"{PROCESSED_PATH}/order_items_clean.csv",
        index=False
    )

    print(f"Order items processed: {len(df)} rows")


def transform_products():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_products_dataset.csv"
    )

    df = df.drop_duplicates()

    df["product_category_name"] = (
        df["product_category_name"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df = df.dropna(
        subset=["product_id"]
    )

    df.to_csv(
        f"{PROCESSED_PATH}/products_clean.csv",
        index=False
    )

    print(f"Products processed: {len(df)} rows")


def transform_payments():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_order_payments_dataset.csv"
    )

    df = df.drop_duplicates()

    df["payment_type"] = (
        df["payment_type"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df = df.dropna(
        subset=["order_id"]
    )

    df.to_csv(
        f"{PROCESSED_PATH}/payments_clean.csv",
        index=False
    )

    print(f"Payments processed: {len(df)} rows")


def transform_reviews():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_order_reviews_dataset.csv"
    )

    df = df.drop_duplicates()

    date_columns = [
        "review_creation_date",
        "review_answer_timestamp"
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

    df = df.dropna(
        subset=["review_id", "order_id"]
    )

    df.to_csv(
        f"{PROCESSED_PATH}/reviews_clean.csv",
        index=False
    )

    print(f"Reviews processed: {len(df)} rows")


def transform_sellers():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_sellers_dataset.csv"
    )

    df = df.drop_duplicates()

    df["seller_city"] = (
        df["seller_city"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df["seller_state"] = (
        df["seller_state"]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    df = df.dropna(
        subset=["seller_id"]
    )

    df.to_csv(
        f"{PROCESSED_PATH}/sellers_clean.csv",
        index=False
    )

    print(f"Sellers processed: {len(df)} rows")


def transform_geolocation():

    df = pd.read_csv(
        f"{RAW_PATH}/olist_geolocation_dataset.csv"
    )

    # This dataset contains 261,831 completely duplicated rows
    # according to our profiling.
    df = df.drop_duplicates()

    df["geolocation_city"] = (
        df["geolocation_city"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df["geolocation_state"] = (
        df["geolocation_state"]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    df.to_csv(
        f"{PROCESSED_PATH}/geolocation_clean.csv",
        index=False
    )

    print(f"Geolocation processed: {len(df)} rows")


def main():

    print("\n========== STARTING TRANSFORMATION ==========\n")

    create_processed_folder()

    transform_customers()
    transform_orders()
    transform_order_items()
    transform_products()
    transform_payments()
    transform_reviews()
    transform_sellers()
    transform_geolocation()

    print("\n========== TRANSFORMATION COMPLETED ==========\n")


if __name__ == "__main__":
    main()