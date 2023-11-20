import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_shopee(search_query):
    # Initialize a Selenium WebDriver (make sure to have geckodriver or chromedriver installed)
    driver = webdriver.Firefox()

    # Shopee search URL
    shopee_url = f'https://shopee.com.my/search?keyword={search_query}'

    # Open the Shopee search page
    driver.get(shopee_url)

    # Wait for the page to load (you might need to adjust the waiting time)
    driver.implicitly_wait(10)

    # Get the page source after dynamic content is loaded
    page_source = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract product information (adjust this based on the Shopee page structure)
    product_list = soup.find_all('div', class_='col-xs-2-4 shopee-search-item-result__item')

    scraped_results = []
    for product in product_list:
        # Extract product details
        product_name = product.find('div', class_='yQmmFK').text.strip()
        product_price = product.find('span', class_='WTFwws').text.strip()

        # Add the extracted information to the results list
        scraped_results.append({'Product Name': product_name, 'Product Price': product_price})

    # Close the WebDriver
    driver.quit()

    return scraped_results

# Streamlit app
st.title("Shopee Scraper App")

# User input for the search query
user_query = st.text_input("Enter the product you want to search on Shopee:")

# Check if the user has entered a query
if user_query:
    # Scrape Shopee based on user input
    results = scrape_shopee(user_query)

    # Display the scraped results
    st.subheader("Scraped Results:")
    for result in results:
        st.write(f"Product Name: {result['Product Name']}")
        st.write(f"Product Price: {result['Product Price']}")
        st.write("=" * 30)
