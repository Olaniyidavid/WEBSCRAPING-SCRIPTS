#THIS CODE SCRAPES ALL THE HOUSES FOR RENT IN LAGOS ON NIGERIANPROPERTYPRO.COM
#Import all necessary libraries
import requests

from bs4 import BeautifulSoup
#SCRAPE ALL THE HOUSE DESCRIPTION ON NIGERIAN PROPERTY PRO AND SAVE INTO A FILE
propertydata = pd.DataFrame(columns=["Number of bedroom", "Location","Price"])
data = requests.get('https://nigeriapropertycentre.com/for-rent/houses/lagos/showtype').text
soup = BeautifulSoup(data,"html.parser")
houses = soup.find_all('div',class_="wp-block-body")
for house in houses:
    room = house.find('div',class_="wp-block-content clearfix text-xs-left text-sm-left")
    roo = room.find('a',href=True)
    NoOfRoom = roo.find('h4',class_="content-title").text
    Loc = house.find('div',class_="wp-block-content clearfix text-xs-left text-sm-left")
    Loca = Loc.find('address',class_="voffset-bottom-10")
    Location = Loca.find('strong').text
    Pri = house.find('div',class_="wp-block-content clearfix text-xs-left text-sm-left")
    Price = Pri.find('span',class_="pull-sm-left").text
    moreinfo = house.find('a',href = True)
   
    propertydata = propertydata.append({"Number of bedroom":NoOfRoom, "Location":Location,"Price":Price}, ignore_index=True)
