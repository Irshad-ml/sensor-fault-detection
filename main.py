from sensor.exception  import SensorException
import os,sys
from sensor.logger import logging


def test_exception():
    try:
        logging.info("This message is : We are dividing 1 by 0")
        x = 1/0
    except Exception as e:
        raise SensorException(e,sys)
    

if __name__=='__main__':
    try:
        test_exception()
    except Exception as e:
        print(e)
    
