import pandas as pd

df = pd.read_csv('/opt/airflow/scripts/raw_data.csv')
if df.isnull().values.any():
    raise ValueError("❌ Validation failed: Missing values found!")
else:
    print("✅ Data validation passed!")
