import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_shopee(search_query, edge_driver_path):
    # Initialize a Selenium WebDriver with Microsoft Edge
    driver = webdriver.Edge(executable_path=edge_driver_path)

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

# User input for the path to Microsoft Edge Driver
edge_driver_path = st.text_input("Enter the path to Microsoft Edge Driver:")

# Check if the user has entered a query and the Edge driver path
if user_query and edge_driver_path:
    # Scrape Shopee based on user input
    results = scrape_shopee(user_query, edge_driver_path)

    # Display the scraped results
    st.subheader("Scraped Results:")
    for result in results:
        st.write(f"Product Name: {result['Product Name']}")
        st.write(f"Product Price: {result['Product Price']}")
        st.write("=" * 30)
