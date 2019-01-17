#!/usr/bin/python

import psycopg2
import json
import datetime

from db_util import make_conn, fetch_data
from boto3 import client as boto3_client

 

def dateTimeConverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
        
def lambda_handler(event, context):
    
    print(event) 
     
    limtCount = (event["topOrders"]!="") and event["topOrders"] or 10
    query_cmd = "SELECT * from ORDERS1 o, ORDER_ITEMS1 t where o.order_date <= '"+event["order_date"]+"' AND o.order_id = t.order_id ORDER BY t.net_price desc LIMIT "+ limtCount
    
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = make_conn()

    result = fetch_data(conn, query_cmd)
    conn.close()
    
    strjson =  json.dumps(result, default = dateTimeConverter)
    return {"response":strjson}
    
