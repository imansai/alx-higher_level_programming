-- List all cities in California that can be found in the database hbtn_0d_usa
-- List all rows of a column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
