import logging
from datetime import datetime


class CustomLogger:
    def __init__(self, name: str) -> None:
        self.logger = logging.Logger(name)

        c_handler = logging.StreamHandler()

        now = datetime.now()
        f_handler = logging.FileHandler("log_" + str(now.strftime("%d-%m-%Y %H-%M-%S")+".log"))
        c_handler.setLevel(level=logging.INFO)
        f_handler.setLevel(logging.ERROR)

        format = logging.Formatter('%(asctime)s - %(name)s :- %(levelname)s ---> %(message)s',
                                   datefmt='%d-%b-%y %H:%M:%S')
        c_handler.setFormatter(format)
        f_handler.setFormatter(format)

        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)
