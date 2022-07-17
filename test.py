import requests
from bs4 import BeautifulSoup
import pandas as pd
from scrapelib import table_to_2d()

table=[]

page = requests.get('https://wwwin/~coryd/zebu/2109_fe/20220705/sum.html',verify=False)
soup = BeautifulSoup(page.text,parser = 'lxml',features='lxml')

for i in soup.find_all('table'):
    table.append(i)

twod = table_to_2d(table[2])
print(twod)