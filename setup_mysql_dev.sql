-- Create a new database and user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd' IF NOT EXISTS;
GRANT ALL PRIVILEGES ON `hbtn_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `preformance_schema` TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
