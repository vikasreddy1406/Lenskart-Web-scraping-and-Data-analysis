SELECT 
    YEAR(order_date) AS year,
    SUM(p.LenskartPrice * o.quantity) AS revenue
FROM Orders o
JOIN Products p ON o.product_id = p.ProductID
WHERE YEAR(order_date) IN (YEAR(GETDATE()), YEAR(GETDATE()) - 1)
GROUP BY YEAR(order_date)
ORDER BY year DESC;
