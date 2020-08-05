/* 
176. Second Highest Salary

Write a SQL query to get the second highest salary from the Employee table.


*/
SELECT MAX(SALARY) AS [SecondHighestSalary]
FROM (SELECT SALARY , DENSE_RANK() OVER(ORDER BY SALARY DESC) AS SALRANK FROM Employee ) AS A
WHERE SALRANK = 2
