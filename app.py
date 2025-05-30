import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': 'visitor_count'},
            UpdateExpression='SET visit_count = if_not_exists(visit_count, :start) + :inc',
            ExpressionAttributeValues={':start': Decimal(0), ':inc': Decimal(1)},
            ReturnValues='UPDATED_NEW'
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'visit_count': int(response['Attributes']['visit_count'])})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
