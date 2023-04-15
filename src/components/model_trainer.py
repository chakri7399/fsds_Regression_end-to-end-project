import os
import pandas as pd
import numpy as np
from src.logger import *
from src.exception import *
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from src.utils import save_object
from src.utils import evaluate_model

@dataclass
class model_train_config:
     trained_model_file_path = os.path.join('artifacts','model.pkl')
class model_train:
    def __init__(self):
        self.model_trainer_config = model_train_config()
    def intiate_model_train(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {"linear_regression":LinearRegression(),"ridge":Ridge(),"lasso":Lasso(),"elaticnet":ElasticNet()}
            model_report:dict= evaluate_model(
                X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            save_object(
                 file_path= self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
        except Exception as e:
            logging.info("exception occured at model_training stage")
            raise custom_exception(e,sys)


