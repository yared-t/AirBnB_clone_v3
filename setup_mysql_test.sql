-- Creates the database hbnb_test_db
-- Auhtor: MikiasHailu and YaredTsige
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Sets password for user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grants privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
