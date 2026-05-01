-- Total expense
SELECT SUM(Amount) AS Total_Expense FROM expenses;

-- Monthly expense
SELECT strftime('%m', Date) AS Month, SUM(Amount) AS Total
FROM expenses GROUP BY Month;

-- Category wise
SELECT Category, SUM(Amount) AS Total
FROM expenses GROUP BY Category ORDER BY Total DESC;

-- Highest spending category
SELECT Category, SUM(Amount) AS Total
FROM expenses GROUP BY Category ORDER BY Total DESC LIMIT 1;