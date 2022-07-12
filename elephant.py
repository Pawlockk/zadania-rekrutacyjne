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

############################################ create_tables ############################################
def create_tables():
  try:
    pg.execute("CREATE TABLE client(id INTEGER, name VARCHAR(64), last_name VARCHAR(64), zip_code VARCHAR(6))")
  except Exception as e:
    print("unable to create table 'client' \n reason: {}".format(e))
  else:
    print("created table client")
    conn.commit()

  try:
    pg.execute("CREATE TABLE address(id INTEGER, country VARCHAR(64), city VARCHAR(64), street VARCHAR(64), number INTEGER, zip_code VARCHAR(6))")
  except Exception as e:
    print("unable to create table 'address' \n reason: {}".format(e))
  else:
    print("created table address")
    conn.commit()

  try:
    pg.execute("CREATE TABLE film(id INTEGER, name VARCHAR(255), category VARCHAR(64), length INTEGER, language VARCHAR(64))")
  except Exception as e:
    print("unable to create table 'film' \n reason: {}".format(e))
  else:
    print("created table film")
    conn.commit()

############################################ create_tables ############################################
def fill_tables():
  try:
    pg.execute("INSERT INTO client(id,name,last_name,zip_code) VALUES (1,'Patryk','Kowalski','52-856')")
    pg.execute("INSERT INTO client(id,name,last_name,zip_code) VALUES (2,'Maria','Kowalska','52-856')")
    pg.execute("INSERT INTO client(id,name,last_name,zip_code) VALUES (3,'Patryk','Nowak','62-718')")
  except Exception as e:
    print("unable to insert values into 'client' \n reason: {}".format(e))
  else:
    print("inserted values into 'client'")
    conn.commit()

  try:
    pg.execute("INSERT INTO address(id,country,city,street,number,zip_code) VALUES (1,'Poland','Warszawa','Miejska',26,'52-856')")
    pg.execute("INSERT INTO address(id,country,city,street,number,zip_code) VALUES (2,'Poland','Poznań','Owcza',75,'62-718')")
  except Exception as e:
    print("unable to insert values into 'address' \n reason: {}".format(e))
  else:
    print("inserted values into 'address'")
    conn.commit()

  try:
    pg.execute("INSERT INTO film(id,name,category,length,language) VALUES (1,'Inside Man','Thriller',129,'english')")
    pg.execute("INSERT INTO film(id,name,category,length,language) VALUES (2,'The Sandman','Horror',112,'english')")
  except Exception as e:
    print("unable to insert values into 'film' \n reason: {}".format(e))
  else:
    print("inserted values into 'film'")
    conn.commit()