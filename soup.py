#import function to open the url
from urllib.request import urlopen,Request

#import BeautifulSoup function
from bs4 import BeautifulSoup as soup

#url of the page to scrap the data from
url = 'https://www.jumia.co.ke/tuskys-electronics/'

#override the user-agent with Mozilla
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})


#open up a connection  by grabbing  the page and assign it to a variable
uClient = urlopen(req)
page_html = uClient.read() #read the page in raw html
uClient.close() #always close a file after reading from it

#
page_soup = soup(page_html,"html.parser")

#grab each product
containers = page_soup.findAll("div",{"class":"sku -gallery"})

for container in containers:
	brand    = container.find("span",{"class":"brand"}).text.strip()
	name     = container.find("span",{"class":"name"}).text.strip()
	myprices = container.find("span",{"class":"price-box ri"})
	newprice = myprices.find("span",{"class":"price"}).text.strip()
	oldprice = myprices.find("span",{"class":"price -old "}).text.strip()
	print("Brand:" +brand, "Name:" +name, "New Price:" +newprice, "Old Price:" + oldprice)

  