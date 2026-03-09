## 5.2.3 Python-Anwendungen für die Sachdatenwiedergabe

Nach der Migration der Datenbank sowie der zentralen Bereitstellung der Verbindungslogik
(`dbparam.py`) und der SQL-Anweisungen (`queries.py`) erfolgt die eigentliche
Datenverarbeitung in entsprechenden Python-Skripten. Diese sind bewusst schlank gehalten und folgen
einem einheitlichen, reproduzierbaren Ablauf.

### Ablaufstruktur der Skripte

Jedes Skript für die tabellarische Ausgabe von Sachdaten besteht im Kern aus vier Schritten:

1. **Auswahl der SQL-Anweisung**  
    über einen Schlüssel aus dem Dictionary `SQL_QUERIES` in `queries.py`.

2. **Aufbau der Datenbankverbindung**  
    über die Funktion `connection()` aus `dbparam.py`.

3. **Ausführen der Abfrage und Einlesen der Ergebnisse**  
    über `pandas.read_sql()`, wodurch das Resultset in einen DataFrame überführt wird.

4. **Ausgabe der Ergebnisse**  
    in der Konsole der Entwicklungsumgebung.

### Beispiel: `01_geburtstagskalender.py`

Das folgende Skript demonstriert die Umsetzung dieses Ansatzes:

```python
#abgeleitet von MS SQL 1 - Aufbau einer OLTP-Datenbank im MS SQL Server - Aufgabe 8

#Import der notwendigen Bibliotheken
import pandas as pd
from dbparam import connection
from queries import SQL_QUERIES

#Abfragen des zugehörigen SQL-Statements aus der Datei "queries.py"
query = SQL_QUERIES['GEBURTSTAGSKALENDER']

#Einlesen der Ausgabetabelle laut SQL-Statement in einen DataFrame, unter Angabe der Datenbankverbindung
with connection() as conn:
    df = pd.read_sql(query, conn)

#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Die Geburtstage der Mitarbeiter - sortiert nach Monat und Tag:\n")
print(df)
```
Es beginnt mit dem Import des Moduls `pandas`, dem Kontextmanger `connection` as `dbparam.py` und dem Dictionary `SQL_QUERIES` aus `queries.py`.

```python
import pandas as pd
from dbparam import connection
from queries import SQL_QUERIES
```
Es folgt die Auswahl des für die Aufgabe benötigten SQL-Statements über dessen Schlüssel. Dieses wird in der Variable `query` gespeichert.

```python
query = SQL_QUERIES['GEBURTSTAGSKALENDER']
```
Nun folgt der im Kapitel *5.2.1 Verbindungslogik zur Datenbank (`dbparam.py`)* bereits erwähnte `with`-Block.

```python
with connection() as conn:
    df = pd.read_sql(query, conn)
```
Dieser interagiert mit dem in `dbparam.py` enthaltenen Kontextmanager zur vollständigen Automatisierung des Öffnens und Schließens der Datenbankverbindung.
Das Verhalten lässt sich in drei voneinander getrennte Phasen einteilen:

**Phase I: Eintritt in den `with`-Block**

Der Einritt in den `with`-Block geschieht mit der Ausführung folgender Codezeile:

```python
with connection() as conn:
```

In dieser Phase ruft Python `connection()` in `dbparam.py` bis zur `yield`-Anweisung auf.
Dort geschieht folgendes:

1. Die Datenbankverbindung wird hergestellt

```python
    # Verbindung öffnen
    con = sqlite3.connect(DB_PATH)
```

2. Das Laden von Erweiterungen wird aktiviert

```python
    # SpatiaLite-Erweiterung laden
    con.enable_load_extension(True)
```

3. Die SpatiaLite-Erweiterung wird geladen

```python
    con.load_extension(SPATIALITE_DLL)
```

4. Die `yield`-Anweisung übergibt das Verbindgungsobjekt `con` an den Aufrufer (`with`-Block)

```python
    try:
        # Verbindung an den Aufrufer „übergeben“
        yield con
```

Das Verbindungsobjekt `con` wird nun als `conn` innerhalb des `with`-Statements verwaltet, daher die Bezeichnung `as conn` am Ende der Zeile des `with`-Blocks. Das Element `conn` beinhaltet nun eine geöffnete SQLite-Datenbankverbindung mit geladener SpatiaLite-Erweiterung.

**Phase II: Ausführung des `with`-Blockinhalts**

Der `with`-Block beinhaltet eine `pandas`-Funktion namens `read_sql()`. Ihr werden das in `query` gespeicherte SQL-Statement sowie das Element `conn` übergeben, welches die Verbindung zur Datenbank bereitstellt. 

```python
df = pd.read_sql(query, conn)
```

Die Funktion übergibt anhand der Datenbankverbindung das SQL-Statement an die SQLite-Datenbank, liest das gefilterte Ergebnis ein und speichert es in einem `DataFrame` namens `df`.

**Phase III: Verlassen des `with`-Blocks**

Sobald der `with`-Block verlassen wird, führt Python automatisch den Code im `finally`-Zweig des Kontextmangers in `dbparam.py` aus:

```python
finally:
    con.close()
```

Wie schon im Kapitel *5.2.1 Verbindungslogik zur Datenbank (`dbparam.py`)* erwähnt, spielt es dabei keine Rolle, ob die Ausführung des Inhalts des `with`-Blocks erfolgreich ist. In allen Fällen wird zwingend `con.close()` ausgeführt und die Datenbankverbindung wieder geschlossen.

Schlussendlich wird der `DataFrame` in der Konsole der Entwicklungsumgebung ausgegeben. Dafür werden zwei `print`-Anweisungen genutzt. Die erste dient lediglich einer kurzen Beschreibung der Ausgabe, der zweite gibt schließlich das Ergebnis aus.

```python
#Ausgabe des DataFrames im Terminal (mit vorangestellter Textbeschreibung)
print("\n Die Geburtstage der Mitarbeiter - sortiert nach Monat und Tag:\n")
print(df)
```
Der folgende Auszug zeigt die Struktur des erzeugten `DataFrame`:

```python
 Die Geburtstage der Mitarbeiter - sortiert nach Monat und Tag:

          Name    Gebdat
0         Ralf  19610101
1        Nager  19700110
2   Rubble-Ger  19830115
3   Feuerstein  20010120
4       Tigger  19880125
5         Kind  19930204
6        Kanga  19980213
7    Doolittle  19850219
8         Shir  19680228
9       Grafie  19680310
10  Geröllheim  19820315
11         Eis  20000320
12        Hase  19870325
13     Poppins  19920404
14       Fuchs  19970413
15        Levi  19840419
                    [...]
```