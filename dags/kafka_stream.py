import uuid
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator



default_args ={
    'owner' : 'airscholar',
    'start_date': datetime(2026, 8 ,24, 00)

}

def stream_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api")
    print(res.json())

with DAG('user automation',
         default_args = default_args,
         schedule_interval ='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable= stream_data
    )

stream_data();