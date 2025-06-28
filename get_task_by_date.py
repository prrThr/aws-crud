from boto3.dynamodb.conditions import Attr
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    date = event['queryStringParameters']['date']

    response = table.scan(
        FilterExpression=Attr('date').eq(date)
    )

    items = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
