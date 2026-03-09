#abgeleitet von MS SQL 2 - Verwaltung geografischer Informationen - Aufgabe 9

# Import der notwendigen Bibliotheken
import pandas as pd
import geopandas as gpd
from shapely import wkb
import matplotlib.pyplot as plt

from src.core.dbparam import connection
from src.core.queries import SQL_QUERIES

# Abfragen der zugehörigen SQL-Statements aus der Datei "queries.py"
query1 = SQL_QUERIES['INHALT_GEOGRAFIE']
query2 = SQL_QUERIES['SELECT_SACHSEN']

# Einlesen der Ausgabetabellen unter Verwendung des Kontextmanagers
with connection() as conn:
    df1 = pd.read_sql(query1, conn)
    df2 = pd.read_sql(query2, conn)

# Ab hier: keine Datenbankverbindung mehr notwendig
# Verarbeitung erfolgt vollständig im Arbeitsspeicher

# Interpretation der Geometriedaten mithilfe von Shapely
df1["Flaeche"] = df1["Flaeche_WKB"].apply(wkb.loads)
df2["Flaeche"] = df2["Flaeche_WKB"].apply(wkb.loads)

# Entfernen der temporären WKB-Spalte
df1.drop(columns=["Flaeche_WKB"], inplace=True)
df2.drop(columns=["Flaeche_WKB"], inplace=True)

# Erstellen von GeoDataFrames
gdf1 = gpd.GeoDataFrame(df1, geometry="Flaeche")
gdf2 = gpd.GeoDataFrame(df2, geometry="Flaeche")

# Ausgabe der DataFrames im Terminal
print("\nInhalt der Tabelle Geografie:\n")
print(df1)

print("\nInhalt der Tabelle Geografie – Bundesland Sachsen:\n")
print(df2)

# Visualisierung der Geodaten
gdf1.plot()
gdf2.plot()
plt.show()