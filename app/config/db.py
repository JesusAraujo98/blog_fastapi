from pymongo import MongoClient
import urllib.parse
from app.config import SECRETS

username = urllib.parse.quote_plus(SECRETS.DB_USERNAME) 
password = urllib.parse.quote_plus(SECRETS.DB_PASSWORD)

conn = MongoClient("monguito", 27017, username=username, password=password)
