from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "telco-etl-Copy4-0613111358",
}

dag = DAG(
    "telco-etl-Copy4-0613111358",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.3.0.dev0 pipeline editor using `telco-etl-Copy1.pipeline`.",
    is_paused_upon_creation=False,
)


notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85 = NotebookOp(
    name="Extract_datasource",
    namespace="airflow",
    task_id="Extract_datasource",
    notebook="demo-pipeline/Extract datasource.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="telco-etl-Copy4-0613111358",
    cos_dependencies_archive="Extract datasource-15c8ef03-d6f7-4c41-a682-11676d9b1f85.tar.gz",
    pipeline_outputs=["test/telco-data.csv"],
    pipeline_inputs=[],
    env_vars={
        "DIR_NAME": "test",
        "DIR_FILE_NAME": "telco-data.csv",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    config_file="None",
    dag=dag,
)

notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85.image_pull_policy = "IfNotPresent"


notebook_op_62d9e3e8_69dc_4700_a838_81641d9cd145 = NotebookOp(
    name="transform_Copy1",
    namespace="airflow",
    task_id="transform_Copy1",
    notebook="demo-pipeline/transform-Copy1.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="telco-etl-Copy4-0613111358",
    cos_dependencies_archive="transform-Copy1-62d9e3e8-69dc-4700-a838-81641d9cd145.tar.gz",
    pipeline_outputs=["test/telco-data-encd.csv"],
    pipeline_inputs=["test/telco-data.csv"],
    env_vars={
        "DIR_NAME": "test",
        "DIR_FILE_NAME": "telco-data.csv",
        "MINIO_ACCESS_KEY": "minio",
        "MINIO_SECRET_KEY": "minio123",
        "MINIO_BUCKET": "telco-data-suc",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    config_file="None",
    dag=dag,
)

notebook_op_62d9e3e8_69dc_4700_a838_81641d9cd145.image_pull_policy = "IfNotPresent"

(
    notebook_op_62d9e3e8_69dc_4700_a838_81641d9cd145
    << notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85
)


notebook_op_43bb6c61_2054_4d37_909a_7341c5b497cd = NotebookOp(
    name="load_data_to_hw_Copy1",
    namespace="airflow",
    task_id="load_data_to_hw_Copy1",
    notebook="demo-pipeline/load data to hw-Copy1.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="telco-etl-Copy4-0613111358",
    cos_dependencies_archive="load data to hw-Copy1-43bb6c61-2054-4d37-909a-7341c5b497cd.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["test/telco-data-encd.csv", "test/telco-data.csv"],
    env_vars={
        "HSFS_FG_NAME": "telco_fg",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    config_file="None",
    dag=dag,
)

notebook_op_43bb6c61_2054_4d37_909a_7341c5b497cd.image_pull_policy = "IfNotPresent"

(
    notebook_op_43bb6c61_2054_4d37_909a_7341c5b497cd
    << notebook_op_62d9e3e8_69dc_4700_a838_81641d9cd145
)
