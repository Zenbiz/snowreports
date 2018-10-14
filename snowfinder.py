# to install a program within colab use !pip install 

import pandas as pd
# !pip show pandas
import requests
# !pip show requests
from bs4 import BeautifulSoup
# !pip show bs4
# !pip install tabulate
from tabulate import tabulate
# pip show tabulate
import csv 
# pip show csv
import bs4
# pip3 install lxml
import lxml
import bs4.builder._lxml


res = requests.get('http://www.WEBSITE.com/news/snow-report/')
soup = BeautifulSoup(res.content,'lxml')

#!pip show lxml
table = soup.find_all('table')[0] 

df = pd.read_html('http://www.WEBSITE.com/news/snow-report/', header=0)[0]
df

# Variable list objects 
resort_list = df.iloc[:, 0]
new_snow = df.iloc[:, 1]
conditions = df.iloc[:, 2]
open_terrian = df.iloc[:, 3]
comments = df.iloc[:, 4

"""
# Export to CSV within google co lab 
from google.colab import files
# do not print header and do not print index column 
df.to_csv('SnowDatabaseExport.csv', header=0, index=False)
files.download('SnowDatabaseExport.csv')
"""

                   
#Below is under heavy construction: Connecting pandas df to postgres (not complete)

"""
# Create a Postgres table for dataframe import 
# https://www.dataquest.io/m/245/intro-to-postgres/4/creating-a-table
conn = psycopg2.connect("dbname=DATABASENAME user=DBUSERNAME")
cur = conn.cursor()
cur.execute("CREATE TABLE users(id integer PRIMARY KEY, email text, name text, address text)")
"""
                   
"""
with open('user_accounts.csv') as f:
    reader = csv.reader(f)
    next(reader)
    rows = [row for row in reader]
"""
                   
"""
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
for row in rows:
    cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", row)
conn.commit()

cur.execute('SELECT * FROM users')
users = cur.fetchall()
conn.close()
"""
                  
"""
conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
# sample_file.csv has a header row.
with open('SnowDataBaseExport.csv', 'r') as f:
    # Skip the header row.
    next(f)
    cur.copy_from(f, 'users', sep=',')
conn.commit()

cur.execute('SELECT * FROM new_snow')
users = cur.fetchall()
conn.close()
"""
                   
"""
# Get all the data from snow data through SQL 
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('SELECT * FROM snow_report')
notes = cur.fetchall()
conn.close()
"""
