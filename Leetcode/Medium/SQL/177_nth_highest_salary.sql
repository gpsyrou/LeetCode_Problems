/*
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
*/

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT MAX([Salary]) as 'getNthHighestSalary(2)'
        FROM
        (
        SELECT Salary, DENSE_RANK() OVER (ORDER BY [Salary] DESC) AS [Rank]
        FROM Employee) t
        WHERE Rank = @N
    );
END
