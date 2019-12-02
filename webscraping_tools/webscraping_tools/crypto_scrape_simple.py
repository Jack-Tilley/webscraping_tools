from webscraping_tools import ezScrape
from bs4 import BeautifulSoup
from selenium import webdriver
from scrapeHelper import *

table = ezScrape.table_scrape("https://www.cryptocurrencychart.com/","/Users/Tilley/Downloads/chromedriver")
print(table)
