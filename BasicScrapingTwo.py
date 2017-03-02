# Locating elements using Xpath is a better option
# Here we are using Xpath to fetch out element data
# Other elements will be similar to last module

# Basic constructs used in Xpath
# / -> Root Element ,, @ -> Attribute ,, // ->  desendent + elemnent itself ,, [c] -> c =condition(as price>110)
#



#Request for hitting url
import requests
from lxml import html


#Change below url to HIT
url = "https://doc.scrapy.org/en/latest/"

#Hitting Request and fetching response | Rate determining Step [Blocking call] [Needs to be threaded]
req = requests.get(url)


#Printing Response Text
#print ("URL Request Response - "+req.text)

#Fetching HTML doc from text String
doc=html.fromstring(req.text)


#-------------------Using absolute path to fetch data --------------------------#

title=doc.xpath('/html/head/title/text()')[0]
print("Doc. Title -> "+title)


#Fetching document header using Abs.
heading=doc.xpath('/html/body/div/section/div/div/div/div/div/h1/text()')[0]
print("Doc. Heading absolute -> "+heading)


#-------------------------------- Accessing elements using relative path ------------------------------------#


#Fetching document header using Abs.
headingR=doc.xpath('//h1/text()')[0]
print("Doc. Heading relative -> "+headingR)



#Fetching all List text data
paraListRelative=doc.xpath('//li/text()')
for text in paraListRelative:
    print(text)
print("\n\n\n\n\nHeaders :\n ")

#Fetching all ul by specifying class name and printing h2 data
header2ListRelative=doc.xpath("//div[@class='section']/h2/text()")
for text in header2ListRelative:
    print(text)

#Accessing particular ID
header2ListRelative=doc.xpath("//div[@id='basic-concepts']/h2/text()")[0]
print("ID data - "+header2ListRelative)


#Searching some class [In-case multiple classes]
searchRelative=doc.xpath("//div[contains(@class,'compound')]")[0]
print("Search Data - "+searchRelative.text)

#Search for given element in HTML doc & then
#fetch some attribute from that element [as fetching href from <a> tag]
fetchAttribute=doc.xpath("//a[contains(@class,'reference')]/@href")
print(fetchAttribute)
