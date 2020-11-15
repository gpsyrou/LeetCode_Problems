/* 1179. Reformat Department Table

Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

*/
SELECT [id],
       SUM(CASE WHEN [Month] = 'Jan' THEN [revenue] END) AS [Jan_Revenue],
       SUM(CASE WHEN [Month] = 'Feb' THEN [revenue] END) AS [Feb_Revenue],
       SUM(CASE WHEN [Month] = 'Mar' THEN [revenue] END) AS [Mar_Revenue],
       SUM(CASE WHEN [Month] = 'Apr' THEN [revenue] END) AS [Apr_Revenue],
       SUM(CASE WHEN [Month] = 'May' THEN [revenue] END) AS [May_Revenue],
       SUM(CASE WHEN [Month] = 'Jun' THEN [revenue] END) AS [Jun_Revenue],
       SUM(CASE WHEN [Month] = 'Jul' THEN [revenue] END) AS [Jul_Revenue],
       SUM(CASE WHEN [Month] = 'Aug' THEN [revenue] END) AS [Aug_Revenue],
       SUM(CASE WHEN [Month] = 'Sep' THEN [revenue] END) AS [Sep_Revenue],
       SUM(CASE WHEN [Month] = 'Oct' THEN [revenue] END) AS [Oct_Revenue],
       SUM(CASE WHEN [Month] = 'Nov' THEN [revenue] END) AS [Nov_Revenue],
       SUM(CASE WHEN [Month] = 'Dec' THEN [revenue] END) AS [Dec_Revenue]
FROM
    Department
GROUP BY [id]
