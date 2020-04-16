CREATE TABLE IF NOT EXISTS users(
	id Integer PRIMARY KEY AUTOINCREMENT,
	username VARCHAR(50) UNIQUE,
	email VARCHAR(100) UNIQUE,
	passwd VARCHAR(256),
	auth_level INT(3),
	nom VARCHAR(50),
	prenom VARCHAR(50)	
)