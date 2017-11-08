from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graph

# opening up connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup - soup(page_html, "html_parser")
page.h1

#grabs each product 
containers = page_soup.findAll("div",{"class":"item-container"})


for container in containers:
    brand = container.div.div.a.img["title"]
