from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
default_args={
    'owner':'pravallika',
    'start_date':datetime(2024,4,10,15,38)
}
def get_data():
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res
def format_data(res):
    data={}
    data['firstname']=res['name']['first']
    data['lastname']=res['name']['last']
    data['gender']=res['gender']
    data['address'] = f"{res['location']['street']['number']} {res['location']['street']['name']} {res['location']['city']} {res['location']['state']} {res['location']['country']}"
    data['postcode']=res['location']['postcode']
    data['email']=res['email']
    data['username']=res['login']['username']
    data['dob']=res['dob']
    data['registered_date']=res['registered']['date']
    data['phone']=res['phone']
    data['picture']=res['picture']['medium']
    return data


def stream_data():
    import json
    import json
    res = get_data()
    res = format_data(res)
    print(json.dumps(res, indent=3))

    # print(json.dumps(res,indent=3))
# with DAG('user_automation',
#          default_args=default_args,
#          schedule='@daily',
#          catchup=False) as dag:
#     streaming_task=PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )
stream_data()