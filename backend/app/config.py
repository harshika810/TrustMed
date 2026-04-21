import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("db_API")
DEBUG = os.getenv("DEBUG")

MONGO_URI = "mongodb+srv://harshika8100_db_user:Harshika810Katyal10@cluster0.huyx7n0.mongodb.net/?appName=Cluster0"

DATABASE_NAME = "trustmed"