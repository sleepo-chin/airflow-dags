from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "test_telco_data_1-0610060846",
}

dag = DAG(
    "test_telco_data_1-0610060846",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.3.0.dev0 pipeline editor using `untitled.pipeline`.",
    is_paused_upon_creation=False,
)


notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85 = NotebookOp(
    name="Extract_datasource",
    namespace="default",
    task_id="Extract_datasource",
    notebook="Airflow/Extract datasource.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="test_telco_data_1-0610060846",
    cos_dependencies_archive="Extract datasource-15c8ef03-d6f7-4c41-a682-11676d9b1f85.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="Pandas 1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "DIR_NAME": "test_2",
        "DIR_FILE_NAME": "telco-data.csv",
    },
    config_file="None",
    dag=dag,
)


notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572 = NotebookOp(
    name="transform",
    namespace="default",
    task_id="transform",
    notebook="Airflow/transform.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="test_telco_data_1-0610060846",
    cos_dependencies_archive="transform-9e3fe02a-9694-429d-9633-cc62bdf4c572.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="Pandas 1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572
    << notebook_op_15c8ef03_d6f7_4c41_a682_11676d9b1f85
)


notebook_op_225cd238_97e0_4418_8183_734355388b5d = NotebookOp(
    name="load_data_to_hw",
    namespace="default",
    task_id="load_data_to_hw",
    notebook="Airflow/load data to hw.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="test_telco_data_1-0610060846",
    cos_dependencies_archive="load data to hw-225cd238-97e0-4418-8183-734355388b5d.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="Pandas 1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_225cd238_97e0_4418_8183_734355388b5d
    << notebook_op_9e3fe02a_9694_429d_9633_cc62bdf4c572
)
