import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL")


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:

            self.records = records
            self.database = database
            self.collection  =  collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == "__main__":
    data_path = "Networksecurity_data\Dataset Phising Website.csv\Dataset Phising Website.csv"
    DATABASE = "AVINASH"
    COLLECTION = 'NetworkSecurityData'
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=data_path)
    no_of_records = networkobj.insert_data_to_mongodb(records,database=DATABASE,collection=COLLECTION)
    print(no_of_records)
