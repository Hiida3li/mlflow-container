import mlflow

try:
    exp_id = mlflow.create_experiment('test')
    print(exp_id)
except:
    pass

    
exp = mlflow.set_experiment('test_something')

with mlflow.start_run() as run:
    