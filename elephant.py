import psycopg2
import psycopg2.extras
import requests
import os
import json

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
    
  pg = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

############################################ create_tables ############################################
def create_tables():
  try:
    pg.execute("CREATE TABLE client(id INTEGER PRIMARY KEY, name VARCHAR(64), last_name VARCHAR(64), zip_code VARCHAR(6))")
  except Exception as e:
    print("unable to create table 'client' \n reason: {}".format(e))
  else:
    print("created table client")
    conn.commit()

  try:
    pg.execute("CREATE TABLE address(id INTEGER PRIMARY KEY, country VARCHAR(64), city VARCHAR(64), street VARCHAR(64), number INTEGER, zip_code VARCHAR(6))")
  except Exception as e:
    print("unable to create table 'address' \n reason: {}".format(e))
  else:
    print("created table address")
    conn.commit()

  try:
    pg.execute("CREATE TABLE film(id INTEGER PRIMARY KEY, name VARCHAR(255), category VARCHAR(64), length INTEGER, language VARCHAR(64))")
  except Exception as e:
    print("unable to create table 'film' \n reason: {}".format(e))
  else:
    print("created table film")
    conn.commit()

############################################ fill_tables ############################################
def fill_tables():
  try:
    pg.execute("INSERT INTO client(id,name,last_name,zip_code) VALUES (1,'Patryk','Kowalski','52-856'), (2,'Maria','Kowalska','52-856'), (3,'Patryk','Nowak','62-718')")
  except Exception as e:
    print("unable to insert values into 'client' \n reason: {}".format(e))
  else:
    print("inserted values into 'client'")
    conn.commit()

  try:
    pg.execute("INSERT INTO address(id,country,city,street,number,zip_code) VALUES (1,'Poland','Warszawa','Miejska',26,'52-856'), (2,'Poland','Poznan','Owcza',75,'62-718')")
  except Exception as e:
    print("unable to insert values into 'address' \n reason: {}".format(e))
  else:
    print("inserted values into 'address'")
    conn.commit()

  try:
    pg.execute("INSERT INTO film(id,name,category,length,language) VALUES (1,'Inside Man','Thriller',129,'english'), (2,'The Sandman','Horror',112,'english')")
  except Exception as e:
    print("unable to insert values into 'film' \n reason: {}".format(e))
  else:
    print("inserted values into 'film'")
    conn.commit()

############################################ queries ############################################
def queries():
  try:
    pg.execute("SELECT * FROM client WHERE zip_code = '52-856'")
  except Exception as e:
    print("unable to process query 1.3.1 \n reason: {}".format(e))
  else:
    jsonik = json.dumps(pg.fetchall())
    print(jsonik)
    print("processed query 1.3.1")
    conn.commit()

  try:
    pg.execute("SELECT address.country, address.city, address.street, address.number, address.zip_code FROM address INNER JOIN client ON address.zip_code=client.zip_code WHERE client.name = 'Patryk' AND client.last_name = 'Nowak'")
  except Exception as e:
    print("unable to process query 1.3.2 \n reason: {}".format(e))
  else:
    jsonik = json.dumps(pg.fetchall())
    print(jsonik)
    print("processed query 1.3.2")
    conn.commit()

  try:
    pg.execute("SELECT * FROM film WHERE category = 'Thriller' AND language = 'english'")
  except Exception as e:
    print("unable to process query 1.3.3 \n reason: {}".format(e))
  else:
    jsonik = json.dumps(pg.fetchall())
    print(jsonik)
    print("processed query 1.3.3")
    conn.commit()