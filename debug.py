from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook

def check_smtp_connection():
    try:
        conn = BaseHook.get_connection('smtp_default')
        print(f"Host: {conn.host}")
        print(f"Port: {conn.port}")
        print(f"Login: {conn.login}")
        print(f"Extra: {conn.extra}")
        print(f"Schema: {conn.schema}")
        return "Connection details printed successfully"
    except Exception as e:
        print(f"Error getting connection: {e}")
        return f"Error: {e}"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 11),
    'retries': 0,
}

dag = DAG(
    'debug_smtp_connection',
    default_args=default_args,
    description='Debug SMTP connection settings',
    schedule=None,  # Manual trigger only
    catchup=False,
)

debug_task = PythonOperator(
    task_id='check_smtp_settings',
    python_callable=check_smtp_connection,
    dag=dag,
)