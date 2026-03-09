#abgeleitet von MS SQL 1 - Aufbau einer OLTP-Datenbank im MS SQL Server - Aufgabe 8
#Beipiel zur Demonstration des Einbinden zusätzlicher SQL-Statements

#Import der notwendigen Bibliotheken
import pandas as pd
from core.dbparam import connection
from new_queries import NEW_SQL_QUERIES

#Abfragen des zugehörigen SQL-Statements aus der Datei "queries.py"
query = NEW_SQL_QUERIES['ALLES_SELEKTIEREN']

#Einlesen der Ausgabetabelle laut SQL-Statement in einen DataFrame, unter Angabe der Datenbankverbindung
with connection() as conn:
    df = pd.read_sql(query, conn)

#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Die gesamte Tabelle Mitarbeiter:\n")
print(df)