End TO End Data Science Project

import dagshub
dagshub.init(repo_owner='thespv', repo_name='MLProject1', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
