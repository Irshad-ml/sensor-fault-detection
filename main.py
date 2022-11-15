from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception  import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline



    

if __name__=='__main__':
    train_pipeline=TrainPipeline()
    #print(train_pipeline.data_ingestion_config.__dict__)
    train_pipeline.run_pipeline()
    


    
