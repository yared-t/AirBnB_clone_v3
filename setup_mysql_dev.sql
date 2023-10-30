-- Creating database with hbnb_dev_db by yared and mike
-- inorder to create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- user created if doesnt exit
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- pass word set 
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- giving privaledge
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- privalege
FLUSH PRIVILEGES;
