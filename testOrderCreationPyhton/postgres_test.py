#!/usr/bin/python

import psycopg2
import json
import datetime
import uuid
import math
import random


from db_util import make_conn, fetch_data, insert_data

        
def lambda_handler(event, context):
    uuidSubStr = str(uuid.uuid1())[0:20]
  
    insertOrdersTextQry = "INSERT INTO ORDERS1 (order_id, order_date, cust_id, supplier_id, description, remarks) VALUES (%s,%s,%s,%s,%s,%s);"  
    insertOrdersItemsTextQry = "INSERT INTO ORDER_ITEMS1 (item_id, order_id, item_description, qty, net_price) VALUES (%s,%s,%s,%s,%s);" 
   
    insertDriversTextQry = "INSERT INTO DRIVERS1 (DRIVERS_ID, D_NAME, PHONE, TRIP_UNIT_COST) VALUES (%s,%s,%s,%s);" 
    insertTripsTextQry = "INSERT INTO TRIPS1 (TIP_ID, order_id, PHONE, FROM_ADDRESS, DESTINATION_ADDRESS) VALUES (%s,%s,%s,%s,%s);" 
   
   
    insertOrdersQryData = ("Ord-" + uuidSubStr, datetime.datetime.now(),"Cust-"+uuidSubStr,"Sup-"+uuidSubStr,"Test Description","None")
    insertOrdersItemsQryData = ("Item-"+uuidSubStr,"Ord-"+uuidSubStr,"Test Item description", random.randrange(1000) ,random.randrange(5000))
    inserttDriversQryData = ("DriverId-"+uuidSubStr[0:10],"DrName-"+uuidSubStr[0:10],random.randrange(10000), random.randrange(10000))
    insertTripsQryData = ("Trip_Id-"+uuidSubStr[0:10],"Ord-" + uuidSubStr,random.randrange(10000), "From-"+uuidSubStr[0:10],"Dest-"+uuidSubStr[0:10])
    
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = make_conn()

    insert_data(conn, insertOrdersTextQry,insertOrdersQryData)
    insert_data(conn, insertOrdersItemsTextQry,insertOrdersItemsQryData)
    insert_data(conn, insertDriversTextQry,inserttDriversQryData)
    insert_data(conn, insertTripsTextQry,insertTripsQryData)
     
    
     
    
