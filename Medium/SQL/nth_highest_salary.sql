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
