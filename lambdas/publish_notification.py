import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# from models.models import Notification
from lambda_decorators import json_http_resp, load_json_body
# from helpers import sns

@json_http_resp
@load_json_body
def handler(event, context):
    # event = Notification(**event['body'])
    import boto3
    sns = boto3.client('sns')
    # Publish a simple message to the specified SNS topic
    response = sns.publish(
        TopicArn='arn:aws:sns:region:0786589:my-topic-arn',   
        Message=event["message"],   
    )
    print(response)
    return {"message": f"Notification sent!"}
