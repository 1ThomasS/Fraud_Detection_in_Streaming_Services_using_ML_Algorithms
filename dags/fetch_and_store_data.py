from datetime import datetime
import requests
import psycopg2
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    'fetch_and_store_data',
    default_args=default_args,
    description='Fetch data from API and store in PostgreSQL',
    catchup=False,
    schedule_interval='*/3 * * * *',
    
)

def fetch_data():
    """Fetch data from the API"""
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    data = response.json()
    return data['results'][0]


def store_data(**kwargs):
    ti = kwargs['ti']
    user_data = ti.xcom_pull(task_ids='fetch_data')

    mysql_hook = MySqlHook(mysql_conn_id='mysql_fraud_detection')
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()

    insert_query = """INSERT INTO users (name, email, location) VALUES (%s, %s, %s);"""
    cursor.execute(insert_query, (user_data['name']['first'], user_data['email'], user_data['location']['city']))
    connection.commit()
    cursor.close()
    connection.close()


fetch_data = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag,
)


store_data = PythonOperator(
    task_id='store_data',
    python_callable=store_data,
    provide_context=True,
    dag=dag,
)


fetch_data >> store_data
