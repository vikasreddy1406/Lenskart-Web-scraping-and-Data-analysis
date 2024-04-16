import requests
from bs4 import BeautifulSoup
import pandas as pd

data={"Name":[],"Address":[],"Location":[],"Timings":[],"PhoneNumber":[],"Rating":[],"NumberofRatings":[]}

locations = [
    "Andhra Pradesh", "Andaman and Nicobar Islands", "Arunachal Pradesh", "Assam",
    "Bihar", "Chennai", "Chhattisgarh", "Dadra and Nagar Haveli", "Delhi",
    "Goa", "Gujarat","Gwalior", "Haryana", "Himachal Pradesh", "Hyderabad",
    "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
    "Madhya Pradesh", "Maharashtra", "Manipur", "Nagaland", "New Delhi"
    "Odisha", "Puducherry", "Punjab","Patna", "Rajasthan",
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal"
]


for location in locations:
  url="https://www.lenskart.com/stores/location/"+location
  headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
  r=requests.get(url,headers=headers)
  soup=BeautifulSoup(r.content,'html.parser')

  for store in soup.find_all('div',class_='StoreCard_imgContainer__P6NMN'):

    data["Location"].append(location)
    #scraping name
    name=store.find('a',{'class' : "StoreCard_name__mrTXJ"}).text
    data["Name"].append(name)
    #print(name)

    #scraping address
    address = store.find('a',{'class' : 'StoreCard_storeAddress__PfC_v'}).text
    data["Address"].append(address)

    #scraping timings
    timings = store.find('div',{'class' : 'StoreCard_storeAddress__PfC_v'}).text[7:-1]
    data["Timings"].append(timings)

    #scraping phonenumber
    phone = store.find('div',{'class' : "StoreCard_wrapper__xhJ0A"}).a.text[1:]
    data["PhoneNumber"].append(phone)

    #scraping ratings and numberofratings
    rating_container = store.find('div', {"class": 'StoreCard_storeRating__dJst3'})
    if rating_container:
        rating = rating_container.find_all('span')[1].text[1:-1]
        number_of_ratings = rating_container.find('label').text[2:-2]
    else:
        rating = None
        number_of_ratings = None

    data["Rating"].append(rating)
    data["NumberofRatings"].append(number_of_ratings)

#print(data)
df=pd.DataFrame.from_dict(data)
df.insert(0,'number', range(1, 1 + len(df)))
df.to_csv("lenskartStoresData.csv",index=False)