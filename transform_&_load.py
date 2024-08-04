import json
import boto3
import pymysql
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=os.getenv('S3_BUCKET_NAME'), Key='random_users.json')
    data = response['Body'].read().decode('utf-8')
    users = json.loads(data)

    connection = pymysql.connect(
        host=os.getenv('RDS_ENDPOINT'),
        user=os.getenv('RDS_USERNAME'),
        password=os.getenv('RDS_PASSWORD'),
        database=os.getenv('RDS_DATABASE')
    )

    cursor = connection.cursor()
    for user in users['results']:
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(sql, (user['name']['first'] + " " + user['name']['last'], user['email']))

    connection.commit()
    cursor.close()
    connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully')
    }
