from sensor.entity.config_entity import TrainingPipelineConfig , DataIngestionConfig, DataValidationConfig
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.entity.artifacts_entity import DataIngestionArtifact,DataValidationArtifact
from sensor.component.data_ingestion import DataIngestion 
from sensor.component.data_validation import DataValidation


class TrainPipeline:
    
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()
        #self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        #self.training_pipeline_config=training_pipeline_config
           
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Data Ingestion Started")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()            
            logging.info(f"Data Ingestion Completed and artifacts: {data_ingestion_artifacts}")
            return data_ingestion_artifacts
        
        except Exception as e:
            raise SensorException(e,sys)
               
    def start_data_validaton(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config = data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except  Exception as e:
            raise  SensorException(e,sys)
               
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
               
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
               
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
               
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
          
    # This function define the sequence   
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validaton(data_ingestion_artifact=data_ingestion_artifact)
            pass
        except Exception as e:
            raise SensorException(e,sys)
        