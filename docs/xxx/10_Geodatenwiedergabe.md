## 5.2.4 Python-Anwendungen für Geodatenwiedergabe

Die Programme zur Visualisierung von Geodaten folgen grundlegend dem gleichen Aufbau wie die
Skripte zur Sachdatenwiedergabe. Ergänzt wird dieser Ablauf um die Aufbereitung binärer Geometriedaten
sowie deren Darstellung.

### Ablaufstruktur der Geodaten-Skripte

Die Verarbeitung gliedert sich in klar getrennte Phasen:

1. **Auswahl der SQL-Anweisungen**  
   über Schlüssel aus dem Dictionary `SQL_QUERIES` in `queries.py`.

2. **Aufbau der Datenbankverbindung**  
   über den in `dbparam.py` implementierten Kontextmanager `connection()`.

3. **Einlesen der Abfrageergebnisse**  
   mit `pandas.read_sql()` in DataFrames.

4. **Laden der Geometriedaten**  
   Dekodierung der WKB-Geometrien mit Shapely.

5. **Aufbereiten der DataFrames**  
   Entfernen temporärer Spalten für die Ausgabe.

6. **Erzeugung von GeoDataFrames**  
   aus den DataFrames mithilfe von GeoPandas.

7. **Ausgabe der Daten** <br>
    Ausgabe des GeoDataFrames in der Konsole und Darstellung der Geodaten mit Matplotlib

### Beispiel: `07_geometrien_darstellen.py`

**Anmerkung:** Die zugrundeliegende Aufgabe für dieses Skript (*MS SQL 2 - Aufgabe 9*) verlangt die Darstellung der räumlichen Ergebnisse aller Bundesländer sowie separat für Sachsen. Daher sind zwei SQL-Abfragen integriert und alle Arbeitsschritte werden doppelt ausgeführt.

Das folgende Skript demonstriert die Umsetzung dieses Ansatzes:

```python
#abgeleitet von MS SQL 2 - Verwaltung geografischer Informationen - Aufgabe 9

# Import der notwendigen Bibliotheken
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

from shapely import wkb
from dbparam import connection
from queries import SQL_QUERIES

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
```

Da bis zur Arbeitsweise des `with`-Blocks bereits alles im vorhergehenden Kapitel *5.2.3 Python-Anwendungen für die Sachdatenwiedergabe* erläutert wurde, geht dieses Kapitel nur auf die darauffolgenden Schritte ein.

Die Interpretation der Geometriedaten erfordert mehrere Teilschritte. Wie bereits im Kapitel *Datenbankmigration* erwähnt liegen die Geometrien in der neuen Datenbank im SpatiaLite-BLOB-Format vor. Die in diesem Skript genutzte Funktion `wkb.loads()` kann dieses jedoch nicht interpretieren und erwartet das WKB-Format nach OGC-Standard. Daher sind die  zugrundeliegenden SQL-Statements `INHALT_GEOGRAFIE` und `SELECT_SACHSEN` folgendermaßen angepasst (demonstriert am Beispiel `INHALT_GEOGRAFIE`):

```sql
SELECT
    Land_ID,
    Bundesland,
    Region,
    Staat,
    ST_AsBinary(Flaeche) AS Flaeche_WKB
FROM Geografie;
```

Die dort genutzte Funktion `ST_AsBinary()` dekodiert das SpatiaLite-BLOB-Format und speichert es als OGC-Standard-konformes WKB-Format in einer neuen Spalte `Flaeche_WKB`. Diese Spalte **existiert nur im Abfrageergebnis** nicht in der Datenbank. Im Python-Skript wird darauf nun die Shapely-Funktion `wkb.loads()` angewendet.

```python
# Interpretation der Geometriedaten mithilfe von Shapely
df1["Flaeche"] = df1["Flaeche_WKB"].apply(wkb.loads)
df2["Flaeche"] = df2["Flaeche_WKB"].apply(wkb.loads)
```

