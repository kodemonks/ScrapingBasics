# This module fetches a URL and searches for given content in that Url response
# Here we are using requests and BeautifulSoup libraries for Scraping
# It's a simple module which shows Scraping basics

#Request for hitting url
import requests
#BeautifulSoup Object for parsing result
from bs4 import BeautifulSoup


#Change below url to HIT
url = "http://www.example.com"

#Hitting Request and fetching response | Rate determining Step [Blocking call] [Needs to be threaded]
req = requests.get(url)


#Printing Response Text
print ("URL Request Response - "+req.text)


# Creating BeautifulSoup Object | Here specify type of parser to be used
# Available options are  - html.parser, html5lib, xml, lxml

soup=BeautifulSoup(req.text,"html.parser")


#Prettified Output
print(soup.prettify())


#Fetching title value | Parsing
print("Site title - "+soup.title.string)


#Fetching all a tags | Change value to fetch different element tags
print(soup.findAll('a'))




#Searching BeautifulSoup object for given element
#Using element name
soup.find_all("title")

#Searching element ID | change id value
soup.find_all(id='link2')

#Searching element CSS | Change CSS class value
soup.find_all("a", class_="sister")

#By Value of element | Change element value
soup.find_all(string="Elsie")






#Limiting search result
soup.find_all("a", limit=2)


#Check only for direct child, leave child of child
soup.html.find_all("title", recursive=False)



#Modifying HTML data
modifyME = soup.find("a")
print("Before modify value - "+modifyME.string)
modifyME.string=" Fake Images"
print("After modify value - "+modifyME.string)





#Encoding in BeautifulSoup - BS converts everything to Unicode using Unicode, Dammit lebrary
# To check the original encoding
original_encoding=soup.original_encoding
print(original_encoding)

#Convert Output in desirable given encoding
soup_output_encoded=soup.prettify("latin-1")
print(soup_output_encoded)


#Errors faced while parsing docs
#HTMLParser.HTMLParseError : malformed start tag | HTMLParser.HTMLParseError : malformed end tag




#We can use .parent , .children  = reach parent/child