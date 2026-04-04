import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    item_id = event['pathParameters']['id']
    location_id = int(event['queryStringParameters']['location_id'])

    response = table.get_item(
        Key={
            'item_id': item_id,
            'location_id': location_id
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response.get('Item', {}), default=decimal_default)
    }