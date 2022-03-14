from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome('/Users/jingyangfan/.wdm/drivers/chromedriver/mac64_m1/99.0.4844.51/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.zolo.ca')

print(driver.page_source)


# # get html data using requests
# URL = "https://www.zolo.ca"

# page = requests.get(URL)

# # parse html data using BeautifulSoup
# soup = BeautifulSoup(page.content, "html.parser")

# # identify id
# results = soup.find(id='listing_container')
# print(page.text)