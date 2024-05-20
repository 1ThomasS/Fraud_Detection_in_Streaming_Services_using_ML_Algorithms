# import json
# import requests

# from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator

# default_args = {
#     'owner': '1_ThomasS',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 5, 15, 22, 00),
#     'email': ['quangvinh432002@gmail.com'],
#     'email_on_failure': False,
#     'email_on_retry': False
# }

# def get_data():
#     res = requests.get('https://randomuser.me/api/')
#     res = res.json()
#     res = res['results'][0]

#     return res

# def format_data(res):
#     data = {}
#     location = res['location']
#     data['first_name'] = res['name']['first']
#     data['last_name'] = res['name']['last']
#     data['gender'] = res['gender']
#     data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
#                       f"{location['city']}, {location['state']}, {location['country']}"
#     data['postcode'] = location['postcode']
#     data['email'] = res['email']
#     data['username'] = res['login']['username']
#     data['dob'] = res['dob']['date']
#     data['registered_date'] = res['registered']['date']
#     data['phone'] = res['phone']
#     data['picture'] = res['picture']['medium']

#     return data

# def stream_data():
#     res = get_data()
#     res = format_data(res)
#     print(json.dumps(res, indent=3))
    

# # dag = DAG(
# #     'user_automation',
# #     default_args=default_args,
# #     schedule_interval='@daily',
# #     catchup=False
# # )

# # streaming_task = PythonOperator(
# #     task_id='stream_data_from_api',
# #     python_callable=stream_data
# # )

# stream_data()


# import json
# import requests

# from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.operators.dummy_operator import DummyOperator
# from airflow.operators.bash_operator import BashOperator


# default_args = {
#     'owner': '1_ThomasS',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 5, 15, 22, 00),
#     'email': ['quangvinh432002@gmail.com'],
#     'email_on_failure': False,
#     'email_on_retry': False
# }

# dag = DAG(
#     dag_id='ryanair_DAG',
#     default_args=default_args,
#     start_date=datetime(2024,5,16),
#     catchup=False,
#     schedule_interval='*/3 * * * *', #every 3 minutes
#     )

# t1 = BashOperator(
#     task_id = 'Bash_task',
#     bash_command = 'python $AIRFLOW_HOME/dags/scripts/RyanAir_ETL.py',
#     dag = dag
#     )
    
# t1
