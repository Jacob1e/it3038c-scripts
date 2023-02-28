import requests
from bs4 import BeautifulSoup

def vulnerability_scan(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    forms = soup.find_all('form')
    inputs = soup.find_all('input')
    scripts = soup.find_all('script')
    
    print(f"Number of forms found: {len(forms)}")
    print(f"Number of input fields found: {len(inputs)}")
    print(f"Number of scripts found: {len(scripts)}")

# Enter URL to scan
url = input("Enter URL to scan: ")

# Check if the URL is valid
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Starting vulnerability scan...")
        vulnerability_scan(url)
    else:
        print("The URL is not accessible.")
except:
    print("Invalid URL. Please enter a valid URL.")


