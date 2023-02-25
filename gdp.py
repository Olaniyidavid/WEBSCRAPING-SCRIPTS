#WEBSCRAPING THE GDP OF WEST AFRICAN COUNTRIES FROM MACROTRENDS
import requests

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#BENIN REPUBLIC
ben_data = pd.DataFrame(columns=["Date", "BRE"])
benin = requests.get("https://www.macrotrends.net/countries/BEN/benin/gdp-gross-domestic-product")
soup = BeautifulSoup(benin.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    ben_data = ben_data.append({"Date":date, "BRE":gdp}, ignore_index=True)
#BURKINA FASO
bfa_data = pd.DataFrame(columns=["BFA"])
bfa = requests.get("https://www.macrotrends.net/countries/BFA/burkina-faso/gdp-gross-domestic-product")
soup = BeautifulSoup(bfa.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    bfa_data = bfa_data.append({"BFA":gdp}, ignore_index=True)
#CABO VERDE
cpv_data = pd.DataFrame(columns=["CPV"])
cpv = requests.get("https://www.macrotrends.net/countries/CPV/cabo-verde/gdp-gross-domestic-product#:~:text=Cabo%20Verde%20gdp%20for%202021,a%2011.12%25%20increase%20from%202017.")
soup = BeautifulSoup(cpv.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    cpv_data = cpv_data.append({"CPV":gdp}, ignore_index=True)
#GAMBIA
gmb_data = pd.DataFrame(columns=["GMB"])
gmb = requests.get("https://www.macrotrends.net/countries/GMB/gambia/gdp-gross-domestic-product")
soup = BeautifulSoup(gmb.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    gmb_data = gmb_data.append({"GMB":gdp}, ignore_index=True)
#GHANA
gha_data = pd.DataFrame(columns=["GHA"])
gha = requests.get("https://www.macrotrends.net/countries/GHA/ghana/gdp-gross-domestic-product")
soup = BeautifulSoup(gha.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    gha_data = gha_data.append({"GHA":gdp}, ignore_index=True)
#GUINEA
gue_data = pd.DataFrame(columns=["GUE"])
gue = requests.get("https://www.macrotrends.net/countries/GIN/guinea/gdp-gross-domestic-product#:~:text=Guinea%20gdp%20for%202021%20was,a%2014.84%25%20increase%20from%202017.")
soup = BeautifulSoup(gue.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    gue_data = gue_data.append({"GUE":gdp}, ignore_index=True)
#GUINEA BISSAU
gueb_data = pd.DataFrame(columns=["GUEB"])
gueb = requests.get("https://www.macrotrends.net/countries/GNB/guinea-bissau/gdp-gross-domestic-product")
soup = BeautifulSoup(gueb.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    gueb_data = gueb_data.append({"GUEB":gdp}, ignore_index=True)
#LIBERIA
lib_data = pd.DataFrame(columns=["LIB"])
lib = requests.get("https://www.macrotrends.net/countries/LBR/liberia/gdp-gross-domestic-product#:~:text=Liberia%20gdp%20for%202021%20was,a%200.95%25%20increase%20from%202017.")
soup = BeautifulSoup(lib.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    lib_data = lib_data.append({"LIB":gdp}, ignore_index=True)
#MALI
mali_data = pd.DataFrame(columns=["MALI"])
mali = requests.get("https://www.macrotrends.net/countries/MLI/mali/gdp-gross-domestic-product")
soup = BeautifulSoup(mali.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    mali_data = mali_data.append({"MALI":gdp}, ignore_index=True)
#MAURITANIA
mta_data = pd.DataFrame(columns=["MTA"])
mta = requests.get("https://www.macrotrends.net/countries/MRT/mauritania/gdp-gross-domestic-product")
soup = BeautifulSoup(mta.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    mta_data = mta_data.append({"MTA":gdp}, ignore_index=True)
#NIGER
nig_data = pd.DataFrame(columns=["NIG"])
nig = requests.get("https://www.macrotrends.net/countries/NER/niger/gdp-gross-domestic-product#:~:text=Niger%20gdp%20for%202021%20was,a%2014.52%25%20increase%20from%202017.")
soup = BeautifulSoup(nig.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    nig_data = nig_data.append({"NIG":gdp}, ignore_index=True)
#NIGERIA
ngr_data = pd.DataFrame(columns=["NGR"])
ngr = requests.get("https://www.macrotrends.net/countries/NGA/nigeria/gdp-gross-domestic-product")
soup = BeautifulSoup(ngr.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    ngr_data = ngr_data.append({"NGR":gdp}, ignore_index=True)
#SENEGAL
sen_data = pd.DataFrame(columns=["SEN"])
sen = requests.get("https://www.macrotrends.net/countries/SEN/senegal/gdp-gross-domestic-product")
soup = BeautifulSoup(sen.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    sen_data = sen_data.append({"SEN":gdp}, ignore_index=True)
#SIERRA LEONE
sln_data = pd.DataFrame(columns=["SLN"])
sln = requests.get("https://www.macrotrends.net/countries/SLE/sierra-leone/gdp-gross-domestic-product")
soup = BeautifulSoup(sln.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    sln_data = sln_data.append({"SLN":gdp}, ignore_index=True)
#TOGO
togo_data = pd.DataFrame(columns=["TOGO"])
togo = requests.get("https://www.macrotrends.net/countries/TGO/togo/gdp-gross-domestic-product")
soup = BeautifulSoup(togo.text,"html.parser")
tables = soup.find_all('table') 
for row in tables[1].tbody.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    gdp = col[1].text
    togo_data = togo_data.append({"TOGO":gdp}, ignore_index=True)

gdpdata = pd.concat([ben_data, togo_data,bfa_data,cpv_data,gmb_data,gha_data,gue_data,gueb_data,lib_data,mali_data,mta_data,nig_data,ngr_data,sen_data,sln_data], axis=1)

countrykey = {"Key":["BRE","BFA","CPV","GMB","GHA","GUE","GUEB","LIB","MALI","MTA","NIG","NGR","SEN","SLN","TOGO"],"Name":["Benin", "Burkina Faso", "Cape Verde", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", "Mali", "Mauritania", "Niger", "Nigeria", "Senegal", "Sierra Leone", "Togo"]}

key = pd.DataFrame(countrykey)
