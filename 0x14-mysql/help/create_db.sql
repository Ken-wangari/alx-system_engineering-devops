-- Create a database named tyrell_corp if it doesn't exist
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Use the tyrell_corp database
USE tyrell_corp;

-- Create a table named nexus6 if it doesn't exist
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);

-- Insert at least one entry into the nexus6 table
INSERT INTO nexus6 (name) VALUES ('Your_Entry_Name');

