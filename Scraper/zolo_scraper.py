from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome('/Users/jingyangfan/.wdm/drivers/chromedriver/mac64_m1/99.0.4844.51/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())

def get_page(page_num):
    url = f'https://www.zolo.ca/toronto-real-estate/page-{page_num}'
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    return soup

# get links for listing on zolo page
def get_links(page_link):
    soup = get_page(page_link)

    # parse html
    html = soup.find('main', id = "listing_container")\
        .find('section', id = 'gallery')\
        .find('div', class_ = 'listings-wrapper xs-flex xs-flex-wrap xs-grid sm-grid-cols-2 lg-grid-cols-3 xl-grid-cols-4 xs-gap-2 sm-gap-3 xs-mx2- sm-mx0')\
        .findAll('article', class_ = 'card-listing xs-relative xs-full-height xs-flex xs-flex-column-reverse xs-flex-justify-end rounded shadow-card xs-overflow-hidden new')
    
    # get link for each listing on the page
    for div in html:
        div = div.find('div', class_ = 'card-listing--image fill-white xs-relative xs-overflow-hidden')
        print(div.find('a')['href'])

def get_info(page_link):
    soup = get_page(page_link)

# # get html data using requests
# URL = "https://www.zolo.ca"

# page = requests.get(URL)

# # parse html data using BeautifulSoup
# soup = BeautifulSoup(page.content, "html.parser")

# # identify id
# results = soup.find(id='listing_container')
# print(page.text)