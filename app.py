import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from mlproject1.logger import logging
from mlproject1.exception import CustomException
from mlproject1.components.data_ingestion import DataIngestion
from mlproject1.components.data_ingestion import DataIngestionConfig
from mlproject1.components.data_transformation import DataTransformationConfig, Datatransformation



if __name__ == "__main__":
     logging.info("The Execution has started")

     try:
         data_ingestion = DataIngestion()
         train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

         data_transformation = Datatransformation()
         data_transformation.initiate_data_transformation(train_data_path,test_data_path)

     except Exception as e:
          logging.info("Custom Exception")
          raise CustomException(e, sys)