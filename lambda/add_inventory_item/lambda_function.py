import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    item = {
        'item_id': body['item_id'],
        'location_id': int(body['location_id']),
        'item_name': body['item_name'],
        'item_description': body['item_description'],
        'item_qty_on_hand': int(body['item_qty_on_hand']),
        'item_price': int(body['item_price'])
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item added successfully'})
    }