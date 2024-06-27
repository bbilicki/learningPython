import random
import time
import pprint
#web scraping
from bs4 import BeautifulSoup
import requests
#pandas
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

#iterators
it = iter([1,2,3,4])  
number = it.__next__()
print(number)
number = it.__next__()
print(number)
number = it.__next__()
print(number)
number = it.__next__()

#web scraping
url = input("Enter a URL:  ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data,'html.parser')
print(soup.get_text())
#https://www.linkedin.com/feed/
for link in soup.find_all('a'):
    print(link.get('href'))

for image in soup.find_all('img'):
    print(image.get('src'))


df = pd.read_excel('test.xlsx')

