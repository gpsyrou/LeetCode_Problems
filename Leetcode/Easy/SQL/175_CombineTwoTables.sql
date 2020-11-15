/* 
175. Combine Two Tables

Write your T-SQL query statement below */
SELECT Person.[FirstName], Person.[LastName], Address.[City], Address.[State]
FROM Person 
LEFT JOIN Address
ON Person.[PersonId] = Address.[PersonId]
