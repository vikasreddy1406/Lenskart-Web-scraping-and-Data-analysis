# Lenskart Web Scraping and Data Analysis Project

## Introduction
Lenskart, a leading eyewear retailer in India, aims to enhance its operational efficiency by centralizing product information, pricing details, customer reviews, and improving customer and employee databases. The objective of this project is to increase sales, identify underperforming stores, and visualize sales trends over the years. This repository outlines the steps taken in data extraction, transformation, and visualization using various tools and methodologies.

## ETL (Extract, Transform, Load) Process
### Extract
- **Scraping Data**: Used Python and BeautifulSoup to scrape the Lenskart website for detailed information on eyeglasses, sunglasses, and contact lenses, along with pricing details, discounts, promotions, and store locations in India.
- **Client Data**: Obtained additional data, including transaction files and customer details, from the client.

### Transform
- **Data Cleaning**: Cleaned the extracted and client-provided data to remove null values and duplicates, ensuring consistency and accuracy.
- **Data Structuring**: Structured the data to facilitate easy loading into the database, ensuring proper data types, removing inconsistencies, and formatting data as per requirements.

### Load
- **Azure Blob Storage**: Uploaded the cleaned data to Azure Blob Storage using `BlobServiceClient` from `azure.storage.blob` in Python.
- **Azure Data Factory**: Used Azure Data Factory to ingest the data into a SQL database, ensuring data integrity and consistency during the loading process.

## Data Models
The project involves several data models to store and process the necessary information:

### Orders
- **Columns**: `order_id`, `transaction_id`, `customer_id`, `product_id`, `store_id`, `quantity`, `order_date`, `payment_method`
- Contains transaction details for each order.

### Products
- **Columns**: `ProductID`, `ProductImageURL`, `ProductURL`, `ProductColor`, `ProductSize`, `ProductWidth`, `MarketPrice`, `LenskartPrice`, `ProductBrandName`, `ProductRating`, `TotalRatings`
- Stores details about each product available on Lenskart.

### StoreDetails
- **Columns**: `number`, `Name`, `Address`, `Location`, `Timings`, `PhoneNumber`, `Rating`, `NumberofRatings`
- Information about each Lenskart store in India.

### CustomerDetails
- **Columns**: `customer_id`, `first name`, `last name`, `email`, `DOB`, `address`, `city`, `region`
- Details about Lenskart customers.

## Data Presentation
### Azure SQL Database
- Wrote SQL queries for the KPIs to get the output data.

### Connecting to Azure SQL Database
- Connected Power BI to the Azure SQL Database to access the data.

### Creating Visualizations
- Used DAX queries to generate visualizations for the specified KPIs.
- Created interactive dashboards to display sales trends, top-performing products, store comparisons, and customer insights.

## KPI Visualizations
- Compared the count of sales transactions over a period between the current year and the previous year.
- Analyzed average transaction value by payment type.
- Compared current year revenue to the previous year.
- Identified the top 10 products by revenue in the last 30 days.
- Calculated the average unit purchase of products in the last 30 days.
- Listed the top 15 highly rated products by their brand name.

## Architecture
![image](https://github.com/vikasreddy1406/Lenskart-WebScraping/assets/96761217/081ace57-b7ed-43d8-83c4-e1037f31898e)


## Power BI Visualizations
- Compared the count of sales transactions over a period between the current year and the previous year.
  ![image](https://github.com/vikasreddy1406/Lenskart-WebScraping/assets/96761217/6e66bd8f-529a-420a-bd67-c039e8ceab98)

- Analyzed average transaction value by payment type.
  ![image](https://github.com/vikasreddy1406/Lenskart-WebScraping/assets/96761217/aac744db-39f2-444c-94ff-08d69af1074c)

- Compared current year revenue to the previous year.
  ![image](https://github.com/vikasreddy1406/Lenskart-WebScraping/assets/96761217/06286da1-b213-4011-a3cb-eff59d50d77c)

- Identified the top 10 products by revenue in the last 30 days.
  ![image](https://github.com/vikasreddy1406/Lenskart-WebScraping/assets/96761217/3b491f6d-4141-40be-b425-4a1796038e2a)

- Calculated the average unit purchase of products in the last 30 days.
  ![image](https://github.com/vikasreddy1406/Lenskart-WebScraping/assets/96761217/a8b1b988-0ec7-4658-99c3-592496a0f581)

- Listed the top 15 highly rated products by their brand name.
  ![image](https://github.com/vikasreddy1406/Lenskart-WebScraping/assets/96761217/eef46173-c573-4b27-b0d2-b6ac497bb2fd)


## Conclusion
The project successfully streamlined Lenskart's data management process, providing valuable insights into sales performance and customer behavior. By leveraging Python for data extraction, Azure for data storage and transformation, and Power BI for visualization, Lenskart can now make informed decisions to boost sales and improve overall operational efficiency.

