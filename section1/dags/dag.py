from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta
import sys
sys.path.append('/Users/junwei/Desktop/tap2023_dsaidde/section1/scripts')
import data_processing

default_args = {
    'owner': 'adminjw',
    'depends_pn_past': False,
    'email': ['june.teo6@hotmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=30),
}

with DAG(
    'processing_dataset',
    default_args=default_args,
    description='processing dataset',
    schedule_interval='0 1 * * *',
    start_date=datetime(2021,1,1),
    catchup=False,
    tags=['retrieve'],
) as dag:
    dag.doc_md = """ This is a dag for processing data"""
    processing_dataset_task = PythonOperator(
        task_id = 'process_data',
        python_callable = data_processing.process)