import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print (page.status_code)
print ( )

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
print ( )

list(soup.children)

[type(item) for item in list(soup.children)]
[soup.element.Doctype, soup.element.NavigableString, soup.element.Tag]
