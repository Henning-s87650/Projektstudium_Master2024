# abgeleitet von MS SQL 2 - Verwaltung geografischer Informationen - Aufgabe 11

# Import der notwendigen Bibliotheken
import pandas as pd
import geopandas as gpd
from shapely import wkb
import matplotlib.pyplot as plt

from src.core.dbparam import connection
from src.core.queries import SQL_QUERIES

# Abfragen des zugehörigen SQL-Statements aus der Datei "queries.py"
query = SQL_QUERIES['SHOPS_BUNDESLAENDER']

# Einlesen der Ausgabetabelle unter Verwendung des Kontextmanagers
with connection() as conn:
    df = pd.read_sql(query, conn)

# Interpretation der Geometriedaten mithilfe von Shapely
df["Flaeche"] = df["Flaeche_WKB"].apply(wkb.loads)

# Entfernen der temporären WKB-Spalte
df.drop(columns=["Flaeche_WKB"], inplace=True)

# Erstellen des GeoDataFrames unter Angabe der Geometriespalte
gdf = gpd.GeoDataFrame(df, geometry="Flaeche")

# Aufsplitten des GeoDataFrames in zwei Teilmengen:
# Bundesländer und Shops
gdf_bl   = gdf[gdf["Typ"] == "Bundesland"]
gdf_shop = gdf[gdf["Typ"] == "Shop"]

# Visualisierung der Geodaten (Bundesländer zuerst, danach Shops)
ax = gdf_bl.plot(edgecolor="black", facecolor="lightgrey")
gdf_shop.plot(ax=ax)
plt.show()