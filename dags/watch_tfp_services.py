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



def send_simple_message():
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
    message =  """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """
    # Creating the list of email addresses
    address_list = ['christopher.sierra@usach.cl', 'administrador@sister.cl']
    smtp_port.sendmail('shortener.fshp@gmail.com' , address_list, message)
    print("Email Sent")
    smtp_port.quit()








def print_hello():
    send_simple_message()
    print('Hello people from python funtion')
    apikey = 'eyJ4NXQiOiJOVGRtWmpNNFpEazNOalkwWXpjNU1tWm1PRGd3TVRFM01XWXdOREU1TVdSbFpEZzROemM0WkE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJ3ZWItdGZzcCIsImlkIjo2LCJ1dWlkIjoiY2NkNzc0YmMtYzkzMC00NmYwLThlNDctZDI5NTZkY2NiYmRkIn0sImlzcyI6Imh0dHBzOlwvXC9hcGltLnByb2QuZ3J1cG9jaGllbi5sb2NhbDo5NDQzXC9vYXV0aDJcL3Rva2VuIiwidGllckluZm8iOnsiR29sZCI6eyJ0aWVyUXVvdGFUeXBlIjoicmVxdWVzdENvdW50IiwiZ3JhcGhRTE1heENvbXBsZXhpdHkiOjAsImdyYXBoUUxNYXhEZXB0aCI6MCwic3RvcE9uUXVvdGFSZWFjaCI6dHJ1ZSwic3Bpa2VBcnJlc3RMaW1pdCI6MCwic3Bpa2VBcnJlc3RVbml0IjpudWxsfSwiVW5saW1pdGVkIjp7InRpZXJRdW90YVR5cGUiOiJyZXF1ZXN0Q291bnQiLCJncmFwaFFMTWF4Q29tcGxleGl0eSI6MCwiZ3JhcGhRTE1heERlcHRoIjowLCJzdG9wT25RdW90YVJlYWNoIjp0cnVlLCJzcGlrZUFycmVzdExpbWl0IjowLCJzcGlrZUFycmVzdFVuaXQiOm51bGx9fSwia2V5dHlwZSI6IlBST0RVQ1RJT04iLCJwZXJtaXR0ZWRSZWZlcmVyIjoiIiwic3Vic2NyaWJlZEFQSXMiOlt7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiRlAtTVctU0VSVklDRVMiLCJjb250ZXh0IjoiXC9mcFwvbXdcLzEuMC4xIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMS4wLjEiLCJzdWJzY3JpcHRpb25UaWVyIjoiR29sZCJ9LHsic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJnZXQtZG9jdW1lbnRzIiwiY29udGV4dCI6IlwvYXBpLXZpZXdkb2NcL2dldC1kb2N1bWVudHNcLzAuMC4xIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMC4wLjEiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn0seyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6ImFwaS12aWV3ZG9jIiwiY29udGV4dCI6IlwvYXBpLXZpZXdkb2NcLzEiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIxIiwic3Vic2NyaXB0aW9uVGllciI6IlVubGltaXRlZCJ9LHsic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJURlAtV0VCLVNFUlZJQ0VTIiwiY29udGV4dCI6IlwvdGZwXC93ZWJcLzEuMC4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMS4wLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn0seyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlRGUC1BUFAtU0VSVklDRVMiLCJjb250ZXh0IjoiXC90ZnBcL2FwcFwvMS4wLjAiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIxLjAuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJHb2xkIn0seyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlRGUC1BUFAtQkFTSUMtU0VSVklDRVMiLCJjb250ZXh0IjoiXC90ZnBcL2FwcFwvYmFzaWNcLzEuMC4xIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMS4wLjEiLCJzdWJzY3JpcHRpb25UaWVyIjoiR29sZCJ9LHsic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJURlAtQVBQLVNFUlZJQ0VTLUNNUyIsImNvbnRleHQiOiJcL3RmcFwvYXBwXC9jbXNcLzEuMC4xIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMS4wLjEiLCJzdWJzY3JpcHRpb25UaWVyIjoiR29sZCJ9XSwidG9rZW5fdHlwZSI6ImFwaUtleSIsInBlcm1pdHRlZElQIjoiIiwiaWF0IjoxNjY2NzEzMTgxLCJqdGkiOiJiOGI3OTczYS1jMTA0LTQ4YjQtOTVkMy00M2MxZWY4ZTVmYzkifQ==.pxo-S2dU3qhKoJMrZrtaNE27G5pLNZKVURVyun0lyQ9JA18jNHwt6bpnzXy1DVhB7clwc1gttkeJbyca0LzX78kkDAECqW028rypBbnZAp8ZN7UBoamlZGlh3cJfTjhtREJCOJ-Xv9e35uP2zZFlDaya2l7LGbha_sGFn2bf9VQTjasi9-Hwz80tl3Vuf8oaTyIWugTGRbJgQM0h1d8PWQFYuyjL5bIhfeNRtS4xtlTwjJT0qm83k-JUgYCj_spmKQn_Fl2PqAmoi2wgYhO6khXPMwxn2-VJuUX_ecr3yBUGm5soUQ-3RZETfCbtMUiaNcKl0xntVNYr9F-z501F4A=='
    url = 'https://sapim.fppay.com/tfp/app/1.0.0/contents'
    headers = {'Accept': 'application/json'}
    
    headers = {
        'Accept': 'application/json',
        'apikey' : f"{apikey}"
    }
    method = 'get'
    req = requests.request(method, url, headers=headers, auth=None)
    print(req.status_code)

with DAG(
    dag_id='python_operator',
    description='Fisrt dag using python operator',
    schedule_interval='@once',
    start_date=datetime(2022,8,1)
    ) as dag:
    
    t1 = PythonOperator(
        task_id = 'hello_with_python',
        python_callable = print_hello
    )
