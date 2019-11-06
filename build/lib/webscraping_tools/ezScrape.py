from webscraping_tools import webscrapingTools as wt
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
    if scroll_time > 0:
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(scroll_time)
        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(5)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    time.sleep(2)
    driver.close()
    soup = BeautifulSoup(innerHTML, "html.parser")
    soupscope = soup.find_all("table")
    if not is_multi_tables:
        scraping = wt.TableScrape(soupscope[0], keep_all_text=True, separated_header=False)
        return scraping.scrape()
    table_list = []
    for each_table in soupscope:
        scraping = wt.TableScrape(each_table, keep_all_text=True, separated_header=False)
        table_list.append(scraping.scrape())
    return scraping.scrape()

# table = table_scrape("https://www.cryptocurrencychart.com/",'/Users/Tilley/Downloads/chromedriver')
# print(table)

def list_scrape(url, PATH_TO_DRIVER, is_multi_lists=False):
    driver = webdriver.Chrome(PATH_TO_DRIVER)
    driver.get(url)
    time.sleep(2)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    time.sleep(2)
    driver.close()
    soup = BeautifulSoup(innerHTML, "html.parser")
    soupscope = soup.find("ul")
    if not is_multi_lists:
        scraping = wt.ListScrape(soupscope) # TODO
        return scraping.scrape()
    
# list1 = list_scrape("https://www.futhead.com/19/players/?bin_platform=ps",'/Users/Tilley/Downloads/chromedriver')
# print(list1)
