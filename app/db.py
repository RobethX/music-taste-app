import sqlite3

from flask import g, current_app

def get_db():
	"""Connect to the database"""
	if "db" not in g:
		g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
		g.db.row_factory = sqlite3.Row

	return g.db

def close_db():
	"""Close the connection to the database"""
	db = g.pop("db", None)
	if db is not None:
		db.close()

def init_db():
	"""Clear existing data and create new tables from schema"""
	db = get_db()

	with current_app.open_resource("schema.sql") as f:
		db.executescript(f.read().decode("utf8"))

def init_app(app):
	"""Register database functions with Flask app"""
	app.teardown_appcontext(close_db)
	#app.cli.add_command(init_db)