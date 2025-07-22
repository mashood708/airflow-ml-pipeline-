import pandas as pd

df = pd.read_csv('/opt/airflow/scripts/raw_data.csv')
df['discount_price'] = df['price'] * 0.9
df.to_csv('/opt/airflow/scripts/transformed_data.csv', index=False)
print("✅ Data transformed and saved to transformed_data.csv")
