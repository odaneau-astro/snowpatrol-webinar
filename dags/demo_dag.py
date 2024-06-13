
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.utils.dates import days_ago

snowflake_conn_id = "snowflake_conn"

snowflake_doc_md = """# SnowPatrol Webinar Demo"""


with DAG(
    dag_id="snowpatrol_webinar_demo",
    schedule=None,
    start_date=days_ago(1),
    doc_md=snowflake_doc_md,
):
    snowflake = SQLExecuteQueryOperator(
        doc_md="This showcases the SnowPatrol Plugin without returning any data.",
        task_id="snowpatrol_webinar_demo",
        conn_id=snowflake_conn_id,
        sql="SELECT TOP 1 'THIS QUERY COMES FROM THE SNOWPATROL WEBINAR DEMO DAG' FROM SNOWFLAKE.INFORMATION_SCHEMA.TABLES;",
    )

    snowflake
