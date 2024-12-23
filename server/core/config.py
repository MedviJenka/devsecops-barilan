import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    APP_PORT = os.getenv('APP_PORT')
    HOST = os.getenv('HOST')
    DEBUG = True
