"""
Before starting, you need to create a database in postgres with the same name as in the config ("db_name")
To create a database use -> CREATE DATABASE {database name};
"""
db_config: dict[str, str] = {
	'db_name': 'SOME DB NAME',
	'user': 'USER',
	'password': 'PASS',
	'host': 'localhost'
}
