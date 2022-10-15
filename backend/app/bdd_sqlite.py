# Fichier - Classe - BddSQLite

import sqlite3
from sqlite3 import Error

# Gestionnaire de BDD SQLite
# https://python.doctor/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite

class BddSQLite:

    # Constructeur
    def __init__(self):
        self.file = 'bdd.db'
        # self.conn = None
        # self.connection()

    # Vérification de la base de donnée
    def connection(self):
        try:
            self.conn = sqlite3.connect(self.file)
            print('[BDD] Connected !')
        except Error as e:
            print('[BDD] Error !')
            print(e)
            self.close()
            return None

    # Exécuter une requète
    def getExecute(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True
        except Error as e:
            print('[BDD] Error !')
            print(e)
            self.close()
            return None

    # Récupérer plusieurs données
    def getAll(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()
        except Error as e:
            print('[BDD] Error !')
            print(e)
            self.close()
            return None

    # Récupérer une donnée
    def getOnce(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return cursor.fetchone()
        except Error as e:
            print('[BDD] Error !')
            print(e)
            self.close()
            return None

    # Récupérer le nombre de ligne
    def count(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return len(cursor.fetchall())
        except Error as e:
            print('[BDD] Error !')
            print(e)
            self.close()
            return None

    # Fermer la connexion
    def close(self):
        self.conn.close()
        print('[BDD] Closed !')
