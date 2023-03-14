-- computes the score average of all records
ALTER TABLE second_table
ADD COLUMN average INT;
UPDATE second_table
SET average = AVG(score);
