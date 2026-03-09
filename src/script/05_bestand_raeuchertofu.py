#abgeleitet von MS SQL 2 - Verwaltung geografischer Informationen - Aufgabe 5

#Import der notwendigen Bibliotheken
import pandas as pd
from src.core.dbparam import connection
from src.core.queries import SQL_QUERIES

#Abfragen des zugehörigen SQL-Statements aus der Datei "queries.py"
query = SQL_QUERIES['BESTAND_RAEUCHERTOFU']

#Einlesen der Ausgabetabelle laut SQL-Statement in einen DataFrame, unter Angabe der Datenbankverbindung
with connection() as conn:
    df = pd.read_sql(query, conn)

#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Entfernungen zwischen den Shops und der HTW und deren Bestand an Räuchertofu:\n")
print(df)