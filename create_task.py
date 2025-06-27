import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        task_id = str(uuid.uuid4())

        item = {
            'id': task_id,
            'title': body['title'],
            'description': body['description'],
            'date': body['date']
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Task created', 'id': task_id})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

