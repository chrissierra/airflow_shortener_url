from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth
import os



from smtplib import SMTP

from dotenv import load_dotenv

load_dotenv()



def send_simple_message2():
    # Creating the respective object along with the gmail login and port number
    smtp_port = SMTP("smtp.gmail.com", 587)

    # Establishing a connection to the SMTP server with Transport Layer Security (TLS) mode
    smtp_port.ehlo()

    # Informing the client to establish a secure connection, either to a TLS or SSL
    smtp_port.starttls()
    
    password = Variable.get("email_pass")
    print('Password: ' + str(password))
    # Logging into your account
    smtp_port.login('shortener.fshp@gmail.com' , password)

    # Creating the contents of the email
    subject = "Hello"
    body = "Email Automation Project!"
    desde = "services@fshp.cl"
    # Usando body?
    message = """\
    Subject: Hi there

    This message is sent from Python.
    """
    # Creating the list of email addresses
    address_list = ['christopher.sierra@usach.cl', 'administrador@sister.cl']
    smtp_port.sendmail('shortener.fshp@gmail.com' , address_list, message)
    print("Email Sent")
    smtp_port.quit()


def send_email(subject="TFSP: Servicios funcionando adecuadamente", text="Los servicios de tarjetafashionspark están funcionando adecuadamente."):
	return requests.post(
		Variable.get("url_mailgun"),
		auth=("api", Variable.get("api_mailgun")),
		data={"from": Variable.get("from_mailgun"),
			"to": "Chris <administrador@sister.cl>",
			"subject": subject,
			"text": text})



def requesting_services():
    try:
        apikey = Variable.get('apim_prod_apikey')
        url = 'https://sapim.fppay.com/tfp/app/1.0.0/contents1'
        headers = {'Accept': 'application/json'}
        
        headers = {
            'Accept': 'application/json',
            'apikey' : f"{apikey}"
        }
        method = 'get'
        req = requests.request(method, url, headers=headers, auth=None)
        print(req.status_code)
        print(req)
        if (req.status_code>299):
            raise Exception('error en servicios')
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
