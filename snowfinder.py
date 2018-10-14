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


"""""
# Variable list objects 
resort_list = df.iloc[:, 0]
new_snow = df.iloc[:, 1]
conditions = df.iloc[:, 2]
open_terrian = df.iloc[:, 3]
comments = df.iloc[:, 4
""
# Export to CSV within google co alb 

from google.colab import files
# do not print header and do not print index column 
df.to_csv('SnowDatabaseExport.csv', header=0, index=False)
files.download('SnowDatabaseExport.csv')
