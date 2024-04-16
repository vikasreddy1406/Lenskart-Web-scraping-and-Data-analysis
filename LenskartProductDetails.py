#Lenskart Product details web scraping using Selenium

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()
url = "https://www.lenskart.com/eyeglasses.html"
driver.get(url)

# Wait for the page to load completely (you might need to adjust the wait time)
driver.implicitly_wait(90)
time.sleep(300)

page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# print(soup.prettify())

# with open("modify2.html", "w", encoding="utf-8") as f:
#   f.write(str(soup))

# with open("modify2.html","r",encoding="utf-8") as f:
#     html_doc=f.read()

# soup=BeautifulSoup(html_doc,'html.parser')

data={"Name":[],"Size":[],"Price":[],"Rating":[],"NumberofRatings":[],"ProductImageLink":[],"ProductDetailsLink":[]}

for product in soup.find_all('a',{"class":"AnchorWrapper--1smmibb iioefz"}):
    #scraping product name
    name=product.find("p",{"class":"ProductTitle--13we1dx irMDLh"}).text
    data["Name"].append(name)
    
    #scraping size
    if(product.find("span" ,{"class":"ProductSize--64lzs8 ePzHjO"})):
        size=product.find("span" ,{"class":"ProductSize--64lzs8 ePzHjO"}).text[6:]
        data["Size"].append(size)
    else:
        data["Size"].append(None)
    
    #scraping price
    
    #to extract rupee symbol
    price=product.find("span",{"class":"CurrencySpan--14uitta cGUeSf"}).text
    
    #to extract price
    price=price+product.find("span",{"class":"CurrencySpan--14uitta cGUeSf"}).find_next_sibling("span").text
    data["Price"].append(price)
    
    
    #scaping rating 
    rating=product.find("span",{"class":"NumberedRatingSpan--fq61xb buibYU"}).text
    
    if(rating!="0"):
        data["Rating"].append(rating)
        numberOfRating=product.find("span",{"class":"NumberedRatingSpan--fq61xb fNtOmf"}).text
        data["NumberofRatings"].append(numberOfRating)
    else:
        data["Rating"].append(None)
        data["NumberofRatings"].append(None)
        
    #scraping product image
    imageSrc= product.find("img", {"class": "ProductImage--xka74 HxzMC"})["src"]
    data["ProductImageLink"].append(imageSrc)
    
    #scraping product details
    productDetails=product["href"]
    data["ProductDetailsLink"].append("https://www.lenskart.com"+productDetails)
    
# print(data)

df=pd.DataFrame.from_dict(data)
df.insert(0,"number",range(1,1+len(df)))
df.to_csv("Alldetails.csv",index=False,encoding='utf-8-sig')

