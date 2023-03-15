-- Description: Create a read-only user for the database
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS 
'usr_0d_2'@'localhost' IDENTIFIED BY 'usr_0d_2_pwd';
GRANT SELECT ON htbn_0d_2.* TO 'usr_0d_2'@'localhost';
