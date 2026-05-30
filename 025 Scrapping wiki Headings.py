"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL= "https://www.scrapethissite.com/pages/"

def get_h2_headers(url):
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status() # Check if the request was successful
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    p_tags=soup.find_all('p')
    print(p_tags)
    headers = []
    for tag in p_tags:
        headers.append(tag.get_text().strip())
    return headers

get_h2_headers(URL)
