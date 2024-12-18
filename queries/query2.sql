--Average Miles Traveled by Fitness Level

SELECT Fitness, AVG(Miles) as AvgMiles
FROM customer_profiles
GROUP BY Fitness
ORDER BY AvgMiles DESC;