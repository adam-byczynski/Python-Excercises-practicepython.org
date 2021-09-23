# Ex17
# Decode a Web Page
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

def get_url(site_name):
      url = site_name
      r = requests.get(url)
      r_html = r.text
      return r_html

def find_title(html_code):
  soup = BeautifulSoup(html_code)
  title = soup.find_all(class_="balancedHeadline")
  return title
#"

def main():
      base_url = 'http://www.nytimes.com/'
      temp = get_url(base_url)
      print("Article Title:", find_title(temp))
      
      
main()