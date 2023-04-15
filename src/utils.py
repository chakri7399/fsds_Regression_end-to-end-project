import os
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from src.exception import *
from src.logger import *
import pickle
# from src.components.model_trainer import * 

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)#making dirname
        os.makedirs(dir_path,exist_ok=True)#creating directory
        with open(file_path,"wb") as file_obj:#pening the file
            pickle.dump(obj,file_obj)#dmuping as pickle file
    except Exception as e:
        logging.info("exception occured at utils file")
        raise custom_exception(e,sys)

        
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise custom_exception(e,sys)

