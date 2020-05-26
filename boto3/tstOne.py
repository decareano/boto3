import json
import boto3

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], 
                                    event['last_name'])  
    return { 
        'message' : message
    }  
    
    
print(lambda_handler(1, 5))

