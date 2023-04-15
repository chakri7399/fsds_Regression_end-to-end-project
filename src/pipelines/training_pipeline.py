import os
from src.exception import *
from src.logger import *
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

from src.components.data_ingestion import *
from src.components.data_trasformation import *
from src.components.model_trainer import *

#running dataingestion and 
if __name__=="__main__":
    obj = data_ingestion()#creating object for data_ingestion class
    train_data,test_data = obj.intitate_data_ingestion()#call the intitate_data_ingestion method  
    data_trans = data_transformation()
    train_arr,test_arr,_ = data_trans.intiate_data_transformation(train_data,test_data)
    model_trainer= model_train()
    model_trainer.intiate_model_train(train_arr,test_arr)
