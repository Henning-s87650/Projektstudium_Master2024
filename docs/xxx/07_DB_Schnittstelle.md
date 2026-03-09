## 5.2.1 Verbindungslogik zur Datenbank (`dbparam.py`)

Das Modul `dbparam.py` kapselt den Verbindungsaufbau zur SQLite-Datenbank und das Laden der SpatiaLite-Erweiterung. Die Anwendung benötigt dafür die Module `os` und `sqlite3` sowie die Klasse `path` des Moduls `pathlib` und den Dekorator `contextmanager`.

```python
#Import der notwendigen Bibliotheken
import os
import sqlite3
from pathlib import Path
from contextlib import contextmanager
```

Danach folgt die zentrale Definition der Pfade zur Datenbank (`DB_PATH`), dem Verzeichnis, indem die SpatiaLite-Erweiterungsdatei liegt (`SPATIALITE_DIR`) sowie der Pfad zur SpatiaLite-Erweiterungsdatei selbst (`SPATIALITE_DLL`).

```python
#Pfad zu DB-Datei, dem SpatiaLite-Verzeichnis und der SpatiaLite-Erweiterungsdatei
DB_PATH = r"D:\Studium\Studienunterlagen\Master\03_Fachsemester\01_Projektstudium\01_PROGRAM\01_DATABASE\gm23s87650_16072025.db"
SPATIALITE_DIR = r"C:\Program Files\Spatialite\mod_spatialite-5.1.0-win-amd64"
SPATIALITE_DLL = r"C:\Program Files\Spatialite\mod_spatialite-5.1.0-win-amd64\mod_spatialite.dll"
```
Durch Aufrufen der Funktion `add_dll_directory()` des Moduls `os` wird das zuvor definierte Verzeichnis der SpatiaLite-Erweiterungsdatei zur Windows-Suchpfadliste hinzugefügt. 

```python
os.add_dll_directory(SPATIALITE_DIR)
```

Dieser Schritt ist notwenidg für das spätere Laden der Erweiterung. Dem Betriebssystem wird so mitgeteilt, in welchem Verzeichnis nach DLL-Dateien gesucht werden soll. <br>
Die Verbindung zur Datenbank wird über eine eigens definierte Funktion namens `connection` hergestellt. Diese wird zuvor mit dem Dekorator `@contextmanager` in einen Kontextmanager umgewandelt.

```python
@contextmanager
def connection():

    # Verbindung öffnen
    con = sqlite3.connect(DB_PATH)

    # SpatiaLite-Erweiterung laden
    con.enable_load_extension(True)
    con.load_extension(SPATIALITE_DLL)

    try:
        # Verbindung an den Aufrufer „übergeben“
        yield con
    finally:
        # Verbindung immer schließen – auch bei Fehlern im with-Block
        con.close()
```
Der Vorteil bei der Verwendung eines Kontextmanagers liegt in der Vereinfachung der Syntax. Ohne dessen Verwendung würde die Funktion `connection()` lediglich ein Objekt mit einer geöffneten Datenbankverbindung zurückgeben. Nach der Ausführung des entsprechenden SQL-Statements müsste diese wieder manuell geschlossen werden, beispielweise durch die Nutzung von `con.close()` nach Ausführung des SQL-Statements direkt im Skript für die Datenverarbeitung.

Die Funktion beginnt mit
```python
def connection():
```
und erhält keine Eingabeparameter, da diese ohnehin immmer dieselben sind. <br>
Als erster Schritt innerhalb der Funktion `connection()` wird `con` als SQLite-Verbindung definiert. Der entsprechenden Funktion `sqlite3.connect()` wird dafür der Pfad zur Datenbankdatei übergeben. Diese Funktion gibt ein SQLite-Verbindungsobjekt zurück, welches somit in `con` gespeichert ist.
```python
# Verbindung öffnen
    con = sqlite3.connect(DB_PATH)
```
In SQLite ist das Laden von Erweiterungsmodulen standardmäßig deaktiviert. Daher muss SpatiaLite beim Öffnen einer Datenbankverbindung zunächst geladen werden, um SQL-Funktionen für räumliche Abfragen nutzen zu können. Dafür wird die Funktion `enable_load_extension()` auf das Verbindungobjekt angewendet und der Wert `True` übergeben. Mithilfe der Funktion `load_extension()` wird dann der Pfad zur Erweiterungsdatei (*mod_spatialite.dll*) angegeben.

