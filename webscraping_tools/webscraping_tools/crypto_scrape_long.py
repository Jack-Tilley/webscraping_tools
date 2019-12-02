from bs4 import BeautifulSoup
from selenium import webdriver
# from webscraping_tools import webscrapingTools as wt
import time
import requests
import os.path
from os import path
import csv

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options = selenium.webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent={0}'.format(user_agent))

def create_table():
    url = "https://www.cryptocurrencychart.com/"
    page = requests.get(url)
    driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver',chrome_options=options)
    driver.get(url)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(60)
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(10)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    time.sleep(2)
    driver.close()
    soup = BeautifulSoup(innerHTML, "html.parser")
    soupscope = soup.find("table", attrs={"id": "currency-table"})
    table = wt.TableScrape(soupscope, keep_all_text=True, separated_header=False, ignore_columns=[3,9,10])
    table = table.scrape()
    return table

def table_to_csv(table,dir):
    header = table[0]
    body = table[1:]
    if os.path.isdir(dir):
        for crypto in body:
            crypto_name = crypto[1].replace("\n","").replace("|","")
            if os.path.isfile(dir + crypto_name + ".csv"):
                with open(dir + crypto_name + ".csv", 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(crypto)
            else:
                with open(dir + crypto_name + ".csv", 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerow(crypto)
            f.close()

table = create_table()
dir = "/Users/Tilley/PycharmProjects/CryptoScrape/venv/crypto_csv/"
table_to_csv(table,dir)

## add date to csv
