#test scraper with Beautiful soup
import requests
from bs4 import BeautifulSoup


url = "coltongene.co"
r = requests.get(url)



r.content 

#print r.content

soup = BeautifulSoup(r.content, "html.parser")

print soup.prettify()

soup.find_all("a")

for link in soup.find_all("a"):
	print link.get("href")
	print link.text