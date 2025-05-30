import mlflow

try:
    exp_id = mlflow.create_experiment('test')
    print(exp_id)
except:
    pass

    
exp = mlflow.set_experiment('test_something')

with mlflow.start_run() as run:
    pass

mlflow.log_param('k1', 10)
mlflow.log_params({'param1': 2, 'param2': 4})
mlflow.log_metric('metric1', 1)
mlflow.log_metrics({'metric2': 2, 'metric3': 4})
