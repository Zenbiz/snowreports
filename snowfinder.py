import pandas as pd
!pip show pandas
import requests
!pip show requests
from bs4 import BeautifulSoup
!pip show bs4
!pip install tabulate
from tabulate import tabulate
!pip show tabulate
import csv 
!pip show csv
import bs4
!pip3 install lxml
import lxml
import bs4.builder._lxml


res = requests.get('http://www.WEBSITE.com/news/snow-report/')
soup = BeautifulSoup(res.content,'lxml')

#!pip show lxml
table = soup.find_all('table')[0] 

df = pd.read_html('http://www.WEBSITE.com/news/snow-report/', header=0)[0]
df
