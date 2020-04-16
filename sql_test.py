#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os, datetime

# sql connection
DATABASE_URL='mysql://python_user:MyPassw0rd#1@localhost/python_db'
SQLite_URL = 'sqlite:///mydb.db'

engine = create_engine(SQLite_URL)

def main():
	niveaux = {"00":"N/A","01":"Premiere Annee","02":"Deuxieme Annee","03":"Troisieme Annee","04":"Quatrieme Annee","05":"Cinquieme Annee"}
	for key, val in niveaux.items():
		print(key,val)
	"""
	with engine.connect() as connection:
		# table creation
		connection.execute("CREATE TABLE IF NOT EXISTS  t1 (id NUMBER, name TEXT)")
		# insertion
		# connection.execute("INSERT INTO t1 (id,name) VALUES(1,'Madley') ")
		# selection
		result= connection.execute("SELECT * FROM users")
		for res in result:
			print(res.nom, res.prenom, res.passwd)"""

def conn_db():
	engine = create_engine(os.getenv(DATABASE_URL))
	db= scoped_session(sessionmaker(bind=engine))

if __name__ == "__main__":
	main()
