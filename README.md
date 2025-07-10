import dagshub
dagshub.init(repo_owner='thespv', repo_name='MLProject1', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)




Here, distutils package is creating problem as it is no longer available in python 3.12+,
So we have to downgrade setuptools as we are not going to downgrade Python,
so, we have to try this in terminal -->  ( pip install setuptools==65.5.0 ) for working properly