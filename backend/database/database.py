import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

class Database:

	def __init__(self, db_filename=os.path.join(current_dir, "database.db")):
		self.db_filename = db_filename
		self.connection = sqlite3.connect(self.db_filename)
	
	# R FROM CRUD
	def r_list(self, query_string, query_parameters=[]):
		cursor = self.connection.cursor()
		cursor.execute(query_string, query_parameters)
		column_names = list(map(lambda c: c[0], cursor.description))
		results = cursor.fetchall()
		self.connection.commit()
		cursor.close()
		return [dict(zip(column_names, results[i])) for i in range(len(results))]
	
	# R FROM CRUD
	def r_item(self, query_string, query_parameters=[]):
		cursor = self.connection.cursor()
		cursor.execute(query_string, query_parameters)
		column_names = list(map(lambda c: c[0], cursor.description))
		results = cursor.fetchone()
		self.connection.commit()
		cursor.close()
		return dict(zip(column_names, results))
	
	# CUD FROM CRUD
	def cud(self, query_string, query_parameters=[]):
		cursor = self.connection.cursor()
		cursor.execute(query_string, query_parameters)
		self.connection.commit()
		cursor.close()