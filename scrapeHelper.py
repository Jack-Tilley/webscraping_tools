# import PhantomJS
from webscrapingTools import TableScrape
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.options import Options
import requests


def table_scrape(url, PATH_TO_DRIVER, scroll_time=0, is_multi_tables=False):
    driver = webdriver.Chrome(PATH_TO_DRIVER)
    driver.get(url)
    time.sleep(2)
    if scroll_time > 0:  # TODO
        pass
    innerHTML = driver.execute_script("return document.body.innerHTML")
    time.sleep(2)
    driver.close()
    soup = BeautifulSoup(innerHTML, "html.parser")
    soupscope = soup.find_all("table")
    if not is_multi_tables:
        scraping = TableScrape(soupscope[0], keep_all_text=True, separated_header=False)
        return scraping.scrape()
    table_list = []
    for each_table in soupscope:
        scraping = TableScrape(each_table, keep_all_text=True, separated_header=False)
        table_list.append(scraping.scrape())
    return scraping.scrape()

# table = table_scrape("https://www.cryptocurrencychart.com/",'/Users/Tilley/Downloads/chromedriver')
# print(table)