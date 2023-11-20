from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

# Set up Firefox options
firefox_options = Options()
# firefox_options.headless = True  # Uncomment this line if you want to run in headless mode

# Create a new instance of the Firefox driver
#driver = webdriver.Firefox(options=firefox_options)
driver = webdriver.Firefox(executable_path='C:/Program Files/Mozilla Firefox', options=firefox_options)


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

        # Wait for the page to load (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-search-item-result__items')))

        soup_a = BeautifulSoup(driver.page_source, 'html.parser')
        products = soup_a.find('div', class_='row shopee-search-item-result__items')
        for link in products.find_all('a'):
            links.append(link.get('href'))
            print(link.get('href'))
    except TimeoutException:
        print('failed to get links with query ' + katakunci)
    return links

product_urls = search(katakunci)

# Close the WebDriver when finished
driver.quit()
