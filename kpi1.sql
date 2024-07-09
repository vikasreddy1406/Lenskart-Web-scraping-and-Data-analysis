-- Current Year Sales Transactions Count
SELECT YEAR(order_date) AS year, COUNT(*) AS sales_transaction_count
FROM Orders
WHERE YEAR(order_date) IN (YEAR(GETDATE()), YEAR(GETDATE()) - 1)
GROUP BY YEAR(order_date)
ORDER BY year DESC;
