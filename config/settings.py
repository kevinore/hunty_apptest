import os
from dotenv import load_dotenv

load_dotenv()
API_VERSION = '0.1'

PORT = os.getenv("PORT")
MONGO_URI = os.getenv("MONGO_URI")



