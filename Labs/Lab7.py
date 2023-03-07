import requests
from bs4 import BeautifulSoup

# Send request to website
response = requests.get("https://www.example.com")

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extract title of the website
title = soup.find("title").text
print(f"Website Title: {title}")

# Extract all the links on the page
links = [link.get("href") for link in soup.find_all("a")]
print("Links: ", links)

# Extract all the headings on the page
headings = [heading.text for heading in soup.find_all(["h1", "h2", "h3"])]
print("Headings: ", headings)
