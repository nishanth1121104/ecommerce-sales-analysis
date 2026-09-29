import pandas as pd

FILE_PATH = "data/raw/olist_order_reviews_dataset.csv"


def profile_reviews():
    df = pd.read_csv(FILE_PATH)

    print("\n========== REVIEWS PROFILE ==========")

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

    print("\nUnique review_id:")
    print(df["review_id"].nunique())

    print("\nUnique order_id:")
    print(df["order_id"].nunique())

    print("\nReview score:")
    print(df["review_score"].value_counts().sort_index())


profiling_reviews = profile_reviews

if __name__ == "__main__":
    profile_reviews()