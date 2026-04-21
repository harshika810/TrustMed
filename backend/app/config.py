import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("db_API")
DEBUG = os.getenv("DEBUG")

DATABASE_NAME = "trustmed"