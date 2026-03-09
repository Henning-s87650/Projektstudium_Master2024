#abgeleitet von MS SQL 1 - Aufbau einer OLTP-Datenbank im MS SQL Server - Aufgabe 8

#Import der notwendigen Bibliotheken
import pandas as pd
from src.core.dbparam import connection
from src.core.queries import SQL_QUERIES

#Abfragen des zugehörigen SQL-Statements aus der Datei "queries.py"
query = SQL_QUERIES['GEBURTSTAGSKALENDER']

#Einlesen der Ausgabetabelle laut SQL-Statement in einen DataFrame, unter Angabe der Datenbankverbindung
with connection() as conn:
    df = pd.read_sql(query, conn)

#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Die Geburtstage der Mitarbeiter - sortiert nach Monat und Tag:\n")
print(df)
