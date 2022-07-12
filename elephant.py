import psycopg2
import requests
import os

password = os.environ['elephant_key']
session = requests.Session()
session.auth = ('', password)
link = None
conn = None
pg = None

############################################ create_database ############################################
def create_database(name):
  try:
    response = session.post('https://customer.elephantsql.com/api/instances', data={'name': '{}'.format(name), 'plan': 'turtle', 'region': 'amazon-web-services::eu-north-1'})
    url = session.get('https://customer.elephantsql.com/api/instances/{}'.format(response.json()["id"]))
    global link
    link = url.json()["url"]
  except Exception as e:
    print("unable to create database \n reason: {}".format(e))
  else:
    print("created {} database".format(name))

############################################ connect ############################################
def connect(name):
  global conn
  global pg
  try:
    conn = psycopg2.connect(link)
  except Exception as e:
    print("unable to connect to database\n reason: {}".format(e))
  else:
    print("connected to {}".format(name))
    
  pg = conn.cursor()
