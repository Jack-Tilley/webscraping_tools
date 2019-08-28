from webscrapingTools import TableScrape
from bs4 import BeautifulSoup
from selenium import webdriver

import time
import requests

url = "https://www.cryptocurrencychart.com/"
page = requests.get(url)
driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver')
driver.get(url)
time.sleep(2)
innerHTML = driver.execute_script("return document.body.innerHTML")
time.sleep(2)
driver.close()
soup = BeautifulSoup(innerHTML, "html.parser")
soupscope = soup.find("table", attrs={"id": "currency-table"})
# ignore = soupscope.find_all("tr", attrs={"class": "expandable"})
# ignore2 = [0,11,12]
x = TableScrape(soupscope, keep_all_text=True, separated_header=False)
print(x.scrape())