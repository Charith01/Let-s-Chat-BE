import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv


DB_URL = ""
DB_NAME = ""
DB_USER = ""
DB_PASS = ""
JWT_SECRET_KEY=""


def initialize_env():
    global DB_URL, DB_NAME, DB_USER, DB_PASS, JWT_SECRET_KEY


logging.info("Initializing the environment variables")
load_dotenv(Path().cwd().__str__() + "/config.env", override=True)

PRIVATE_API_URL = os.environ.get("PRIVATE_API_URL")
DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")

for env_field, env_value in {"DB_URL": DB_URL, "DB_NAME": DB_NAME,
                             "DB_USER": DB_USER, "DB_PASS": DB_PASS, "JWT_SECRET_KEY": JWT_SECRET_KEY
                             }.items():
    if not env_value:
        logging.error(f"{env_field} is not set, exiting...")
        sys.exit(99)

logging.info("Environment is loaded successfully")
