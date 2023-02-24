import requests
from bs4 import BeautifulSoup

print("THIS CODE RETURNS ALL THE IT ROLES ON JOBBERMAN WITH RELEVANT INFO \n")
for page in range(0,5):
    data = requests.get("https://www.jobberman.com/jobs/software-data" + '?page=' + str(page))
    soup = BeautifulSoup(data.text,"html.parser")
    jobs = soup.find_all('div',class_="mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500")
    for job in jobs:
        jo = job.find('a',class_="relative mb-3 text-lg font-medium break-words focus:outline-none metrics-apply-now text-brand-linked text-loading-animate").text
        #j = job.find('div',class_="flex items-center")
        #jo = j.find('a',class_="relative mb-3 text-lg font-medium break-words focus:outline-none metrics-apply-now text-brand-linked text-loading-animate").text
        company = job.find('p',class_="text-sm text-brand-linked").text
        #company = co.find('a',class_="text-loading-animate text-loading-animate-link",href=True).text
        d = job.find('div',class_="flex flex-row items-start items-center px-5 py-3 w-full border-t border-gray-300")
        date = d.find('p',class_="ml-auto text-sm font-normal text-gray-700 text-loading-animate").text
        i = job.find('div',class_="flex flex-wrap mt-3 text-sm text-gray-500 md:py-0")
        info = i.find('span',class_="mb-3 px-3 py-1 rounded bg-brand-opaque mr-2 text-loading-hide").text
        link = j.find('a',href=True)
        print(jo.strip())
        print(company.strip())
        print(date.strip())
        print(info.strip())
        print(f"{link.get('href')}\n")
