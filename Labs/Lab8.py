

import re
import requests
from bs4 import BeautifulSoup

def get_inline_styles(soup):
    inline_styles = []
    for tag in soup.find_all(style=True):
        inline_styles.append(tag['style'])
    for style_tag in soup.find_all('style'):
        inline_styles.append(style_tag.string)
    return inline_styles

def extract_colors_from_css(css):
    colors = set()
    color_pattern = re.compile(r'(#[0-9A-Fa-f]{3,8})|rgba?\s*\([^)]+\)|hsla?\s*\([^)]+\)')
    for match in color_pattern.finditer(css):
        colors.add(match.group(0))
    return colors

def scrape_css_colors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    css_styles = get_inline_styles(soup)
    colors = set()
    
    for css in css_styles:
        css_colors = extract_colors_from_css(css)
        colors.update(css_colors)

    return colors

if __name__ == "__main__":
    url = input("Enter the URL to scrape CSS colors: ")

    try:
        colors = scrape_css_colors(url)
        print(f"Colors found on {url}:")
        for color in colors:
            print(color)
    except Exception as e:
        print(f"Error: {e}")

''' Example output:        
        
Colors found on https://www.w3schools.com/:
#E7E9EB
#777
#1d2a35
#f1f1f1
#FFF4A3
#F3ECEA
#000
#FFC0C7
#ED594A
#059862
#D9EEE1
#fff080
#fff
#38444d
#666
#FDD800
#e3e6e8
#eee
#e2e3e9
#ffffff
#282A35
#04AA6D
#232434
#bbb
#rgb(21,32,43)
#04aa6b
#96D4D4
#ddd
#ffb3bb
#ffccd1
#ffecee
#5AC05A

