import os

API_VERSION = '0.1'

"""Database config"""
PORT = os.getenv("PORT", 5000)
MONGO_URI = os.getenv("MONGO_URI", None)



