# Created by Luis Fuentes
# sam local invoke "DataEngineeringRDS" -e events/event.json -n events/envs.json

import sys
import os
import pymysql

# Getting envariomental variables
RDS_HOST = os.environ["RDS_HOST"]
DBNAME = os.environ["DBNAME"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

try:
    # pymysql.connect() outside of the handler allows your function to re-use the database connection for better performance
    print("------Begin-----")
    conn = pymysql.connect(RDS_HOST, user=USERNAME, passwd=PASSWORD, db=DBNAME, connect_timeout=5)
    print("Connection was succesful")
except pymysql.MySQLError as e:
    print("Connection was NOT successful")
    print(e)
    sys.exit()

def lambda_handler(event, context):
    """This function connects to a AWS RDS instance

    Parameters:

    event (str): JSON event

    context (str): JSON context

    :Returns: None

    """

    item_count = 0

    with conn.cursor() as cur:
        # cur.execute('insert into Employee (EmpID, Name) values(3, "Mary")')
        # conn.commit()
        cur.execute("SELECT COUNT(*) FROM UPS_MASTER")
        for row in cur:
            item_count += 1
            print(row)
    conn.commit()