In den DataFrames wird eine neue Spalte `Flaeche` angelegt, in welcher die Werte enthalten sind, die sich durch die Anwendung von `wkb.loads()` auf die Werte der Spalte `Flaeche_WKB` ergeben. `Flaeche` ist somit eine reine Shapely-Geometriespalte. 

Da die zugrundeliegende Aufgabe für dieses Skript (*MS SQL 2 - Aufgabe 9*) die Fragestellung *Wie sieht die Definition der Flaeche im WKT-Format aus?* enthält, wird anschließend für eine saubere Ausgabe des DataFrames die Spalte `Flaeche_WKB` entfernt. Bei dessen Darstellung sollen nur *Land_ID*, *Bundesland*, *Region*, *Staat* und *Flaeche* sichtbar sein. Streng genommen handelt es sich bei den Werten in der Spalte `Flaeche` nicht um ein WKT-Format. Doch die Shapely-Geometriewerte werden dem OGC-Format so stark nachempfunden, dass es eine genauso gute Lesbarkeit gewährleistet.

```python
# Entfernen der temporären WKB-Spalte
df1.drop(columns=["Flaeche_WKB"], inplace=True)
df2.drop(columns=["Flaeche_WKB"], inplace=True)
```

Letztendlich erfolgt das Erstellen von GeoDataFrames für die spätere Darstellung der Geometrien. Die Eingabeparameter sind die jeweiligen DataFrames sowie die Spalte `Flaeche`, welche die geographischen Informationen enthält.

```python
# Erstellen von GeoDataFrames
gdf1 = gpd.GeoDataFrame(df1, geometry="Flaeche")
gdf2 = gpd.GeoDataFrame(df2, geometry="Flaeche")
```

Wie bereits aus dem voherigen Kapitel bekannt, werden die DataFrames in der Konsole ausgegeben.

```python
# Ausgabe der DataFrames im Terminal
print("\nInhalt der Tabelle Geografie:\n")
print(df1)

print("\nInhalt der Tabelle Geografie – Bundesland Sachsen:\n")
print(df2)
```

Das Ergebnis sieht folgendermaßen aus:

```python
Inhalt der Tabelle Geografie:

   Land_ID              Bundesland         Region          Staat                                            Flaeche
0       01                 Sachsen            Ost    Deutschland  MULTIPOLYGON (((12.877999000000102 51.67269900...
1       02                  Bayern            Süd    Deutschland  MULTIPOLYGON (((10.133860000000084 50.54999899...
2       03                Saarland           West    Deutschland  MULTIPOLYGON (((7.037959999999998 49.643380000...
3       04     Nordrhein-Westfalen           West    Deutschland  MULTIPOLYGON (((8.666279000000088 52.525281000...
4       05       Baden-Württemberg            Süd    Deutschland  MULTIPOLYGON (((9.650460000000066 49.776340000...
5       06         Rheinland-Pfalz           West    Deutschland  MULTIPOLYGON (((7.799629000000095 50.943019999...
6       07           Niedersachsen           West    Deutschland  MULTIPOLYGON (((8.48805496452138 53.9254149916...
[...]

Inhalt der Tabelle Geografie – Bundesland Sachsen:

  Land_ID Bundesland Region        Staat                                            Flaeche
0      01    Sachsen    Ost  Deutschland  MULTIPOLYGON (((12.877999000000102 51.67269900...
```


Den letzten Schritt bildet das Darstellen der Geometrien. Zuerst wird die Funktion `plot()` der Matplotlib-Schnittstelle `pyplot` verwendet, um aus den Geometriedaten grafische Objekte zu erzeugen. Anschließend erfolgt mit der Verwendung der `show()` die Darstellung der Grafiken.

```python
# Visualisierung der Geodaten
gdf1.plot()
gdf2.plot()
plt.show()
```

Das Ausführen des Skriptes öffnet zwei separate Fenster, in denen die Geometrien der jeweiligen GeoDataFrames dargestellt werden:

![Ergebnisse der Geodatenwiedergabe](media/Plots_Geodaten.png)

**Anmerkung:** Die Laufzeit des Skriptes wird erst mit dem Schließen dieser Fenster beendet.

