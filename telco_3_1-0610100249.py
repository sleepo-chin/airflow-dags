from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "telco_3_1-0610100249",
}

dag = DAG(
    "telco_3_1-0610100249",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.3.0.dev0 pipeline editor using `untitled.pipeline`.",
    is_paused_upon_creation=False,
)


notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85 = NotebookOp(
    name="Extract_datasource",
    namespace="airflow",
    task_id="Extract_datasource",
    notebook="Airflow/Extract datasource.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="telco_3_1-0610100249",
    cos_dependencies_archive="Extract datasource-15c8ef03-d6f7-4c41-a682-11676d9b1f85.tar.gz",
    pipeline_outputs=["test_2/telco_data.csv"],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "DIR_NAME": "test_2",
        "DIR_FILE_NAME": "telco_data.csv",
    },
    config_file="None",
    dag=dag,
)


notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572 = NotebookOp(
    name="transform",
    namespace="airflow",
    task_id="transform",
    notebook="Airflow/transform.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="telco_3_1-0610100249",
    cos_dependencies_archive="transform-9e3fe02a-9694-429d-9633-cc62bdf4c572.tar.gz",
    pipeline_outputs=["test_2/telco_data.csv"],
    pipeline_inputs=["test_2/telco_data.csv"],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MINIO_ACCESS_KEY": "minio",
        "MINIO_SECRET_KEY": "minio123",
        "MINIO_BUCKET": "data",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572
    << notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85
)
