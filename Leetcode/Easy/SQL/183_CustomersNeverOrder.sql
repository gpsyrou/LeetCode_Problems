/* 
183. Customers Who Never Order

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.
*/

SELECT Customers.[Name] AS [Customers]
FROM Customers
WHERE Customers.[Id] NOT IN (SELECT DISTINCT [CustomerId] FROM Orders)
