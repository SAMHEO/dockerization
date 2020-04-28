# dockerization

# Configuration

Three files are required (db_hostname, db_username, db_password)
Each file shoudl include hostname, username, or password for db

environment example for mongodb:
HOSTNAME_FILE: /run/secrets/db_hostname
MONGO_INITDB_ROOT_USERNAME_FILE: /run/secrets/db_username
MONGO_INITDB_ROOT_PASSWORD_FILE: /run/secrets/db_password
