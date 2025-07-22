import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('/opt/airflow/scripts/predicted_data.csv')

engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres:5432/airflow')
df.to_sql('ecommerce_data', engine, if_exists='replace', index=False)
print("✅ Data loaded into PostgreSQL table: ecommerce_data")


df = pd.read_csv('/opt/airflow/scripts/predicted_data.csv')

engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres:5432/airflow')
df.to_sql('ecommerce_data', engine, if_exists='replace', index=False)
print("✅ Data loaded into PostgreSQL table: ecommerce_data")
