import os
import json
import sys
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
encoded_password = quote_plus(password)
cluster_url = os.getenv("MONGO_CLUSTER")
database_name = os.getenv("DATABASE_NAME")

mongo_uri = f"mongodb+srv://{username}:{encoded_password}@{cluster_url}/?retryWrites=true&w=majority"
print(mongo_uri)

import certifi
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
print("Connected successfully!")
import pandas as pd
import numpy as np
import pymongo
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.my_logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop = True,inplace = True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(mongo_uri)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
if __name__ == "__main__":
    FILE_PATH = r"C:\Users\91949\Desktop\Network Security Project\data_set\phisingData.csv"
    DATABASE = "VARUN"
    collection = "NetworkSecurityData"
    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json_convertor(file_path = FILE_PATH)
    ##print(records)
    no_of_records = network_obj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)
    
         
        
    
