# E-Commerce Sales Analysis

An end-to-end e-commerce data analysis project using Python, SQL, and Power BI.

## 📊 Project Overview

This project analyzes e-commerce sales data to understand sales performance, customer behavior, payment methods, order status, product categories, and delivery performance.

The project follows a complete data analytics workflow:

- Data loading
- Data cleaning
- Data validation and profiling
- SQL business analysis
- Power BI dashboard development

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- SQL
- SQLite
- Power BI
- Git & GitHub

## 📁 Project Structure

```text
ecommerce-sales-analysis/
│
├── data/
│   └── processed/
│       ├── customers_clean.csv
│       ├── geolocation_clean.csv
│       ├── order_items_clean.csv
│       ├── orders_clean.csv
│       ├── payments_clean.csv
│       ├── products_clean.csv
│       ├── reviews_clean.csv
│       └── sellers_clean.csv
│
├── sql/
│   └── business_analysis.sql
│
├── src/
│   ├── loading/
│   │   ├── database.py
│   │   └── load_data.py
│   │
│   ├── transformation/
│   │   └── transform_data.py
│   │
│   └── validation/
│       ├── profile_all.py
│       ├── profiling_customer.py
│       ├── profiling_geolocation.py
│       ├── profiling_order_items.py
│       ├── profiling_orders.py
│       ├── profiling_payments.py
│       ├── profiling_products.py
│       ├── profiling_reviews.py
│       └── profiling_sellers.py
│
├── ecommerce_dashboard.pbix
├── requirements.txt
├── .gitignore
└── README.md