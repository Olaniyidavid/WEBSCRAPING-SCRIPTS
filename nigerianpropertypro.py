#THIS CODE SCRAPES ALL THE HOUSES FOR RENT IN LAGOS ON NIGERIANPROPERTYPRO.COM
#Import all necessary libraries
import requests

from bs4 import BeautifulSoup
#SCRAPE ALL THE HOUSE DESCRIPTION ON NIGERIAN PROPERTY PRO AND SAVE INTO A FILE
file = open("Test.txt","w",encoding = "utf-8")
url = 'https://nigeriapropertycentre.com/for-rent/houses/lagos/showtype'
for page in range(1,2):
    data = requests.get(url + '?page=' + str(page))
    soup = BeautifulSoup(data.text,"html.parser")
    houses = soup.find_all('div',class_="wp-block-body")
    for house in houses:
        room = house.find('div',class_="wp-block-content clearfix text-xs-left text-sm-left")
        roo = room.find('a',href=True)
        NoOfRoom = roo.find('h4',class_="content-title").text
        Loc = house.find('div',class_="wp-block-content clearfix text-xs-left text-sm-left")
        Loca = Loc.find('address',class_="voffset-bottom-10")
        Location = Loca.find('strong').text
        r = (f"{NoOfRoom} {Location}\n")
        file.write(r)
    file.flush()
    file.close
