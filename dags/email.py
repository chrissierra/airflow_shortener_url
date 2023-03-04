from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
from airflow import DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['christopher.sierra@usach.cl'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
with DAG(
    'email_tutorial',
    default_args=default_args,
    description='A simple email ',
    schedule_interval='@once',
    start_date=datetime(2022,8,1),
    catchup=False
) as dag:
    send_email_notification= EmailOperator(
        task_id="send_test_email",
        to= "christopher.sierra@usach.cl",
        subject="Test email",
        html_content="<h2>this is test email"   
    )
