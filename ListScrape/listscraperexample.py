from bs4 import BeautifulSoup
from selenium import webdriver
from tablescraper import TableScrape
import time
import requests
from listscraper import ListScrape


url = "https://www.futhead.com/19/players/?bin_platform=ps"
page = requests.get(url)
driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver')
driver.get(url)
innerHTML = driver.execute_script("return document.body.innerHTML")
driver.close()
soup = BeautifulSoup(innerHTML, "html.parser")
time.sleep(5)
soupscope = soup.find("ul", attrs={"class": "list-group list-group-table player-group-table"})
x = ListScrape(soupscope, rows_to_ignore=[0, 1])
print(x.scrape())
