from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifacts_entity import DataIngestionArtifact
import os,sys
from pandas import DataFrame
from sensor.data_access.sesnor_data import SensorData
from sklearn.model_selection import train_test_split



class DataIngestion:
    
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:            
           self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
    
    def export_data_into_feature_store(self):
        """
        This function will export mongodb collection(car) record as dataframe into feature_store
        
        """
        try:
            logging.info("Starting exporting data from mongodb to feature store")
            sensor_data=SensorData()
            dataframe=sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            print(dataframe.shape)
            
            #Till here we get the dataframe now  next we need to create feature_store folder to store data in sensor.csv file
            
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            
            # create feature store folder. 
            # feature_store_file path is : artifact\\11_15_2022_16_55_55\\data_ingestion\\feature_store\\sensor.csv but we need
            # only the directory from it excluding the filename for that
         
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            
            #Till here dataframe store into artifact\\11_15_2022_16_55_55\\data_ingestion\\feature_store\\sensor.csv
            # So we completed till export data to feature store
            return dataframe
         
        except Exception as e:
            raise SensorException(e,sys)
        
        
    def split_data_as_train_test(self,dataframe:DataFrame):
        """
        This function will split the feature_store dataset into train and test file
        
        """
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)

            logging.info("Performed train test split on the dataframe")

            logging.info("Exited split_data_as_train_test method of Data_Ingestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)

            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise SensorData(e,sys)
        
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            dataframe=self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            data_ingestion_artifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                  test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    
    
            
        