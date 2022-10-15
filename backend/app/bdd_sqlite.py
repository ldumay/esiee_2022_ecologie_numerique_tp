# Fichier - Classe - BddSQLite

import sqlite3
from sqlite3 import Error

# Gestionnaire de BDD SQLite
# https://python.doctor/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite

class BddSQLite:

	# Constructeur
	def __init__(self):
		self.file = 'bdd.db'
		# self.connection()

	# Vérification de la base de donnée
	def connection(self):
		try:
			self.conn = sqlite3.connect(self.file, check_same_thread=False)
			print('[BDD] Connected !')
		except Error as err:
			print('[BDD] Error !')
			print(err)
			self.close()
			return False

	# Exécuter une requète
	def getExecute(self, query):
		try:
			print("Executing query", query, flush=True)
			cursor = self.conn.cursor()
			cursor.execute(query)
			self.conn.commit()
			return True
		except Error as err:
			print('[BDD] Error !')
			print(err)
			self.close()
			return False

	# Récupérer plusieurs données
	def getAll(self, query):
		try:
			cursor = self.conn.cursor()
			cursor.execute(query)
			self.conn.commit()
			return cursor.fetchall()
		except Error as err:
			print('[BDD] Error !')
			print(err)
			self.close()
			return []

	# Récupérer une donnée
	def getOnce(self, query):
		try:
			cursor = self.conn.cursor()
			cursor.execute(query)
			self.conn.commit()
			return cursor.fetchone()
		except Error as err:
			print('[BDD] Error !')
			print(err)
			self.close()
			return False

	# Récupérer le nombre de ligne
	def count(self, query):
		try:
			cursor = self.conn.cursor()
			cursor.execute(query)
			self.conn.commit()
			rows = cursor.fetchall()
			return rows[0]
		except Error as err:
			print('[BDD] Error !')
			print(err)
			self.close()
			return False

	# Fermer la connexion
	def close(self):
		self.conn.close()
		print('[BDD] Closed !')
