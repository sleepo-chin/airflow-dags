from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "ETL-PIPELINE-0614075022",
}

dag = DAG(
    "ETL-PIPELINE-0614075022",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.3.0.dev0 pipeline editor using `telco-etl.pipeline`.",
    is_paused_upon_creation=False,
)


notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85 = NotebookOp(
    name="Extract_datasource",
    namespace="airflow",
    task_id="Extract_datasource",
    notebook="demo-pipeline/Extract datasource.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="ETL-PIPELINE-0614075022",
    cos_dependencies_archive="Extract datasource-15c8ef03-d6f7-4c41-a682-11676d9b1f85.tar.gz",
    pipeline_outputs=["test/telco-data2.csv"],
    pipeline_inputs=[],
    env_vars={
        "DIR_NAME": "test",
        "DIR_FILE_NAME": "telco-data2.csv",
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


notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572 = NotebookOp(
    name="transform",
    namespace="airflow",
    task_id="transform",
    notebook="demo-pipeline/transform.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="ETL-PIPELINE-0614075022",
    cos_dependencies_archive="transform-9e3fe02a-9694-429d-9633-cc62bdf4c572.tar.gz",
    pipeline_outputs=["test/telco-data-transform.csv"],
    pipeline_inputs=["test/telco-data2.csv"],
    env_vars={
        "MINIO_ACCESS_KEY": "minio",
        "MINIO_SECRET_KEY": "minio123",
        "MINIO_BUCKET": "data",
        "DIR_FILE_NAME": "telco-data-transform.csv",
        "DIR_NAME": "test",
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

notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572.image_pull_policy = "IfNotPresent"

(
    notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572
    << notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85
)


notebook_op_5952a542_10fa_4fc0_8bc7_7cc6510e6822 = NotebookOp(
    name="load_data_to_hw_Copy1",
    namespace="airflow",
    task_id="load_data_to_hw_Copy1",
    notebook="demo-pipeline/load data to hw-Copy1.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="ETL-PIPELINE-0614075022",
    cos_dependencies_archive="load data to hw-Copy1-5952a542-10fa-4fc0-8bc7-7cc6510e6822.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["test/telco-data2.csv", "test/telco-data-transform.csv"],
    env_vars={
        "HSFS_FG_NAME": "telco_data",
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

notebook_op_5952a542_10fa_4fc0_8bc7_7cc6510e6822.image_pull_policy = "IfNotPresent"

(
    notebook_op_5952a542_10fa_4fc0_8bc7_7cc6510e6822
    << notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572
)
