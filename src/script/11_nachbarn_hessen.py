#abgeleitet von MS SQL 2 - Verwaltung geografischer Informationen - Aufgabe 13s

#Import der notwendigen Bibliotheken
import pandas as pd
from src.core.dbparam import connection
from src.core.queries import SQL_QUERIES

#Verbindungsaufbau mit der Datenbank durch Abrufen der Funktion "connection" aus der Datei "dbparam.py"
query = SQL_QUERIES['NACHBAR_HESSEN']

#Einlesen der Ausgabetabelle laut SQL-Statement in einen DataFrame, unter Angabe der Datenbankverbindung
with connection() as conn:
    df = pd.read_sql(query, conn)

#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Abstände zwischen den Shops:\n")
print(df)