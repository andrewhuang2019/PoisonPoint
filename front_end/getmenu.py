from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import requests
import time

# Trying to use this link to webscrape menu
# https://medium.com/@Fooddatascrape1/how-to-extract-restaurant-menu-data-using-python-2fbb8a57d993

url = 'https://www.chick-fil-a.com/menu' # initializing arbitrary url to restaurant menu

#data = requests.get(url)

# # what does this do
# driver = webdriver.Chrome()
# driver.get(url)
# driver.execute_script("window.scrollTo(1,20000)")
# time.sleep(2)

# # the above code works i think(?) everything after is unexplored 
# html = driver.page_source

#soup = BeautifulSoup(data,'html.parser')

# attempting to print html data
html = urlopen(url).read().decode("utf-8")
b_soup = BeautifulSoup(html, "html.parser")
raw_html = b_soup.get_text()
removed_long_spaces = raw_html.replace("\n","")
print(removed_long_spaces)
print("Deluxe Sandwich" in removed_long_spaces)
