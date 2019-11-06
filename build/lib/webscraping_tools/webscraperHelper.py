from webscraping_tools import webscrapingTools as wt
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

class scrapeHelper():
    def __init__(self, url, scrape_type, element_name="", attrs=[], title_name="", scrape_all=False, page_html="",
                 dynamically_loaded=False, scrollable=False, wait_time=2, end_time = 30, path_to_driver=""
                 ):
        self.url = url
        self.scrape_type = scrape_type
        self.element_name = element_name
        self.attrs = attrs
        self.title_name = title_name
        self.scrape_all=scrape_all
        self.page_html = page_html
        self.dynamically_loaded = dynamically_loaded
        self.scrollable = scrollable
        self.wait_time = wait_time
        self.path_to_driver = path_to_driver
        self.end_time = end_time
        self.is_found = False

    #def

    def is_table(self):
        pass





