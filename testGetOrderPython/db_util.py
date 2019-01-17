#!/usr/bin/python
import psycopg2

db_host = "tripsdev.cnfqsmapnljd.us-west-2.rds.amazonaws.com"
db_port = 5432
db_name = "DispatchOrders"
db_user = "root"
db_pass = "welcome001*"
db_table = "tablename"


def make_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print ("I am unable to connect to the database")
    return conn


def fetch_data(conn, query):
    result = []
    print ("Now executing: %s" % (query))
    cursor = conn.cursor()
    cursor.execute(query)

    raw = cursor.fetchall()
    for line in raw:
        result.append(line)

    return result
