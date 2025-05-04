import os
import time
import mlflow

def eval(param_1, param_2):
    return (param_1 + param_2)/2


def mani():

    with mlflow.start_run as run:
        mlflow.set_tag('version', '1.0.0')
        mlflow.log_param('param_1', param_1)
        mlflow.log_param('param_2', param_2)
        mlflow.log_metric('mean', eval(param_1=param_1, param_2=param_2))
        


    
