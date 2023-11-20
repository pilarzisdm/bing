import requests
from bs4 import BeautifulSoup

def scrape_shopee(search_query):
    # Shopee search URL
    shopee_url = f'https://shopee.com.my/search?keyword={search_query}'

    # Send a GET request to the Shopee search page
    response = requests.get(shopee_url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product information (adjust this based on the Shopee page structure)
        product_list = soup.find_all('div', class_='row shopee-search-item-result__items')

        for product in product_list:
            # Extract product details
            product_name = product.find('div', class_='Bn8MAD').text.strip()
            product_price = product.find('span', class_='WTFwws').text.strip()

            # Print or process the extracted information
            print(f'Product Name: {product_name}\nProduct Price: {product_price}\n{"="*30}')

    else:
        print(f"Failed to fetch Shopee search results. Status code: {response.status_code}")

# Example: Scraping Shopee for "laptop"
scrape_shopee("laptop")
