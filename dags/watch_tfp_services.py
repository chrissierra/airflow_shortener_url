from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

from datetime import datetime
import requests


def send_email(subject="TFSP: Servicios funcionando adecuadamente", text="Los servicios de tarjetafashionspark están funcionando adecuadamente."):
	return requests.post(
		Variable.get("url_mailgun"),
		auth=("api", Variable.get("api_mailgun")),
		data={"from": Variable.get("from_mailgun"),
			"to": ["Chris <administrador@sister.cl>", "Chris <christopher.sierra@usach.cl>"],
			"subject": subject,
			"text": text})



services_list = ['https://sapim.fppay.com/tfp/app/1.0.0/contents']

def requesting_services():
    for url in services_list:
        requesting_service(url)



def requesting_service(url):
    try:
        apikey = Variable.get('apim_prod_apikey')        
        headers = {
            'Accept': 'application/json',
            'apikey' : f"{apikey}"
        }
        method = 'get'
        req = requests.request(method, url, headers=headers, auth=None)
        if (req.status_code>299):
            raise Exception('Error en servicios')
        return req
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise Exception(e)

def service_watcher():    
    try:
        requesting_services()
        send_email()
    except:
        send_email(subject='TFSP: Error en servicios', text='Los servicios están mostrando errores. ')

        

with DAG(
    dag_id='python_operator',
    description='Fisrt dag using python operator',
    schedule_interval='@once',
    start_date=datetime(2022,8,1)
    ) as dag:
    
    t1 = PythonOperator(
        task_id = 'hello_with_python',
        python_callable = service_watcher
    )
