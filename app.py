import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from mlproject1.logger import logging
from mlproject1.exception import CustomException
from mlproject1.components.data_ingestion import DataIngestion
from mlproject1.components.data_ingestion import DataIngestionConfig
from mlproject1.components.data_transformation import DataTransformationConfig, Datatransformation
from mlproject1.components.model_trainer import ModelTrainerConfig, ModelTrainer



if __name__ == "__main__":
     logging.info("The Execution has started")

     try:
         data_ingestion = DataIngestion()
         train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

        # Data Transformation
         data_transformation = Datatransformation()
         train_arr,test_arr,processor_path = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        # Model Training
         model_trainer = ModelTrainer()
         print(model_trainer.initiate_model_trainer(train_arr,test_arr))

     except Exception as e:
          logging.info("Custom Exception")
          raise CustomException(e, sys)