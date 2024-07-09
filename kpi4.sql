--Top product by total sales
SELECT TOP 1 p.ProductID, p.ProductBrandName, p.ProductColor, p.LenskartPrice, SUM(o.quantity) as total_sold
FROM Orders o
JOIN Products p ON o.product_id = p.ProductID
GROUP BY p.ProductID, p.ProductBrandName, p.ProductColor, p.LenskartPrice
ORDER BY total_sold DESC;