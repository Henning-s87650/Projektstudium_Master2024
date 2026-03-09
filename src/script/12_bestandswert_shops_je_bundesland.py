#abgeleitet von MS SQL 2 - Verwaltung geografischer Informationen - Aufgabe 14

#Import der notwendigen Bibliotheken
import pandas as pd
from src.core.dbparam import connection
from src.core.queries import SQL_QUERIES

#Import der notwendigen Bibliotheken
conn = connection()

#Abfragen der zugehörigen SQL-Statements aus der Datei "queries.py"
view = SQL_QUERIES['VIEW_BESTANDSWERT_BL']
query = SQL_QUERIES['BESTANSWERT_PRO_KM2']

#Aufruf der Funktion connection aus der Datei "dbparam.py" und Ausführen des Statements, um den View zu erstellen
with connection() as con:
    con.execute(view)

#Einlesen der Ausgabetabelle laut SQL-Statement in einen DataFrame, unter Angabe der Datenbankverbindung
df = pd.read_sql(query, conn)

#Schließen der Datenbankverbindung
conn.close()

#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Bestandswert pro km² (unter Nutzung von vw_Bestandswert):\n")
print(df)