--Average Income by Marital Status

SELECT MaritalStatus, AVG(Income) AS AvgIncome
FROM customer_profiles
GROUP BY MaritalStatus
ORDER BY AvgIncome DESC;


