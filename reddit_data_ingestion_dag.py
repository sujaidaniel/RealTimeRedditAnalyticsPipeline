import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Include project directories in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

# Default configuration for the DAG
default_args = {
    'owner': 'Daniel Pallapati',
    'start_date': datetime(2024, 10, 25),
}

# Generate a timestamp-based file suffix
current_date_suffix = datetime.now().strftime("%Y%m%d")

# Define the DAG
dag = DAG(
    dag_id='reddit_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline'],
)

# Task to extract data from Reddit
extract_reddit_data = PythonOperator(
    task_id='extract_reddit_data',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_data_{current_date_suffix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100,
    },
    dag=dag,
)

# Task to upload extracted data to Amazon S3
upload_data_to_s3 = PythonOperator(
    task_id='upload_data_to_s3',
    python_callable=upload_s3_pipeline,
    dag=dag,
)

# Define task dependencies
extract_reddit_data >> upload_data_to_s3
