import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.iplt20.com/stats/2024'
# putting the url we need to scrape

requests.get(url)
# here we get no error running this code so we will continue 

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

print(soup)
# this will print the html foramt of the given link

print(soup.prettify())

