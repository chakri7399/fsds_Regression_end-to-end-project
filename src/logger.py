import logging 
import os
from src.exception import *
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #creating log file with month-day-year-hour-minute format[sample logfile nam will be : 08_48_04_02_2012.log]
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
#for checking exception and raising the custom_excetion
if __name__ =="__main__":
    try:
        a = 4/0
    except Exception as e:
        raise custom_exception(e,sys)