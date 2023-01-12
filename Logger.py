import logging
from datetime import datetime
import os


class CustomLogger:
    def __init__(self, name: str) -> None:
        self.logger = logging.Logger(name)

        consoleLog = logging.StreamHandler()
        if not os.path.exists("log"):
            os.makedirs("log")

        now = datetime.now()
        fileName = f'log_{str(now.strftime("%d-%m-%Y %H-%M-%S"))}.log'
        errorLog = logging.FileHandler("log/error_"+fileName)
        allLog = logging.FileHandler("log/all_"+fileName)
        consoleLog.setLevel(level=logging.INFO)
        errorLog.setLevel(logging.ERROR)
        allLog.setLevel(logging.NOTSET)

        format = logging.Formatter('%(asctime)s - %(name)s :- %(levelname)s ---> %(message)s',
                                   datefmt='%d-%b-%y %H:%M:%S')
        consoleLog.setFormatter(format)
        errorLog.setFormatter(format)
        allLog.setFormatter(format)

        self.logger.addHandler(consoleLog)
        self.logger.addHandler(errorLog)
        self.logger.addHandler(allLog)
