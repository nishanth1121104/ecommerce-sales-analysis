from profiling_customer import profiling_customer
from profiling_orders import profiling_orders
from profiling_order_items import profiling_order_items
from profiling_products import profiling_products
from profiling_payments import profiling_payments
from profiling_reviews import profiling_reviews
from profiling_sellers import profiling_sellers
from profiling_geolocation import profiling_geolocation


def run_all_profiles():

    print("\n========== STARTING DATA PROFILING ==========\n")

    profiling_customer()
    profiling_orders()
    profiling_order_items()
    profiling_products()
    profiling_payments()
    profiling_reviews()
    profiling_sellers()
    profiling_geolocation()

    print("\n========== PROFILING COMPLETED ==========\n")


if __name__ == "__main__":
    run_all_profiles()