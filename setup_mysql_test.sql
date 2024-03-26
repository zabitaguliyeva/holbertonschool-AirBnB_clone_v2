-- A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- A new user hbnb_dev (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
ALTER USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
