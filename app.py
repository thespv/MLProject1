import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from mlproject1.logger import logging
from mlproject1.exception import CustomException
from mlproject1.components.data_ingestion import DataIngestion
from mlproject1.components.data_ingestion import DataIngestionConfig



if __name__ == "__main__":
     logging.info("The Execution has started")

     try:
         data_ingestion = DataIngestion()
         data_ingestion.initiate_data_ingestion()

     except Exception as e:
          logging.info("Custom Exception")
          raise CustomException(e, sys)