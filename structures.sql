GRANT ALL PRIVILEGES ON python_db.* TO 'python_user'@'%' IDENTIFIED BY 'MyPassw0rd#1'
CREATE DATABASE IF NOT EXISTS python_db;

CREATE TABLE IF NOT EXISTS users(
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(50) UNIQUE,
	email VARCHAR(100) UNIQUE,
	passwd VARCHAR(256),
	auth_level INT(3),
	nom VARCHAR(50),
	prenom VARCHAR(50)	
)
insert into niveau (niveau,description) values (00,'Annee');
insert into niveau (niveau,description) values (01,'Annee');
insert into niveau (niveau,description) values (02,'Annee');
insert into niveau (niveau,description) values (03,'Annee');
insert into niveau (niveau,description) values (04,'Annee');
insert into niveau (niveau,description) values (05,'Annee');
insert into personnes (nom,prenom,code,email,adresse,telephone,niveau) values('Administrator','Flask admin','ADM-01','admin@flaskapp.com','Haiti','509-0000-0000',00);
insert into users (username,passwd,auth_level,code) values('admin','MonMotDePasse',9,'ADM-01');

