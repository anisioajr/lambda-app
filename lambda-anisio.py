# try it
import os


AWS_ACCESS_KEY_ID = os.environ["aws_access_key_id"]
AWS_SECRET_ACCESS_KEY  = os.environ["aws_secret_access_key"]

print(f"API_KEY: { AWS_ACCESS_KEY_ID}")
print(f"API_SECRET: {AWS_SECRET_ACCESS_KEY}")
