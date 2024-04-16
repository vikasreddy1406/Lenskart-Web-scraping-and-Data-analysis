#Lenskart product details web scraping using api

import requests
import csv

categories=["3363","3362","19623","8427","8415"]
products_list=[]

for cat in categories:
    url = "https://api-gateway.juno.lenskart.com/v2/products/category/"+cat+"?page-size=1400&page=0"
    response = requests.get(url)
    
    if response.status_code==200:
        data = response.json()  
        # print(data)
        products_data = data['result']['product_list']
        for each_product in products_data:
            products_list.append(each_product)


csv_file = "lenskart_products.csv"
csv_header = ["Product ID", "Product Image URL", "Product URL", "Product Color", "Product Size","Product Width", "Market Price", "Lenskart Price", "Product Brand Name","Product Rating","Total Ratings"]


with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_header)  
    
    
    for product in products_list:
        product_id = product.get('id')
        product_image_url = product.get('image_url')
        product_url = product.get('product_url')
        product_color = product.get('color', '')
        product_size = product.get('size', '')
        product_width = product.get('width','')
        product_brand_name = product.get('brand_name', '')
        product_rating = product.get('avgRating','')
        total_ratings = product.get('totalNoOfRatings','')
        
        
        market_price = ''
        lenskart_price = ''
        prices = product.get('prices', [])
        for price in prices:
            if price['name'] == 'Market Price':
                market_price = price['price']
            elif price['name'] == 'Lenskart Price':
                lenskart_price = price['price']
        
        writer.writerow([product_id, product_image_url, product_url, product_color, product_size, product_width, market_price, lenskart_price, product_brand_name,product_rating,total_ratings])
