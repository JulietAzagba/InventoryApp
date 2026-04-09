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
    response = table.scan()

    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'], default=decimal_default)
    }