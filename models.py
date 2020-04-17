import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Niveau(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	niveau = db.Column(db.Integer,unique=True,nullable=False)
	description = db.Column(db.String(30),nullable=False)
	
	def __init__(self,niveau,description):
		self.niveau = niveau
		self.description = description

class Personne(db.Model):
	__tablename__ = "personnes"
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.String(60),nullable = False)
	prenom = db.Column(db.String(60),nullable = False)
	code = db.Column(db.String(30),unique=True,nullable = False)
	email =  db.Column(db.String(160),unique=True,nullable = False)
	adresse = db.Column(db.String(60),nullable = True)
	telephone = db.Column(db.String(15),nullable = True)
	niveau = db.Column(db.Integer, db.ForeignKey("niveau.niveau"),nullable= False)
	
	def __init__(self,nom,prenom,code,email,adresse,telephone,niveau):
		self.nom = nom
		self.prenom = prenom
		self.code = code
		self.email = email
		self.adresse = adresse
		self.telephone = telephone
		self.niveau = niveau

class Role(db.Model):
	__tablename__ = "roles"
	id = db.Column(db.Integer, primary_key=True)
	auth_level = db.Column(db.Integer,unique=True,nullable=False)
	role_desc = db.Column(db.String(50),nullable=False) 

	def __init__(self,auth_level,role_desc):
		self.auth_level = auth_level
		self.role_desc = role_desc

class Users(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40),unique=True,nullable = False)
	passwd = db.Column(db.String(256),nullable = False)
	auth_level = db.Column(db.Integer,db.ForeignKey("roles.auth_level"),nullable = False)
	code = db.Column(db.String(30),db.ForeignKey("personnes.code"),nullable= False)

	def __init__(self,username,passwd,auth_level,code):
		self.username = username
		self.passwd = passwd
		self.auth_level = auth_level
		self.code = code

