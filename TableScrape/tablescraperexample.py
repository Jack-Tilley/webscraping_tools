# Jack Tilley
# tablescraperexample.py
# February 2019
# This program demonstrates how to use tablescraper.py

from tablescraper import TableScrape
from bs4 import BeautifulSoup
from selenium import webdriver
from tablescraper import TableScrape
import time

# For non-dynamically loaded webpages, simply use bs4 and requests
url = "https://www.w3schools.com/html/html_tables.asp"
driver = webdriver.Chrome('PATH TO CHROMEDRIVER') # Necessary for dynamically loaded webpages
driver.get(url)
# time.sleep(3) # waits for webpage to load before scraping if necessary
innerHTML = driver.execute_script("return document.body.innerHTML")
driver.close()
soup = BeautifulSoup(innerHTML, "html.parser")
soupscope = soup.find("table",attrs={"id": "customers"}) # location of table to be scraped
table = TableScrape(soupscope, separated_header=False)
print(table.scrape())

# returns:
# [['Company', 'Contact', 'Country'],
#  ['Alfreds Futterkiste', 'Maria Anders', 'Germany'],
#  ['Centro comercial Moctezuma', 'Francisco Chang', 'Mexico'],
#  ['Ernst Handel', 'Roland Mendel', 'Austria'],
#  ['Island Trading', 'Helen Bennett', 'UK'],
#  ['Laughing Bacchus Winecellars', 'Yoshi Tannamuri', 'Canada'],
#  ['Magazzini Alimentari Riuniti', 'Giovanni Rovelli', 'Italy']]
