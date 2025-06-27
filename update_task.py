import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    try:
        task_id = event['pathParameters']['id']
        body = json.loads(event['body'])

        response = table.update_item(
            Key={'id': task_id},
            UpdateExpression="set title=:t, description=:d, #dt=:dt",
            ExpressionAttributeNames={
                "#dt": "date"
            },
            ExpressionAttributeValues={
                ':t': body['title'],
                ':d': body['description'],
                ':dt': body['date']
            },
            ReturnValues="ALL_NEW"
        )

        updated_item = response.get('Attributes', {})

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Task updated', 'task': updated_item})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

