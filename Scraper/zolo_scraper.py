from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome('/Users/jingyangfan/.wdm/drivers/chromedriver/mac64_m1/99.0.4844.51/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())

# get the number of pages to cycle through
def num_of_pages(page_link):
    soup = get_page(page_link)
    html = soup.find('section', class_='supplementary-nav xs-my6 xs-flex xs-flex-column xs-flex-align-center')\
        .find('nav', class_ = 'xs-hide md-flex')\
        .findAll('a', class_ = 'button button--mono button--large xs-mr1')
    return html[-1].string

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

# get preview information for one page
def get_preview_info(page_link):
    # get previews data
    driver.get(page_link)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

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

# get preview information for multiple pages
def get_preview_info_multi(page_link, num_pages):
    # get previews data
    driver.get(page_link)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

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
        
        next_page_button = driver.find_element(By.CSS_SELECTOR, "button button--mono button--large xs-flex xs-flex-align-center xs-mr1")
        next_page_button.click()

print(get_preview_info_multi('https://www.zolo.ca', 1))
# print(num_of_pages('https://www.zolo.ca'))