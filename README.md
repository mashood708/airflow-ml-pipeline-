# airflow-ml-pipeline-
# Airflow ML Pipeline for E-commerce Data

## 📌 Overview
This project implements an **end-to-end ETL + Machine Learning pipeline** using **Apache Airflow**, **PostgreSQL**, and **Streamlit Dashboard**.  
It automates:
- **Data Extraction**
- **Validation**
- **Transformation**
- **ML Predictions**
- **Loading into Database**
- **Interactive Dashboard Visualization**

---

## ✅ Tech Stack
- **Apache Airflow** – Workflow Orchestration
- **Python** – Scripts for ETL & ML
- **PostgreSQL** – Database Storage
- **Pandas, Scikit-learn** – Data Processing & ML
- **Docker & Docker Compose** – Containerization
- **Streamlit** – Dashboard for visualization

---

## ✅ Project Structure
airflow-ml-pipeline/
│
├── dags/
│ └── ecommerce_pipeline.py # Airflow DAG definition
│
├── scripts/
│ ├── extract.py # Extract raw data
│ ├── validate.py # Validate data
│ ├── transform.py # Transform data
│ ├── ml_predict.py # Generate predictions
│ └── load.py # Load data to PostgreSQL
│
├── dashboard/
│ └── app.py # Streamlit dashboard
│
├── docker-compose.yml # Docker setup
└── requirements.txt # Dependencies

yaml
Copy
Edit

---

## ✅ Features
✔ **ETL Automation** with Airflow  
✔ **ML Model** for price prediction  
✔ **PostgreSQL Integration**  
✔ **Interactive Dashboard** using Streamlit  

---

## ✅ Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/airflow-ml-pipeline.git
cd airflow-ml-pipeline
2️⃣ Start Services with Docker
bash
Copy
Edit
docker-compose up -d
3️⃣ Access Airflow Web UI
makefile
Copy
Edit
http://localhost:8080
Username: airflow | Password: airflow
4️⃣ Trigger DAG
Go to Airflow UI

Unpause and run ecommerce_ml_pipeline

5️⃣ Run Dashboard
bash
Copy
Edit
cd dashboard
streamlit run app.py
Open in browser:

arduino
Copy
Edit
http://localhost:8501
✅ Screenshots
(Add screenshots of Airflow UI and Streamlit dashboard here)

✅ Author
Muhammad Mashood Iqbal
📧 mashoodiqbal1122@gmail.com
📌 LinkedI
