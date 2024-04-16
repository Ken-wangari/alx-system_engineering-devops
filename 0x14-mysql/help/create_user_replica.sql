-- Create user replica_user and grant access to replication
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica';

-- Grant replication privileges for specific database (tyrell_corp)
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant specific database privileges if necessary
GRANT SELECT ON tyrell_corp.* TO 'replica_user'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

