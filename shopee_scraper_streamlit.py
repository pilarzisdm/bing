import streamlit as st
import requests
import csv

def get_seller_info(seller_id):
    url = f"https://shopee.co.id/api/v4/shop/get?shopid={seller_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def save_to_csv(seller_data, seller_id):
    filename = f"shopee_seller_{seller_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["Seller ID", "Shop Name", "Total Products", "Rating", "Location"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            "Seller ID": seller_id,
            "Shop Name": seller_data["name"],
            "Total Products": seller_data["item_count"],
            "Rating": seller_data["rating_star"],
            "Location": seller_data["place"]
        })

def main():
    st.title("Shopee Seller Info Scraper")
    seller_id = st.text_input("Enter Shopee seller ID:")
    if st.button("Get Seller Info"):
        seller_data = get_seller_info(seller_id)
        if seller_data:
            save_to_csv(seller_data["data"], seller_id)
            st.success(f"Data saved to shopee_seller_{seller_id}.csv")
            st.write(f"Location: {seller_data['data']['place']}")
        else:
            st.error("Error fetching data. Please check the seller ID.")

if __name__ == "__main__":
    main()
