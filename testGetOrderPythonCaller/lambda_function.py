#!/usr/bin/python

import json


from boto3 import client as boto3_client

lambda_client = boto3_client('lambda')

payload = {
  "order_date": "2018-11-22",
  "topOrders": "5"
}

        
def lambda_handler(event, context):
    
    resp = lambda_client.invoke(
              FunctionName = "testGetOrderPython",
              InvocationType = "RequestResponse",
              Payload = json.dumps(payload))
    print("response",resp["Payload"].read())
    
    respOrder = lambda_client.invoke(
              FunctionName = "testOrderCreationPyhton",
              InvocationType = "Event",
              Payload = json.dumps(payload))
    return  "Done"
     
    
     
    
