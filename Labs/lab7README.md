# Lab 7 Steps

Here is how you can run a Python script that I created, which uses a plugin called Beautifulsoup4

First, install the requests module and Beautifulsoup. Make sure you have python downloaded and use powershell to run

```python
pip install requests
pip install Beautifulsoup4
```

Now, find a website you want to scrape

Enter your url into the script

Now, in Python, run the following code:

```python
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
```

This script parses the website html the extracts the title of the webpage, all links on the page and all headings on the page
