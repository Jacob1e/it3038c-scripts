import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com")

soup = BeautifulSoup(response.content, "html.parser")

title = soup.find("title").text
print(f"Website Title: {title}")

links = [link.get("href") for link in soup.find_all("a")]
print("Links: ", links)

headings = [heading.text for heading in soup.find_all(["h1", "h2", "h3"])]
print("Headings: ", headings)
