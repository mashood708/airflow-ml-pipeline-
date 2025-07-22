import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/opt/airflow/scripts/transformed_data.csv')

X = df[['rating']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

df['predicted_price'] = model.predict(X)
df.to_csv('/opt/airflow/scripts/predicted_data.csv', index=False)
print("✅ ML predictions done and saved to predicted_data.csv")
