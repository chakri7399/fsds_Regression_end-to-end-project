#stepl1: importing all necessary libraries
import sys
import pandas as pd
import numpy as np
from src.exception import * #importing exception module
from src.logger import * #importing logging module
from sklearn.preprocessing import OrdinalEncoder # for hadniling categorical_features
from sklearn.pipeline import Pipeline #for pipeline
from sklearn.impute import SimpleImputer # for handiling missing values
from sklearn.preprocessing import StandardScaler # for feature scaling
from sklearn.compose import ColumnTransformer #for combining numerical and categorical pipelines
from dataclasses import dataclass
import os
from src.utils import save_object
 #for creating pickle file

#step2 : configuration of output file path using dataclass
@dataclass
class data_trasnformation_config:
    data_trans_path = os.path.join('artifacts','preprocessor.pkl') # stroing the ouput in a preprocssor.pkl file

#step3: intializing data_transformation
class data_transformation:
    def __init__(self):
        self.data_trans_config = data_trasnformation_config() #storing the variables of dataclass
    def get_data_trans(self):
        try:
            logging.info("Data transformation has started")
            
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            logging.info('Pipeline Initiated')
            
            #this is the numerical pipeline where we will perfrom simple imputer and standard scaling
            numerical_pipeline = Pipeline( steps = [('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())])
            
            #this is the categorical pipeline where we will perfrom simple imputer,ordinal encoding and standard scaling
            categorical_pipeline = Pipeline(steps = [('imputer',SimpleImputer(strategy="most_frequent")),('Encoding',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),('scaler',StandardScaler())])
            
            #we are combining the numerical and categorical pipelines
            preprocessor = ColumnTransformer([('num_pipeline',numerical_pipeline,numerical_cols),('cat_pipeline',categorical_pipeline,categorical_cols)])
            
            return preprocessor
            logging.info("Pipeline Completed")
        
        except Exception as e:
            logging.info("exception occured at Data_transformation step")
            raise custom_exception(e,sys)
            logging.info(str(e))
    
    def intiate_data_transformation(self,train_path,test_path):
            try:
                train_data = pd.read_csv(train_path)#reading the training data file
                test_data = pd.read_csv(test_path) # reading the test data file
                logging.info(f'Training data is {train_data.head()}')
                logging.info(f'Test data is {test_data.head()}')
                logging.info('Obtaining preprocessing object')
                preprocessing_obj = self.get_data_trans()#creating preprocessing object
                
                #getting input and target features for train and test data 
                target_column = ['price'] # setting target column
                drop_columns = ['id','price'] # setting to get input features
                input_train_data = train_data.drop(drop_columns,axis=1)#input features for train data
                target_train_data = train_data[target_column]#target column for train data 
                input_test_data = test_data.drop(drop_columns,axis=1)#input features for test_data
                target_test_data = test_data[target_column] # target column for test data

                #applying fit_transform for input_train_data and transfroming the input_test_data using the preprocessor object
                input_train_data_arr = preprocessing_obj.fit_transform(input_train_data)
                input_test_data_arr = preprocessing_obj.transform(input_test_data)
                
                #concatenating the input features and target features along second axis
                train_data_arr = np.c_[input_train_data_arr,np.array(target_train_data)]
                test_data_arr = np.c_[input_test_data_arr,np.array(target_test_data)]
                
                #saving the picke file using save_object function in utils.py
                
                save_object(file_path = self.data_trans_config.data_trans_path,obj=preprocessing_obj) # first parameter should be object which we created for dataclass and second one is preprcoessing object
                logging.info("pickle file saved")
                return (train_data_arr,test_data_arr,self.data_trans_config.data_trans_path)
            
            except Exception as e:
                logging.info("exception occured at data_transformation intiation step")
                raise custom_exception(e,sys)
