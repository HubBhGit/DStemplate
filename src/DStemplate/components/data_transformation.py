import os
from src.DStemplate import logger
from sklearn.model_selection import train_test_split
from src.DStemplate.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    ##Note:We can add different data transformation techniques such as Scaler, PCA etc
    
    def train_test_splitting(self):
        data=pd.raed_csv(self.config.data_path)
        
        # Split the data into training and test sets
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
        
        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
        