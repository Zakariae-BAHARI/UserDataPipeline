import requests
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def extract_users():
    response = requests.get('https://randomuser.me/api/?results=10')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def upload_to_s3(data, bucket_name, file_name):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)

if __name__ == "__main__":
    bucket_name = os.getenv('S3_BUCKET_NAME')
    user_data = extract_users()
    if user_data:
        upload_to_s3(str(user_data), bucket_name, 'random_users.json')
