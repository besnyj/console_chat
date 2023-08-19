import logging

localhost = ("192.168.1.215", 10992)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("server log")
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def working(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        logger.info("FUNCTION WORKED AS EXPECTED")
        return value
    return wrapper