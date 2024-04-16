-- Create user holberton and grant access to primary/replica status of the database
CREATE USER IF NOT EXISTS 'holberton'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT SELECT, INSERT, UPDATE, REPLICATION CLIENT, REPLICATION SLAVE ON tyrell_corp.* TO 'holberton'@'localhost';

FLUSH PRIVILEGES;

