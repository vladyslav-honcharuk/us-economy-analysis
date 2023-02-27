USE mrts;

SELECT 
	YEAR(period),
    SUM(value) as revenue
FROM mrts_table
WHERE Kind_of_Business = 'Electronic stores'
GROUP BY 1
HAVING SUM(value) > 0;

SELECT 
	YEAR(period),
    SUM(value) as revenue,
    Kind_of_Business
FROM mrts_table
GROUP BY 1, 3
HAVING SUM(value) > 0
ORDER BY revenue DESC;

SELECT 
	YEAR(period),
    SUM(value) AS revenue
FROM mrts_table
GROUP BY 1
HAVING SUM(value) > 0;
 