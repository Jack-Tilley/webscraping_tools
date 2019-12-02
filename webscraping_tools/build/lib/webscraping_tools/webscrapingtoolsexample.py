from webscraping_tools import webscrapingTools as wt
from bs4 import BeautifulSoup
from selenium import webdriver
#import selenium
import time
#from selenium.webdriver.chrome.options import Options
import requests

# TABLESCRAPE EXAMPLE
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
x = wt.TableScrape(soupscope, keep_all_text=True, separated_header=False)
print(x.scrape())

# CONTENTSCRAPE EXAMPLE
url = "https://www.youtube.com/"
page = requests.get(url)
driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver')
driver.get(url)
time.sleep(2)
innerHTML = driver.execute_script("return document.body.innerHTML")
time.sleep(2)
driver.close()
soup = BeautifulSoup(innerHTML, "html.parser")
time.sleep(5)
soupscope = soup.find("ytd-section-list-renderer", attrs={"id": "primary","class":"style-scope ytd-two-column-browse-results-renderer"})
# z = soup.find_all("ytd-grid-video-renderer", attrs={"class":"style-scope yt-horizontal-list-renderer"})
# print(z)
y = wt.ContentScrape(soupscope, item_tag_value="ytd-grid-video-renderer",
                  item_attribute="class", item_attribute_value="style-scope yt-horizontal-list-renderer")
print(y.scrape())

# LISTSCRAPE EXAMPLE
url = "https://www.futhead.com/19/players/?bin_platform=ps"
page = requests.get(url)
driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver')
driver.get(url)
time.sleep(2)
innerHTML = driver.execute_script("return document.body.innerHTML")
time.sleep(2)
driver.close()
soup = BeautifulSoup(innerHTML, "html.parser")
time.sleep(5)
soupscope = soup.find("ul", attrs={"class": "list-group list-group-table player-group-table"})
z = wt.ListScrape(soupscope, rows_to_ignore=[0, 1])
print(z.scrape())

# TODO
# url = "https://www.w3.org/TR/html401/struct/lists.html"
# page = requests.get(url)
# driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver')
# driver.get(url)
# innerHTML = driver.execute_script("return document.body.innerHTML")
# driver.close()
# soup = BeautifulSoup(innerHTML, "html.parser")
# time.sleep(5)
# soupscope = soup.find("ul")
# x = ListScrape(soupscope)
# print(x.scrape())
# url = "https://www.cryptocurrencychart.com/"
# page = requests.get(url)
# time.sleep(2)
# #driver = webdriver.PhantomJS()
# options = Options()
# options.headless = True
# driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver', chrome_options=options)
# time.sleep(2)
# # driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver')
# innerHTML = driver.page_source
# time.sleep(2)
# soup = BeautifulSoup(innerHTML, "html.parser")
# soupscope = soup.find("table", attrs={"id": "currency-table"})
# x = wt.TableScrape(soupscope, keep_all_text=True, separated_header=False)
# print(x.scrape())
