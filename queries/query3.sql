--percentage of total customers for each gender who purchase each product
SELECT 
    Product, 
    Gender, 
    COUNT(*) AS ProductCount,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_profiles WHERE Product = c.Product)) AS PercentageByGender
FROM customer_profiles c
GROUP BY Product, Gender
ORDER BY Product, PercentageByGender DESC;
