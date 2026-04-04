import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    location_id = int(event['pathParameters']['id'])
    
    response = table.query(
        IndexName='location_id-item_id-index',
        KeyConditionExpression=boto3.dynamodb.conditions.Key('location_id').eq(location_id)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }