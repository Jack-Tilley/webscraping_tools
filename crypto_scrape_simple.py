from webscrapingTools import *
from bs4 import BeautifulSoup
from selenium import webdriver
from scrapeHelper import *

table = scraperHelper.table_scrape("https://www.cryptocurrencychart.com/",'PATHTOCHROMEDRIVER')
print(table)
