SELECT Manufacturer, sales_qty, ROW_NUMBER(OVER ORDER BY sales_qty DESC) AS r
FROM (
    SELECT DISTINCT Manufacturer, COUNT(DISTINCT SalesID) AS sales_qty
    FROM Cars
    JOIN Sales USING(CarID) 
    WHERE DATE_TRUNC('month', TransDatetime) = MONTH(GETDATE())
    GROUP BY 1
) table1
WHERE r <= 3

