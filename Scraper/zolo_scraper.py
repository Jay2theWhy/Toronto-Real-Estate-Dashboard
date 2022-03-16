from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome('/Users/jingyangfan/.wdm/drivers/chromedriver/mac64_m1/99.0.4844.51/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())

# get soup from page link
def get_page(page_link):
    url = page_link
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

    # parse html
    html = soup.find('main', id = "listing_container")\
        .find('section', id = 'gallery')\
        .find('div', class_ = 'listings-wrapper xs-flex xs-flex-wrap xs-grid sm-grid-cols-2 lg-grid-cols-3 xl-grid-cols-4 xs-gap-2 sm-gap-3 xs-mx2- sm-mx0')\
        .findAll('article', class_ = 'card-listing xs-relative xs-full-height xs-flex xs-flex-column-reverse xs-flex-justify-end rounded shadow-card xs-overflow-hidden new')
    
    # get link for each listing on the page
    for div in html:
        div = div.find('div', class_ = 'card-listing--details xs-p2 xs-text-4 fill-white flex xs-flex-column xs-flex-shrink-0 xs-relative')
        
        # break into html blocks
        address_block = div.find('div', class_ = 'card-listing--location text-5 truncate xs-flex-order-2')\
            .find('a', class_ = 'address text-primary')\
            .find('h3', class_ = 'card-listing--location text-5 xs-inline')
        
        other_block = div.find('ul', class_ = 'card-listing--values truncate list-unstyled xs-flex-order-1 xs-mb05')

        # price
        price = other_block.find('li', class_ = 'price xs-block xs-mb1 text-2 heavy')\
            .find('span', itemprop = 'price')
        print(price['value'])

        # address
        print(address_block.find('span', class_ = 'street').string)
        print(address_block.find('span', class_ = 'city').string)
        print(address_block.find('span', class_ = 'province').string)

        # bed, bath, sqft
        bed_bath_sqft = other_block.findAll('li', class_ = 'xs-inline xs-mr1')
        for item in bed_bath_sqft:
            print(item.string)

get_info('https://www.zolo.ca/toronto-real-estate/page-1')


# # get html data using requests
# URL = "https://www.zolo.ca"

# page = requests.get(URL)

# # parse html data using BeautifulSoup
# soup = BeautifulSoup(page.content, "html.parser")

# # identify id
# results = soup.find(id='listing_container')
# print(page.text)