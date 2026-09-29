import pandas as pd

FILE_PATH = "data/raw/olist_geolocation_dataset.csv"


def profile_geolocation():
    df = pd.read_csv(FILE_PATH)

    print("\n========== GEOLOCATION PROFILE ==========")

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

    print("\nUnique ZIP prefixes:")
    print(df["geolocation_zip_code_prefix"].nunique())


profiling_geolocation = profile_geolocation

if __name__ == "__main__":
    profile_geolocation()