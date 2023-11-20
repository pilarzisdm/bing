from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=2')

driver = webdriver.Chrome(options=chrome_options)

katakunci = input('Masukkan kata kunci : ')

def search(katakunci):
    links = []
    print('mencari semua product dengan kata kunci ' + katakunci)
    url = 'https://shopee.co.id/search?keyword=' + katakunci
    try:
        driver.get(url)
        time.sleep(5)
        driver.execute_script('window.scrollTo(0, 1500);')
        time.sleep(5)
        driver.execute_script('window.scrollTo(0, 2500);')
        time.sleep(5)
        soup_a = BeautifulSoup(driver.page_source, 'html.parser')
        products = soup_a.find('div', class_='row shopee-search-item-result__items')
        for link in products.find_all('a'):
            links.append(link.get('href'))
            print(link.get('href'))
    except TimeoutException:
        print('failed to get links with query ' + katakunci)
    return links

product_urls = search(katakunci)
