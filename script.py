import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

books = []
for item in soup.find_all("article", class_="product_pod"):
    title = item.find("h3").find("a")["title"]
    price = item.find("p", class_="price_color").text
    rating = item.find("p", class_="star-rating")["class"][1]
    books.append({"title": title, "price": price, "rating": rating})

print(books)
