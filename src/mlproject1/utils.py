import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from mlproject1.logger import logging
from mlproject1.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL Database Started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df = pd.read_sql_query('SELECT * FROM students',mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e, sys)
