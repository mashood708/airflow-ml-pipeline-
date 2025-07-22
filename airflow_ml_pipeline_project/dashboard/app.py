import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("📊 E-commerce Dashboard")

# DB Connection
engine = create_engine('postgresql+psycopg2://airflow:airflow@localhost:5432/airflow')

try:
    df = pd.read_sql("SELECT * FROM ecommerce_data", engine)
    st.success("✅ Data loaded from PostgreSQL")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

st.subheader("E-commerce Data with Predictions")
st.dataframe(df)

# Chart
st.subheader("Predicted Price by Product")
st.bar_chart(df[['product', 'predicted_price']].set_index('product'))


st.title("E-commerce Dashboard")

engine = create_engine('postgresql+psycopg2://airflow:airflow@localhost:5432/airflow')

try:
    df = pd.read_sql("SELECT * FROM ecommerce_data", engine)
    st.success("✅ Data loaded from PostgreSQL")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

st.subheader("E-commerce Data with Predictions")
st.dataframe(df)

st.subheader("Predicted Price by Product")
st.bar_chart(df[['product', 'predicted_price']].set_index('product'))
