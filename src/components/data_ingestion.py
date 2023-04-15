import os
from src.exception import *
from src.logger import *
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

from src.components.data_trasformation import *

#creating dataclass for input[train_path and test_path] which is data_ingestion configuration
@dataclass
class data_ingestion_input:
    train_path:str = os.path.join('artifacts','train.csv') #path for training data
    test_path:str =os.path.join('artifacts','test.csv')#path for training data
    raw_data_path:str =os.path.join('artifacts','raw_data.csv')#backup of raw data

#creating a class for data ingestion
class data_ingestion():
    def __init__(self):
        self.data_ingestion_input = data_ingestion_input() #this varaible will store the train_path,test_path,raw_path in the form of tuple  [calling a data class ]
    
    #intiating data ingestion
    def intitate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            data = pd.read_csv('/home/chakradhar/diamond_price/Notebooks/Data/data_file.csv')#reading the data
            logging.info("data reading is done")
            os.makedirs(os.path.dirname(self.data_ingestion_input.raw_data_path),exist_ok=True)#creating directory for raw_data
            data.to_csv(self.data_ingestion_input.raw_data_path,index=False)#saving the file as csv
            logging.info("Train_test_split started")
            train_data,test_data = train_test_split(data,test_size=0.3,random_state=36)#doing the train_test split for data
            train_data.to_csv(self.data_ingestion_input.train_path,index=False)#saving train_data
            test_data.to_csv(self.data_ingestion_input.test_path,index=False)#saving the test_data
            logging.info("Data ingestion is completed")
            return(self.data_ingestion_input.train_path,self.data_ingestion_input.test_path)
        except Exception as e:
            logging.info("EXception occured at data Ingestion stage")
            raise custom_exception(e,sys)
            logging.info(str(e))
if __name__=="__main__":
    obj = data_ingestion()#creating object for data_ingestion class
    train_data,test_data = obj.intitate_data_ingestion()#call the intitate_data_ingestion method  
    data_trans = data_transformation()
    train_arr,test_arr,_ = data_trans.intiate_data_transformation(train_data,test_data)


