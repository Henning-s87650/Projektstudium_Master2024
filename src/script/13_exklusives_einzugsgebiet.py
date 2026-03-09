#selbsterstellt

#Import der notwendigen Bibliotheken
import pandas as pd
from src.core.dbparam import connection
from src.core.queries import SQL_QUERIES

#Abfragen des zugehörigen SQL-Statements aus der Datei "queries.py"
query = SQL_QUERIES['EXKLUSIVES_EINZUGSGEBIET']

#Einlesen der Ausgabetabelle laut SQL-Statement in einen DataFrame, unter Angabe der Datenbankverbindung
with connection() as conn:
    df = pd.read_sql(query, conn)

#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Die Geburtstage der Mitarbeiter - sortiert nach Monat und Tag:\n")
print(df)

#vielleicht nochmal testen, ob plotten möglich -> wäre ultimativer Test für komplexe Abfrage mit Geodaten und gleichzeitiger Darstellung