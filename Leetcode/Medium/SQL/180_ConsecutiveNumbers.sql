/* 
180. Consecutive Numbers

Write a SQL query to find all numbers that appear at least three times consecutively.
*/
SELECT DISTINCT LOG1.[NUM] AS [ConsecutiveNums]
FROM 
    Logs AS LOG1, Logs AS LOG2, Logs AS LOG3
WHERE 
    LOG1.[ID]  = LOG2.[ID] - 1
AND LOG2.[ID]  = LOG3.[ID] - 1
AND LOG1.[NUM] = LOG2.[NUM]
AND LOG2.[NUM] = LOG3.[NUM]
