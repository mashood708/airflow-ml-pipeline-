from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    dag_id='ecommerce_ml_pipeline',
    default_args=default_args,
    description='ETL + ML Pipeline for E-commerce Data',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id='extract_data',
        bash_command='python /opt/airflow/scripts/extract.py'
    )

    validate = BashOperator(
        task_id='validate_data',
        bash_command='python /opt/airflow/scripts/validate.py'
    )

    transform = BashOperator(
        task_id='transform_data',
        bash_command='python /opt/airflow/scripts/transform.py'
    )

    predict = BashOperator(
        task_id='ml_predict',
        bash_command='python /opt/airflow/scripts/ml_predict.py'
    )

    load = BashOperator(
        task_id='load_data',
        bash_command='python /opt/airflow/scripts/load.py'
    )

    extract >> validate >> transform >> predict >> load
