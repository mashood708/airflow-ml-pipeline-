import pandas as pd

# Dummy product data
data = {
    'product': ['Laptop', 'Phone', 'Headphones'],
    'price': [1000, 500, 100],
    'rating': [4.5, 4.2, 4.0]
}

df = pd.DataFrame(data)
df.to_csv('/opt/airflow/scripts/raw_data.csv', index=False)
print("✅ Data extracted and saved to raw_data.csv")
