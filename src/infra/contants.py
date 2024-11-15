import os


GLOBAL_PATH = os.path.abspath(__file__)
PROJECT_PATH = GLOBAL_PATH.split('src')[0][:-1]
JSON_DATA = fr'{PROJECT_PATH}\src\infra\files\person_data.json'
