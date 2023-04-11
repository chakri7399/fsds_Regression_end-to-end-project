import sys
from src.logger import logging
def error_message_details(error,error_detail:sys):
    type,value,exc_tb = sys.exc_info()#it will give information about error in the form of list where 3 paramter is importnat[traceback]
    file_name = exc_tb.tb_frame.f_code.co_filename#getting file name where error is occured
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
class custom_exception(Exception): #inheriting the exception class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #getting the constructor of Exceptin class and passing error_message as parameter
        self.error_message = error_message_details(error_message,error_detail)#calling the error_message_details method to get error_message
    def __str__(self):
        return self.error_message
