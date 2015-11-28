#test for weather.com scraper -  attempt to scrape the 10 day forcast  key 238c1df7f1f3c89a
'''
import requests
import urllib2
from bs4 import BeautifulSoup

url = "http://www.wunderground.com/q/zmw:98004.1.99999?sp=KWABELLE53"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

#organize = soup.prettify()

#print organize.encode('UTF-8')


links = soup.find_all('h2')

for link in links:
	print link.get("title")
	print link.text
'''

import urllib2
import json



def weatherCheck(city):
	# f = urllib2.urlopen('http://api.wunderground.com/api/238c1df7f1f3c89a/forecast/geolookup/conditions/q/WA/Bellevue.json')

	if (city == "bellevue"):
		f = open('C:/Users/Jigesh/Documents/python/bellevue.json')
		# f = urllib2.urlopen('http://api.wunderground.com/api/238c1df7f1f3c89a/forecast/geolookup/conditions/q/WA/Bellevue.json')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		location = parsed_json['location']['city']
		lat =  parsed_json['location']['lat']
		lon =  parsed_json['location']['lon']
		test = parsed_json['forecast']
		damnitjig = parsed_json['location']['nearby_weather_stations']['pws']['station'][0]

		return damnitjig


cityChoice = "bellevue"

print weatherCheck(cityChoice)
