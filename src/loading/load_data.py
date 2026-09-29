import pandas as pd

from database import get_engine


PROCESSED_PATH = "data/processed"


TABLES = {
    "customers": "customers_clean.csv",
    "orders": "orders_clean.csv",
    "order_items": "order_items_clean.csv",
    "products": "products_clean.csv",
    "payments": "payments_clean.csv",
    "reviews": "reviews_clean.csv",
    "sellers": "sellers_clean.csv",
    "geolocation": "geolocation_clean.csv"
}


def load_data():

    engine = get_engine()

    for table_name, file_name in TABLES.items():

        print(f"\nLoading {table_name}...")

        file_path = f"{PROCESSED_PATH}/{file_name}"

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(
            f"{table_name}: {len(df)} rows loaded"
        )


if __name__ == "__main__":
    load_data()