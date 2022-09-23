import logging
import os
from datetime import date
from unidecode import unidecode


class Logger:
    def __init__(self, currentFile=__file__, clear= True):
        """
            Auto create directory with date time and unicode message log

            *Params:
                currentFile: to add path file running in log message
                clear: to clear data of log file
            *Methods:
                info: log info
                warning: log warning
                error: log error
        """
        today = date.today()
        logName = today.strftime("%Y.%m.%d.log")

        self.__file__ = os.path.abspath(os.path.normpath(currentFile))
        self.logDir = "log"
        self.logFile = os.path.join(self.logDir, logName)
        self.log = logging
        os.makedirs(self.logDir, exist_ok=True)
        if clear or not os.path.exists(self.logFile):
            self.clear()
        logging.basicConfig(
            format=f"[%(asctime)s] - %(levelname)-6s: ['{self.__file__}'] - %(message)s",
            filename=self.logFile,
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )
        logging.raiseExceptions = False

    def clear(self):
        with open(self.logFile, "w"):
            pass

    def info(self, msg):
        self.log.info(f"{unidecode(msg)}")

    def warning(self, msg):
        self.log.warning(f"{unidecode(msg)}")

    def error(self, msg):
        self.log.error(f"{unidecode(msg)}")

if __name__ == "__main__":
    logger = Logger(currentFile=__file__)
    print(logger.__file__)