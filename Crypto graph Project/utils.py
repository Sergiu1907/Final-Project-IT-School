import logging
import pathlib
from datetime import datetime


LOGGER_NAME = "main_logger"

root = pathlib.Path(__file__).parent
logs_path = root.joinpath("logs/logs3")
log_filename = datetime.now().strftime("%d%m%Y_%H%M%S.log")
log_abs_path = logs_path.joinpath(log_filename)

def configure_logger():
    try:
        # creem folderul de loguri
        logs_path.mkdir(exist_ok=True, parents=True)
    except OSError as err:
        print(err)

    # Format
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    message_only = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    verbose_fmt = logging.Formatter("<%(asctime)s> <%(msecs)d> - [%(levelname)s] - %(filename)s - %(levelno)s - %(message)s")

    # Handler
    # tipuri de handler https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers
    cli_handler = logging.StreamHandler() # pentru CLI - consola
    # ii spunem ce format sa foloseasca acest handler
    cli_handler.formatter = message_only
    cli_handler.setLevel(logging.INFO)

    # handler care scrie in fisiere
    file_handler = logging.FileHandler(log_abs_path)
    # specificam formatul
    file_handler.formatter = verbose_fmt
    file_handler.setLevel(logging.ERROR)

    # Logger
    # creem un logger nou, care are nevoie de un nume, retinut in LOGGER_NAME
    logger = logging.getLogger(LOGGER_NAME)
    # set nivel de gravitate
    logger.setLevel(logging.DEBUG)
    # adaugam handler la logger
    logger.addHandler(cli_handler)
    # mai adaugam un handler
    logger.addHandler(file_handler)