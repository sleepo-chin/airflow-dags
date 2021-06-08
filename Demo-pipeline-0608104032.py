from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "Demo-pipeline-0608104032",
}

dag = DAG(
    "Demo-pipeline-0608104032",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.3.0.dev0 pipeline editor using `Demo-pipeline.pipeline`.",
    is_paused_upon_creation=False,
)


notebook_op_5fbc29fe_a049_48d7_9ba6_6161f32ac928 = NotebookOp(
    name="load_data",
    namespace="default",
    task_id="load_data",
    notebook="demo-airflow/elyra-pipeline/load_data.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="Demo-pipeline-0608104032",
    cos_dependencies_archive="load_data-5fbc29fe-a049-48d7-9ba6-6161f32ac928.tar.gz",
    pipeline_outputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
    },
    config_file="None",
    dag=dag,
)

notebook_op_5fbc29fe_a049_48d7_9ba6_6161f32ac928.image_pull_policy = "IfNotPresent"


notebook_op_1c6df6b6_efb0_4e96_b534_a9e619a99746 = NotebookOp(
    name="Part_1___Data_Cleaning",
    namespace="default",
    task_id="Part_1___Data_Cleaning",
    notebook="demo-airflow/elyra-pipeline/Part 1 - Data Cleaning.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="Demo-pipeline-0608104032",
    cos_dependencies_archive="Part 1 - Data Cleaning-1c6df6b6-efb0-4e96-b534-a9e619a99746.tar.gz",
    pipeline_outputs=["data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv"],
    pipeline_inputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_1c6df6b6_efb0_4e96_b534_a9e619a99746.image_pull_policy = "IfNotPresent"

(
    notebook_op_1c6df6b6_efb0_4e96_b534_a9e619a99746
    << notebook_op_5fbc29fe_a049_48d7_9ba6_6161f32ac928
)


notebook_op_10444450_7c59_4686_973e_548b18815903 = NotebookOp(
    name="Part_2___Data_Analysis",
    namespace="default",
    task_id="Part_2___Data_Analysis",
    notebook="demo-airflow/elyra-pipeline/Part 2 - Data Analysis.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="Demo-pipeline-0608104032",
    cos_dependencies_archive="Part 2 - Data Analysis-10444450-7c59-4686-973e-548b18815903.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[
        "data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv",
        "data/noaa-weather-data-jfk-airport/jfk_weather.csv",
    ],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_10444450_7c59_4686_973e_548b18815903.image_pull_policy = "IfNotPresent"

(
    notebook_op_10444450_7c59_4686_973e_548b18815903
    << notebook_op_1c6df6b6_efb0_4e96_b534_a9e619a99746
)


notebook_op_7dea35cd_22dd_4842_ad0b_e188e15f3aa6 = NotebookOp(
    name="Part_3___Time_Series_Forecasting",
    namespace="default",
    task_id="Part_3___Time_Series_Forecasting",
    notebook="demo-airflow/elyra-pipeline/Part 3 - Time Series Forecasting.ipynb",
    cos_endpoint="http://minio-kubeflow.apps.ocp.ikp.com/",
    cos_bucket="test",
    cos_directory="Demo-pipeline-0608104032",
    cos_dependencies_archive="Part 3 - Time Series Forecasting-7dea35cd-22dd-4842-ad0b-e188e15f3aa6.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[
        "data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv",
        "data/noaa-weather-data-jfk-airport/jfk_weather.csv",
    ],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_7dea35cd_22dd_4842_ad0b_e188e15f3aa6.image_pull_policy = "IfNotPresent"

(
    notebook_op_7dea35cd_22dd_4842_ad0b_e188e15f3aa6
    << notebook_op_1c6df6b6_efb0_4e96_b534_a9e619a99746
)
