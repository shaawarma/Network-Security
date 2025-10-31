import sys
import os
import pymongo
from urllib.parse import quote_plus

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.my_logging.logger import logging
from NetworkSecurity.pipeline.training_pipeline import  TrainingPipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd
from NetworkSecurity.utils.main_utils.utils import load_object

username = quote_plus(os.getenv("MONGO_USERNAME", ""))
password = quote_plus(os.getenv("MONGO_PASSWORD", ""))
encoded_password = quote_plus(password)
cluster_url = os.getenv("MONGO_CLUSTER")
database_name = os.getenv("DATABASE_NAME")

mongo_uri = f"mongodb+srv://{username}:{encoded_password}@{cluster_url}/?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_uri, tlsCAFile=ca)

from NetworkSecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from NetworkSecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
if __name__ == "__main__":
    app_run(app,host = "localhost",port = 8000)