```python
    # SpatiaLite-Erweiterung laden
    con.enable_load_extension(True)
    con.load_extension(SPATIALITE_DLL)
```
Auf diese Weise ist jede Verbindung, die `connection()` aufbaut fähig, räumliche Funktionen auf die Datenbank anzuwenden. <br>
Am Ende der Funktion folgt ein `try`-`finally`-Block mit `yield`-Anweisung.
```python
    try:
        # Verbindung an den Aufrufer übergeben
        yield con
    finally:
        # Verbindung immer schließen – auch bei Fehlern im with-Block
        con.close()
```
Dieser Codeabschnitt ist die zentrale Funktionalität des verwendeten Kontextmanagers. Die Funktion `connection()` wird damit in zwei Phasen aufgeteilt:

1. vor-`yield`-Phase
   - Öffnen der Datenbankverbindung
   - Laden der SpatiaLite-Erweiterung
2. nach-`yield`-Phase
   - Schließen der Datenbankverbindung

Der Befehl `yield con` übernimmt zwei Aufgaben gleichzeitig. Er übergibt das Verbindungsobjekt `con` an den Aufrufer (Skripte zur Datenverarbeitung), damit dort unter dessen Angabe SQL-Anweisungen an die Datenbank übermittelt werden können. In den Skripten zur Datenverarbeitung wird das durch einen `with`-Block realisiert (siehe: Logik der Datenverarbeitung):
```python
with connection() as conn:
    df = pd.read_sql(query, conn)
```
Zudem markiert er die Trennlinie zwischen dem Verbindungsaufbau und -abbau. Der oberhalb von `yield` stehende Code wird beim Eintritt in den `with`-Block ausgeführt, der darunterstehende Code:
```python
    finally:
        # Verbindung immer schließen – auch bei Fehlern im with-Block
        con.close()
```
bei dessen Verlassen. <br>

Die Kombination mit dem `try`-`finally`-Block stellt folgenden Ablauf sicher: Egal, wie der `with`-Block verlassen wird - ob mit oder ohne einem Fehler - der Code im `finally`-Block wird immer ausgeführt. Dadurch wird die Datenbankverbindung, unabhängig vom erfolgreichen Ausführen der SQL-Statements stets geschlossen.

Die folgende Abbildung stellt den gesamten Code des Programm `dbparam.py` dar.

```python
# Import der notwendigen Bibliotheken
import os
import sqlite3
from pathlib import Path
from contextlib import contextmanager

# Pfad zu DB-Datei, dem SpatiaLite-Verzeichnis und der SpatiaLite-Erweiterungsdatei
DB_PATH = r"D:\Studium\Studienunterlagen\Master\03_Fachsemester\01_Projektstudium\01_PROGRAM\01_DATABASE\gm23s87650_16072025.db"
SPATIALITE_DIR = r"C:\Program Files\Spatialite\mod_spatialite-5.1.0-win-amd64"
SPATIALITE_DLL = r"C:\Program Files\Spatialite\mod_spatialite-5.1.0-win-amd64\mod_spatialite.dll"

os.add_dll_directory(SPATIALITE_DIR)

@contextmanager
def connection():

    # Verbindung öffnen
    con = sqlite3.connect(DB_PATH)

    # SpatiaLite-Erweiterung laden
    con.enable_load_extension(True)
    con.load_extension(SPATIALITE_DLL)

    try:
        # Verbindung an den Aufrufer „übergeben“
        yield con
    finally:
        # Verbindung immer schließen – auch bei Fehlern im with-Block
        con.close()
```
