-- Create a new MySQL user 'user_0d_1'@'localhost' with the specified password 'user_0d_1_pwd', if the user doesn't already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables to the user 'user_0d_1' when connecting from the local machine ('localhost').
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';

-- Refresh the MySQL privilege cache to apply the recent privilege changes.
FLUSH PRIVILEGES;
