import airflow

from airflow import DAG
from airflow.contrib.operators.oozie_subdag_operator import OozieSubDagOperator


args = {
    'owner': 'airflow',
    'email': ['airflow@example.com'],
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='example_oozie_subdag_operator',
    schedule_interval='@daily')

subdag_task = OozieSubDagOperator(
    task_id='subdag_task',
    config='asd',
    dag=dag)
