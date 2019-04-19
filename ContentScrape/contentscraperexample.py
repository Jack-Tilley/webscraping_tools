import requests
from contentscraper import ContentScrape


## If you are getting none as a result, allow the webpage to load, or use selenium scroll feature
url = "https://www.youtube.com/"
page = requests.get(url)
driver = webdriver.Chrome('/Users/Tilley/Downloads/chromedriver')
driver.get(url)
innerHTML = driver.execute_script("return document.body.innerHTML")
driver.close()
soup = BeautifulSoup(innerHTML, "html.parser")
time.sleep(5)
soupscope = soup.find("ytd-section-list-renderer", attrs={"id": "primary","class":"style-scope ytd-two-column-browse-results-renderer"})
# z = soup.find_all("ytd-grid-video-renderer", attrs={"class":"style-scope yt-horizontal-list-renderer"})
# print(z)
x = ContentScrape(soupscope, item_tag_value="ytd-grid-video-renderer",
                  item_attribute="class", item_attribute_value="style-scope yt-horizontal-list-renderer")
print(x.scrape())
