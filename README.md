# webscraping_tools
Tools to make webscraping easier

# Installation:
1) in your terminal, type: `pip install webscraping_tools`
2) Make sure bs4 and selenium have been pip installed
3) In a python window, type: `from webscraping_tools import webscrapingTools, ezScrape`

# Using ezScrape.py:
ezScrape is a quick and easy way to scrape any table or list from a website. All you need is the website URL and a path to the webdriver of your choice. ezScrape returns a nested list containing your scraped data

To scrape a table from any website:
1) `table_data = ezScrape.table_scrape("WEBSITE_URL_TO_BE_SCRAPED", "PATH_TO_SELENIUM_DRIVER")`
2) `print(table_data)`
3) Done.

To scrape a list from any website:
1) `list_data = ezScrape.list_scrape("WEBSITE_URL_TO_BE_SCRAPED", "PATH_TO_SELENIUM_DRIVER")`
2) `print(list_data)`
3) Done.

# Using webscrapingTools.py:
webscrapingTools is a powerful way to gather lists, tables, and general content from a website. webScrapingTools requires a basic understanding of html to be utilized but can be customized to handle more complex tasks than ezScrape. 

To use, take a look at webscrapingtoolsexample.py for a basic understanding.
