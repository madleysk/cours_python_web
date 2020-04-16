from flask import Flask, render_template, session, redirect, url_for, request
from markupsafe import escape
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import modules.auth as auth
import os, datetime, hashlib

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_9#y6K"G4Q0c\n\xec]/'

page_title = "REMA PRODUCTION"
headline = "Web programming with python and javascript !"
app_url = "http://localhost:5000"
dico = {"page_title":page_title,"app_url":app_url}
# sql connection
DATABASE_URL='mysql://python_user:MyPassw0rd#1@localhost/python_db' #Mysql database
SQLite_URL = 'sqlite:///database/mydb.db' # Sqlite Database

engine = create_engine(SQLite_URL)
db= scoped_session(sessionmaker(bind=engine))

"""
def main():
	with engine.connect() as connection:
		# table creation
		connection.execute("CREATE TABLE IF NOT EXISTS  t1 (id NUMBER, name TEXT)")
		# insertion
		connection.execute("INSERT INTO t1 (id,name) VALUES(1,'Madley') ")
		# selection
		result= connection.execute("SELECT name FROM t1")
		for res in result:
			print(res.name)
"""
def conn_db():
	engine = create_engine(os.getenv(DATABASE_URL))
	db= scoped_session(sessionmaker(bind=engine))

try:
	annee = datetime.datetime.now().year
	dico['annee'] = annee
except:
	dico['annee'] = "Year"

@app.route("/")
def index():
	dico['page_title'] = page_title+" - Accueil"
	isapril = verifApril()
	return render_template("layout.html",dico=dico,headline=headline)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('pseudo')
		res = db.execute("SELECT username, passwd FROM users WHERE username=:username",{"username":username}).fetchone()
		if res != None:
			if(res.username == username):
				passwd = request.form.get('passwd')
				if(auth.pass_verify(passwd,res.passwd)):
					session['username'] = username
					return redirect(username)
				else:
					return "Password incorrect"
		else:
			return "Username/Password incorrect"
	return render_template("login.html", dico=dico,headline=headline )
	    
@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/subscribe', methods=['GET','POST'])
def subscribe():
	# subsribing user
	if (request.method == "POST"):
		# Verifying path
		assert request.path == '/subscribe'
		# verifying the uniqueness of the username else process
		username = request.form.get('username')
		res = db.execute("SELECT username FROM users WHERE username=:username",{"username":username}).fetchone()
		if res:
			return 'User already exist !'
		else:
			passwd = auth.pass_hashing(request.form.get('passwd'))
			nom = request.form.get('nom')
			prenom = request.form.get('prenom')
			auth_level = request.form.get('auth_level')
			email = request.form.get('email')
			db.execute("INSERT INTO users (username,passwd,nom,prenom,auth_level,email) VALUES(:username,:passwd,:nom,:prenom,:auth_level,:email)",
				{"username":username,"passwd":passwd,"nom":nom,"prenom":prenom,"auth_level":auth_level,"email":email})
			db.commit()
			return 'Registration succeed !'
	return render_template("signup.html", dico=dico,headline=headline )
     
@app.route("/isapril")
def mars():
	isapril = verifApril()
	return render_template("main.html",dico=dico, isapril=isapril)

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	try:
		if session['username']:
			msg = 'Vous allez etre redirige dans 10 secondes.'+'<meta http-equiv="refresh" content="10;url=/">'
			return f"Hello, {name} !"+ msg
	except KeyError:
		return f"Hello, {name} !"
	return f"Hello, {name} !"

@app.route("/form", methods=["POST","GET"])
def form():
	dico['page_title'] = page_title+" - Inscription"
	if (request.method == "POST"):
		prenom = request.form.get('prenom')
		return render_template("form.html",dico=dico,headline=headline,prenom=prenom,)
	return render_template("form.html",dico=dico,headline=headline)
	
@app.route("/db_wizzard")
def db_wizzard():
	return render_template("db_wizzard.html",dico=dico,headline=headline )

def verifApril():
	now = datetime.datetime.now()
	isapril = False
	if now.month == 4:
		isapril = True
	return isapril

def create_structure():
	with open("structures.sql") as sql_file:
		cont = sql_file.read()
		db.execute(cont)
		sql_file.close()
