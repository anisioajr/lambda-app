# try it
from dotenv import load_dotenv
import os

load_dotenv()

api_key = ${{ secrets.AWS_ACCESS_KEY_ID }}
api_secret = ${{ secrets.AWS_SECRET_ACCESS_KEY }}

print("API_KEY: ", api_key)
print("API_SECRET: ", api_secret)
