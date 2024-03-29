from __future__ import print_function
import boto3
import base64

client = boto3.client('sns')
# Include your SNS topic ARN here.
topic_arn = 'arn:aws:sns:eu-north-1:533950634958:CadabraAlarms'

def lambda_handler(event, context):
    try:
        client.publish(TopicArn=topic_arn, Message='Investigate sudden surge in orders', Subject='Cadabra Order Rate Alarm')
        print('Successfully delivered alarm message')
    except Exception:
        print('Delivery failure')