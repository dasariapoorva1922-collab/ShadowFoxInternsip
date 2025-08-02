import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    data = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.replace("Â", "")
        rating = book.p["class"][1]
        data.append([title, price, rating])

    return data

# Main function to scrape all pages
def scrape_all_pages():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_data = []

    for page in range(1, 51):  # Scrape pages 1 to 50
        url = base_url.format(page)
        print(f"Scraping page {page}...")
        page_data = scrape_page(url)
        all_data.extend(page_data)

    # Save all data to a CSV file
    with open("all_books_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Rating"])  # Write header
        writer.writerows(all_data)  # Write all rows

    print("All data has been scraped and saved to 'all_books_data.csv'.")

# Run the scraper
scrape_all_pages()
