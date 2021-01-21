/*
181. Employees Earning More Than Their Managers

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
*/

WITH employees_vs_managers AS
(
    SELECT emp.[Name], emp.[Salary] , man.[Salary] AS [Manager_Salary]
    FROM Employee emp
    INNER JOIN Employee man
    ON man.ID  = emp.ManagerId
)
SELECT [Name] AS [Employee]
FROM employees_vs_managers
WHERE [Manager_Salary] < [Salary]
