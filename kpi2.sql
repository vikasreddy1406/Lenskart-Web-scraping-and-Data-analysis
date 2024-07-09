SELECT payment_method, sum(quantity) AS avg_transaction_quantity
FROM Orders
GROUP BY payment_method;
