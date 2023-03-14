-- lists all records of the table second_table 
-- don't list rows without a name value
-- records should display the score and name
-- records should be listed in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
