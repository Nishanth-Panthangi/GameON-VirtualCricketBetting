
import requests
from bs4 import BeautifulSoup
import json
import sys

#page = urllib2.urlopen('http://www.cricbuzz.com/live-cricket-scorecard/18366/wi-vs-ind-only-t20i-india-tour-of-west-indies-2017').read()
url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
url2 = "http://www.cricbuzz.com/live-cricket-scorecard/18366/wi-vs-ind-only-t20i-india-tour-of-west-indies-2017"
page = requests.get(url2)
soup = BeautifulSoup(page.text,"html.parser")
#print soup.prettify()

data = soup.findAll("div", { "class" : "cb-col cb-col-100 cb-scrd-hdr-rw" })
print data
