# Inhaltsverzeichnis
- Einleitung
- technische Grundlagen
    - Datengrundlage
    - Anforderungsanalyse
        - Anforderungen an die Datenbank
        - Anforderungen an die Python-Programme
    - Systementwurf
    - Auswahl der Python-Bibliotheken
        - Kriterien
        - Bewertung der Bibliotheken
        - Ergebnis der Bewertung
    - Systemvoraussetzungen und Softwareinstallation (überarbeiten)
        - Installation der benötigten Softwarekomponenten
        - Setup der Projektumgebung (überarbeiten)
- Implementierung
    - Datenbankmigration
        - Erstellen des Datenbankschemas
        - Übertragung der Tabelleninhalte mit FME
        - Validierung des Migrationsprozesses
    - Python-Programmierung
        - Verbindungslogik zur Datenbank (`dbparam.py`)
        - Verwaltung der SQL-Anweisungen (`queries.py`)
        - Python-Anwendungen für die Sachdatenwiedergabe
        - Python-Anwendungen für Geodatenwiedergabe
- Nutzung der Software auf anderem Desktop
- Anpassung und Erweiterung der Software
    - Anpassung an neue Systemumgebungen
    - Erweiterung der SQL-Verwaltung
    - Erweiterung der Datenverarbeitung
- (Ergebnisauswertung)
- (Fazit)
- Anhang

# 1 Einleitung

hier kommt eine Einleitung

# 2 technische Grundlagen

## 2.1 Datengrundlage

Als Ausgangsbasis dient eine relationale Datenbank, die bereits im Rahmen des Mastermoduls Datenbanktechnologien (Geoinformatik/Management) zu Übungszwecken verwendet wurde. Die Verwaltung dieser Datenbank erfolgt über Microsoft SQL Server Management Studio (MS SSMS). Sie umfasst sechs Tabellen, von denen zwei Geodaten des Typs *geography* enthalten. Die nachfolgende Abbildung veranschaulicht die Tabellenstruktur, enthaltene Datentypen sowie bestehende Beziehungen zwischen den Tabellen. 

![ER-Diagramm der Datengrundlage](media/ER_Diagramm_MS_SSMS.png)

Diese Struktur bildet die Grundlage für alle späteren SQL-Abfragen und Auswertungen und
definiert den Funktionsumfang, den das Zielsystem in SQLite/SpatiaLite reproduzieren soll.

## 2.2  Anforderungsanalyse

Die Anforderungen sind in **funktionale** und **nicht-funktionale** Anforderungen unterteilt. Zusätzlich wird zwischen Anforderungen an die **Datenbank** und an die **Python-Programme** unterschieden.

### 2.2.1   Anforderungen an die Datenbank

#### Funktionale Anforderungen an die Datenbank

Die Anforderungen an die Datenbank leiten sich aus den im Modul „Datenbanktechnologien“ durchgeführten MS-SQL-Praktika ab. Diese Aufgaben definieren den Funktionsumfang der ursprünglichen MS-SQL-Server-Datenbank und dienen als Referenzrahmen für die neue SQLite-/SpatiaLite-Lösung.

**Räumliche Datenhaltung (FD1)**  
In „MS SQL 2 – Verwaltung geografischer Informationen“ wird die Tabelle `Shop` um eine Spalte vom Typ `geography` erweitert und mit GPS-Koordinaten befüllt. Zusätzlich werden die Flächen der deutschen Bundesländer als Polygongeometrien in die Tabelle `Geografie` eingefügt. Die neue Datenbank muss Punkt- und Flächengeometrien dauerhaft speichern und in einem räumlichen Format verwalten können, das arithmetische und relationale Operationen unterstützt.

**Räumliche Abfragen (FD2)**  
Die Praktikumsaufgaben umfassen unter anderem:
- Ermittlung der Shops innerhalb eines bestimmten Bundeslands,
- Ausgabe von Koordinaten im WKT-Format,
- Abfrage der Bundesländer, die Hessen begrenzen.

Die Datenbank muss daher in der Lage sein topologische Operationen und räumliche Abfragen interpretieren und ausführen können.

**Geometrische Berechnungen (FD3)**  
Es sollen Abstände (z. B. zwischen Shops und dem Standort der HTW Dresden) und Flächeninhalte der Bundesländer berechnet werden können.

**Aggregation und Views (FD4)**  
Bereits in „MS SQL 1 – Aufbau einer OLTP-Datenbank“ wird eine View gefordert, die den wertmäßigen Gesamtbestand pro Bundesland abbildet. In „MS SQL 2“ wird diese Aggregation mit Geometrien kombiniert, um den Bestandswert pro Quadratkilometer zu berechnen. Die Datenbank muss Aggregationen und Views bereitstellen, die diese Auswertungen ermöglichen.

**Abfrageoptimierung und Indizes (FD5)**  
In „MS SQL 4 – Analyse von Abfrageplänen“ werden der Einfluss und die Wirkung von Indizes auf das Abfrageverhalten untersucht. Die neue Datenbank muss das Anlegen und Nutzen von Indizes zur Abfrageoptimierung unterstützen.

####  Übersicht funktionale Anforderungen Datenbank

| Nummer | Anforderung              | Beschreibung                                                              |
|--------|--------------------------|---------------------------------------------------------------------------|
| FD1    | Räumliche Datenhaltung   | Geodaten (Punkte, Flächen) müssen gespeichert und ausgewertet werden.    |
| FD2    | Räumliche Abfragen       | Abfragen nach räumlichen Beziehungen müssen ausführbar sein.             |
| FD3    | Berechnungen             | Abstände und Flächeninhalte müssen berechnet werden können.              |
| FD4    | Aggregation und Views    | Aggregationen und Views müssen erstellt und ausgegeben werden können.    |
| FD5    | Abfrageoptimierung       | Indizes sollen zur Abfrageoptimierung angelegt und genutzt werden.       |

---

#### Nicht-funktionale Anforderungen an die Datenbank

Die nicht-funktionalen Anforderungen betreffen die strukturelle und inhaltliche Übereinstimmung der migrierten SQLite-/SpatiaLite-Datenbank mit der ursprünglichen MS-SQL-Server-Datenbank.

**Tabellenstruktur (ND1)**  
In „MS SQL 1“ wird ein relationales Schema mit den Tabellen `Shop`, `Geografie`, `Mitarbeiter`, `Artikel` und `Bestand` definiert. Die neue Datenbank soll diese Tabellenstruktur vollständig abbilden, um alle Praktikumsaufgaben und Abfragen auf gleicher Basis durchführen zu können.

**Relationen (ND2)**  
Primär- und Fremdschlüsselbeziehungen sind für die Aufgaben essenziell (z. B. Verknüpfung von Shops mit Geometrien oder von Artikeln mit Beständen). Die migrierte Datenbank soll diese Beziehungen korrekt übernehmen.

**Inhaltliche Übereinstimmung (ND3)**  
Die Inhalte der Tabellen in SQLite sollen den Daten der MS-SQL-Datenbank entsprechen, damit sich Abfragen, Distanzberechnungen und Aggregationen sinnvoll vergleichen lassen.

####  Übersicht nicht-funktionale Anforderungen Datenbank

| Nummer | Anforderung               | Beschreibung                                                                 |
|--------|---------------------------|------------------------------------------------------------------------------|
| ND1    | Tabellenstruktur          | Die Tabellen `Shop`, `Geografie`, `Mitarbeiter`, `Artikel`, `Bestand` müssen vorhanden sein. |
| ND2    | Relationen                | Primär- und Fremdschlüssel sollen der ursprünglichen Datenbank entsprechen. |
| ND3    | Inhaltliche Übereinstimmung | Die Tabellendaten der SQLite-Datenbank sollen der MS-SQL-Datenbank gleichen. |

## 2.2.2 Anforderungen an die Python-Programme

####   Funktionale Anforderungen an die Python-Programme

Die funktionalen Anforderungen an das Python-Programm leiten sich aus dem Projektziel, sowie aus den in den MS-SQL-Praktika durchgeführten Aufgaben ab. Sie beschreiben die Fähigkeiten, die das Python-System besitzen muss, um die Daten aus der migrierten SQLite-/SpatiaLite-Datenbank auszugeben und die Ergebnisse analog zur ursprünglichen SQL-Server-Umgebung darzustellen.

**Datenbankverbindung (FP1)**  
Das Python-Programm muss eine Verbindung zur SQLite-/SpatiaLite-Datenbank herstellen.

**SpatiaLite-Erweiterung laden (FP2)**  
Die SpatiaLite-Erweiterung muss geladen werden, damit räumliche Funktionen verfügbar sind. Ohne das Laden der Erweiterung wären die aus MS SQL 2 bekannten Funktionen wie Distanz-, Flächen- oder Überschneidungsoperationen nicht durchführbar.

**SQL-Anweisungen ausführen (FP3)**  
Das Programm muss SQL-Anweisungen ausführen können (FP3). Dies umfasst sowohl klassische Sachdatenabfragen als auch räumliche SQL-Statements. Die Verwendung von SQL-Statements zur Datenverarbeitung, anstatt der reinen Nutzung von Python-Syntax, ergibt sich aus der Zielsetzung zur Nachempfindung der Bearbeitungslogik der Aufgaben der MS SQL-Praktika.

**Gefilterte Datenlagen einlesen (FP4)**  
Gefilterte Datenlagen (z. B. einzelne Bundesländer, Shops oder Mitarbeiter) sollen eingelesen werden können.

**Tabellarische Darstellung von Sachdaten (FP5)**  
Die eingelesenen Daten sollen tabellarisch dargestellt werden, um die Ergebnisse mit der MS-SQL-Server-Umgebung vergleichbar zu halten.

**Visualisierung von Geodaten (FP6)**  
Geodaten (Flächen aus `Geografie`, Punkte aus `Shop`) sollen mithilfe von Python visualisiert werden können.

####  Übersicht funktionale Anforderungen Python

| Nummer | Anforderung                       | Beschreibung                                                                 |
|--------|-----------------------------------|------------------------------------------------------------------------------|
| FP1    | Datenbankverbindung aufbauen      | Öffnen einer Datenbankinstanz aus Python.                                   |
| FP2    | SpatiaLite-Erweiterung laden      | Laden der SQLite-Erweiterung SpatiaLite.                                    |
| FP3    | SQL-Anweisungen                   | Ausführen von SQL-Anweisungen zur Datenanalyse.                             |
| FP4    | Einlesen gefilterter Datenlage    | Einlesen gefilterter Datenlagen über SQL.                                   |
| FP5    | Darstellung von Sachdaten         | Tabellarische Darstellung der gefilterten Sachdaten.                        |
| FP6    | Visualisierung von Geodaten       | Darstellung der Geodatenlage in Kartenform.                                 |

#### Nicht-funktionale Anforderungen an die Python-Programme (NP)

Die nicht-funktionalen Anforderungen betreffen Eigenschaften der Python-Lösung, die über die reine Funktionserfüllung hinausgehen.

**Open-Source-Basis (NP1)**  
Es sollen ausschließlich Open-Source-Komponenten eingesetzt werden. Dadurch bleibt die Lösung lizenzfrei, offen und reproduzierbar.

**Wartbarkeit und Modularität (NP2)**  
Der Code soll modular strukturiert und nachvollziehbar kommentiert sein. Verbindungslogik, Abfrageverwaltung und Datenverarbeitung werden getrennt, um:
- einzelne Komponenten unabhängig testen und erweitern zu können,
- die Wartbarkeit und Wiederverwendbarkeit zu erhöhen.

#### Übersicht nicht-funktionale Anforderungen Python

| Nummer | Anforderung   | Beschreibung                                                    |
|--------|---------------|-----------------------------------------------------------------|
| NP1    | Open-Source   | Alle verwendeten Softwarekomponenten sollen Open-Source-basiert sein. |
| NP2    | Wartbarkeit   | Modularer Aufbau und nachvollziehbare Kommentare im Programmcode.     |

## 2.3   Systementwurf

Auf Basis der Anforderungsanalyse ergibt sich ein Systementwurf mit vier Komponenten. Das folgende Diagramm veranschaulicht diesen und zeigt die Interaktionen zwischen den verschiedenen Komponenten.

![UML-Diagramm des Systementwurfs](media/Schema_Systemkonzept.jpg)

Zusammenfassend lassen sich die einzelnen Kompenenten folgednermaßen beschreiben:

1. **Datenhaltung**  
   - SQLite-Datenbank mit SpatiaLite-Erweiterung  
   - Speicherung von Sach- und Geodaten  
   - möglichst exakte Abbildung der ursprünglichen MS-SQL-Server-Datenbank, um eine inhaltliche und funktionale Vergleichbarkeit sicherzustellen.

2. **Schnittstelle zur Datenhaltung**  
   - Python-basierte Verbindungslogik  
   - Öffnen der Datenbankinstanz  
   - Laden der SpatiaLite-Erweiterung  
   - Rückgabe eines Verbindungsobjekts, das in allen Auswertungsskripten wiederverwendet wird.

3. **Verwaltung der Verarbeitungsregeln**
   - enthält SQL-Satements für die Datenverarbeitung in Form eines Dictionary
   - jedes Statement besitzt ein "sprechendes" Schlüsselattribut
   - Nutzung der Schlüsselattribute zum Aufruf der SQL-Statements für die Datenverarbeitung

4. **Datenverarbeitung und Visualisierung**  
   - spezialisierte Python-Skripte für Analyse- und Visualisierungsaufgaben  
   - Auswahl passender SQL-Anweisung aus dem Dictionary
   - Übergabe des SQL-Statements und der Verbindungsparameter an die Datenbank  
   - Einlesen der gefilterten Datenlage in tabellarische Datenstrukturen
   - Ausgabe von Sachdaten im Terminal und zusätzliche Visualisierung von Geodaten.

## 2.4  Auswahl der Python-Bibliotheken

Für die Umsetzung der in der Anforderungsanalyse formulierten Anforderungen an die Python-Programme ist die Auswahl geeigneter Bibliotheken von zentraler Bedeutung. Ziel ist ein skriptbasiertes System, das Sach- und Geodaten aus der SQLite-/SpatiaLite-Datenbank ausliest, auswertet und darstellt.

Die Bibliotheksauswahl orientiert sich dabei an den funktionalen Anforderungen **FP3 bis FP6** sowie der nicht-funktionalen Anforderung **NP1**.  
Der Verbindungsaufbau zur Datenbank erfolgt über das Python-Modul `sqlite3` und das Laden der Spatialite-Erweiterung mithilfe des Moduls `os`. Damit sind die Anforderungen **FP1** (Datenbankanbindung) und **FP2** (Laden der SpatiaLite-Erweiterung) bereits erfüllt. Diese beiden Anforderungen fließen daher nicht in die Formulierung der Auswahlkriterien ein.

### 2.4.1 Kriterien

Auf Basis der funktionalen Anforderungen werden folgende Kriterien für die Bewertung der Bibliotheken definiert:

| Kriterium | Beschreibung                                                                                 | Bezug |
|----------|-----------------------------------------------------------------------------------------------|-------|
| K1       | Verarbeitung von SQL – die Bibliothek muss SQL-Anweisungen an die Datenbank übergeben können | FP3   |
| K2       | Interpretation von Tabellenstrukturen – tabellarisch geordnete Daten interpretieren          | FP4   |
| K3       | Tabellarische Wiedergabe – tabellarische Daten wiedergeben                                   | FP5   |
| K4       | Grundlegende Interpretation von Geometrieformaten                                            | FP5   |
| K5       | Erweiterte Interpretation von Geometrieformaten – z. B. mehrteilige Geometrien               | FP5   |
| K6       | Visualisierung von Geometriedaten – Geometriedaten ad hoc darstellen                        | FP6   |

Die nicht-funktionale Anforderung **NP1 (Open-Source)** wird nicht als eigenes Kriterium aufgeführt, da bei der Recherche von vornherein ausschließlich Bibliotheken mit Open-Source-Lizenz betrachtet werden.

Auf Grundlage dessen wird eine Bewertungsmatrix erstellt, in der eine Auswahl relevanter Bibliotheken gegenübergestellt wird. Die betrachteten Bibliotheken wurden im Rahmen einer Recherche in Fachartikeln, Online-Foren und anhand von Downloadstatistiken ausgewählt.

#### Bewertungsmatrix

| Bibliothek | K1 | K2 | K3 | K4 | K5 | K6 |
|-----------|----|----|----|----|----|----|
| Shapely   | ✗  | ✗  | ✗  | ✓  | ✓  | ✗  |
| GeoPandas | ✗  | ✓  | ✓  | ✓  | ✓  | ✓  |
| Cartopy   | ✗  | ✗  | ✗  | ✓  | ✓  | ✓  |
| Folium    | ✗  | ✗  | ✗  | ✓  | ✗  | ✓  |
| ipyleaflet| ✗  | ✗  | ✗  | ✓  | ✗  | ✓  |
| leafmap   | ✗  | ✗  | ✗  | ✓  | ✓  | ✓  |

### 2.4.2 Bewertung der Bibliotheken

**GeoPandas**  
Die Matrix verdeutlicht, dass GeoPandas nahezu alle Kriterien erfüllt:

- Interpretation tabellarischer Datenstrukturen (K2),
- tabellarische Wiedergabe (K3),
- Verarbeitung grundlegender und mehrteiliger Geometrietypen (K4, K5),
- direkte Visualisierung von Geometriedaten (K6).

Damit deckt GeoPandas einen Großteil der Anforderungen **FP3 bis FP6** ab.

**Shapely**  
Shapely, auf dem GeoPandas technisch basiert, erfüllt die geometriebezogenen Kriterien (K4, K5), bietet jedoch:

- keine tabellarischen Datenstrukturen (K2, K3),
- keine eigenen Visualisierungsmöglichkeiten (K6).

Da Shapely vollständig in GeoPandas integriert ist, entsteht durch eine eigenständige Nutzung kein zusätzlicher Mehrwert.

**Cartopy**  
Cartopy unterstützt eine Vielzahl von Geometrietypen (K4, K5) und verfügt über umfangreiche Visualisierungsfunktionen (K6). Es bietet jedoch:

- keine tabellarische Datenverarbeitung (K2, K3),
- keine Schnittstellen zur SQL- oder Datenbankkommunikation (K1).

Abgesehen von einer breiten Palette kartographischer Projektions- und Darstellungsmöglichkeiten bietet Cartopy damit keine entscheidenden Vorteile für die Projektziele. Es eignet sich eher als Ergänzung, nicht jedoch als zentrale Bibliothek.

**Folium**  
Folium basiert auf dem JavaScript-Framework Leaflet und erzeugt interaktive Karten als HTML-Dokumente. Die Übergabe von Daten erfolgt über das GeoJSON-Format, wodurch Geometrien zuvor konvertiert werden müssen. Einschränkungen:

- keine Unterstützung für WKB oder WKT – eine direkte Nutzung der in SpatiaLite gespeicherten Geometriemodelle ist nicht möglich,
- keine Verarbeitung von SQL-Anweisungen (K1),
- keine Interpretation oder Ausgabe tabellarischer Datenstrukturen (K2, K3),
- nur grundlegende Geometrieformate (K4), keine mehrteiligen Geometrien (K5),
- Visualisierung (K6) ist browserbasiert und an das Generieren von HTML-Artefakten gebunden.

Aufgrund dieser Einschränkungen ist Folium für das Erreichen des Projektziels nicht geeignet.

**ipyleaflet**  
ipyleaflet ist eine an Jupyter-Notebooks angepasste Variante des Leaflet-Frameworks und verfolgt einen ähnlichen Ansatz wie Folium. Die Bibliothek ist vollständig auf interaktive Notebook-Umgebungen ausgerichtet. Wie bei Folium fehlen:

- Funktionen zur Interpretation tabellarischer Datenstrukturen (K2, K3),
- jede Art von SQL-Integration (K1).

Die Verarbeitung von Geometrien (K4) erfolgt über GeoJSON oder Koordinatenlisten. Die im Projekt benötigten WKB-Formate können nicht direkt eingelesen werden; komplexere Geometrien (K5) erfordern zusätzliche Vorverarbeitungsschritte. ipyleaflet bietet zwar umfangreiche interaktive Visualisierungsmöglichkeiten (K6), jedoch ausschließlich in Jupyter-Umgebungen. Insgesamt erfüllt die Bibliothek damit zu wenige der geforderten Kriterien und wird nicht weiter berücksichtigt.

**leafmap**  
leafmap ist noch stärker auf Notebook-Umgebungen spezialisiert und fungiert als Metawerkzeug, das verschiedene Visualisierungsframeworks zusammenführt.
Das Modul weißt folgende Defizite auf:

- keine Integration tabellarischer Strukturen oder SQL-Schnittstellen (K1, K2, K3),
- Interpretation geometrischer Datenformate erfolgt ausschließlich durch eingebundene Bibliotheken wie GeoPandas (K4, K5),
- Darstellung erfolgt über Notebook-Widgets, die außerhalb interaktiver Umgebungen nicht funktionsfähig sind (K6).

leafmap ist damit gut für interaktive Kartenerstellung in Jupyter-Umgebungen geeignet, verfolgt jedoch einen anderen Schwerpunkt als das Projektziel und wird daher ebenfalls nicht weiter betrachtet.

### 2.4.3 Ergebnis der Auswahl

Die systematische Bewertung zeigt, dass **GeoPandas** die einzige Bibliothek ist, die eine Mehrheit der geforderten Kriterien vollständig erfüllt. In Kombination mit:

- `pandas`,
- `Shapely`,
- `Matplotlib`

entsteht eine integrierte Umgebung, mit der sowohl Sachdaten als auch Geometrien verarbeitet und visualisiert werden können. GeoPandas bildet somit den zentralen Baustein der Python-Implementierung.

# 4 Systemvoraussetzungen und Softwareinstallation

Die entwickelte Lösung ist für den Betrieb auf einem lokalen Arbeitsplatzrechner ausgelegt und wurde unter einem Windows-Betriebssystem implementiert und getestet. Die verwendeten Komponenten sind generell plattformunabhängig und nicht an Windows gebunden.

Plattformabhängig wiederum ist die Installation und das Laden der SpatiaLite-Erweiterung. Diese wird unter Windows als dynamsiche Programmbibliothek (DLL) eingebunden und über betriebssystemspezifische Suchpfade aufgerufen. Entsprechend werden in der Implementierung Windows-typische Dateipfade verwendet. Das Hinzufügen von DLL-Pfaden wird mithilfe der Python-Standardbibliothek vorgenommen.

**Anmerkung:** SpatiaLite ist ebenfalls nicht Windows-gebunden. Die Wahl von Windows als Betriebssystem bedingt jedoch die Art der Installation.

Die Ausführung der Python-Skripte erfolgt lokal und ohne Server- oder Webkomponenten. Alle Anwendungen werden direkt im Benutzerkontext gestartet und greifen auf eine dateibasierte SQLite-Datenbank zu. Eine Mehrbenutzerfähigkeit oder der Betrieb in einer verteilten Umgebung ist nicht vorgesehen.

Geodaten werden in der Datenbank als SpatiaLite-Geometrien gespeichert und für die Verarbeitung in
Python in das OGC-konforme WKB-Format überführt. Die anschließende Interpretation und Visualisierung
erfolgt vollständig im Arbeitsspeicher.

Das System dient der fachlichen Reproduktion und Analyse der im Modul *Datenbanktechnologien*
behandelten Inhalte in einer alternativen technischen Umgebung und ist nicht als produktives
Informationssystem ausgelegt.

## 4.1 Installation der benötigten Softwarekomponenten

Dieses Kapitel beschreibt die grundlegenden Installationsschritte für die im Projekt verwendeten
Softwarekomponenten. Ziel ist es, eine lauffähige Arbeitsumgebung bereitzustellen, in der die
Python-Anwendungen und die SQLite-Datenbank ohne weitere Anpassungen ausgeführt werden
können. Die Anleitung erhebt keinen Anspruch auf Vollständigkeit im Sinne einer detaillierten
Installationsdokumentation der einzelnen Produkte, sondern konzentriert sich auf die für den
Projektbetrieb notwendigen Schritte.


### 4.1.1   Installation von Python

Für die Ausführung der Python-Skripte ist eine lokale Python-Installation erforderlich, sofern noch nicht vorhanden.

1. Die aktuelle Python-Version kann von der [offiziellen Projektseite](https://www.python.org/downloads/)  heruntergeladen werden.
2. Während der Installation ist darauf zu achten, dass Python dem Systempfad hinzugefügt wird
   („Add Python to PATH“):
   <img src=media/Install_Py1.png width="550">
3. Der Erfolg der Installation kann über die mit dem Befehel ```python --version``` in der Eingabeaufforderung Überprüft werden. Der Rückgabewert ist die aktuelle Versionsnummer:
    ![Überprüfung der Python-Version](media/Install_Py2.png)


####   Installation weiterer Python-Bibliotheken

Das Installieren der benötigten Bibliotheken geschieht mit der Eingabeaufforderung durch das Ausführen des folgenden Befehls:

```console
 pip install pandas geopandas shapely matplotlib
 ```

### 4.1.2 Installation von SQLite

SQLite dient als Datenbanksystem für die persistente Speicherung der Projekt­daten. Da SQLite
serverlos arbeitet, ist keine klassische Installation im Sinne eines Datenbankservers
erforderlich.

1. Die vorkompilierten SQLite-Binärdateien können von der 
   [offiziellen Projektseite](https://www.sqlite.org/download.html) heruntergeladen
   werden. Für Windows wird das Paket *Precompiled Binaries for Windows* benötigt.

2. Das heruntergeladene Archiv wird in ein beliebiges Verzeichnis entpackt, beispielsweise
   `C:\sqlite`.

3. Optional kann das Verzeichnis, dem Systempfad *PATH* hinzugefügt
   werden, um SQLite direkt über die Eingabeaufforderung verwenden zu können.

4. Falls Schritt 3 ausgeführt wurde, kann über die Eingabeaufforderung die Installation mithilfe des foglenden Befehels überprüft werden:

   ```console
   sqlite3 --version
   ```

Wird, wie nach der Installation von Python, eine Versionsnummer ausgegeben, ist SQLite korrekt eingerichtet. Für den Betrieb der
Python-Anwendungen ist der direkte Aufruf von sqlite3 mithilfe der Eingabeaufforderung nicht zwingend erforderlich, da der
Zugriff auf die Datenbank über das Python-Modul sqlite3 erfolgt.

### 4.1.3   Installation von SpatiaLite

Zur Verarbeitung räumlicher Daten wird die Erweiterung SpatiaLite benötigt. Diese ergänzt
SQLite um Funktionen zur Speicherung, Analyse und Abfrage von Geodaten.

1. Die passende SpatiaLite-Version für Windows kann von der
[Projektseite](https://www.gaia-gis.it/gaia-sins/) heruntergeladen werden. Es wird die ZIP-Datei names *mod_spatialite* benötigt, welche unter *MS Windows binaries* zu finden ist.

2. Das Archiv wird in ein eigenes Verzeichnis entpackt, beispielsweise
C:\Program Files\Spatialite\.

3. Damit es beim Laden der Erweiterung unter Windows nicht zu möglichen Fehlern kommt, wird empfohlen das neue Verzeichnis dem Systempfad *PATH* hinzuzufügen.

4. Falls Schritt 3 ausgeführt wurde, kann über die Eingabeaufforderung die Installation mithilfe des foglender Befehle überprüft werden:

   4.1. SQLite über folgenden Befehl starten:
   
   ```console 
   sqlite3
   ``` 

   4.2. Laden von SpatiaLite mithilfe der SQL-Anweisung:

   ```sql
   SELECT load_extension('mod_spatialite');
   ```  

   4.3.  SpatiaLite-Version mithilfe folgender SQL-Anweisung ausgeben lassen:

   ```sql
   SELECT spatialite_version();
   ```

   Die Ausgabe kann folgendermaßen aussehen:

   ![Eingabeaufforderung nach Absetzen der obigen Befehle](media/install_spatialite.png)

   Das SQL-Statement 
   
   ```sql
   SELECT spatialite_version();
   ``` 

   hat die Versionsnummer *5.1.0* zurückgegeben, damit ist die Installation erfolgreich.

### Fehlerquellen nach der Installation

Unter Windows kann das Laden von ``mod_spatialite.dll`` trotz vorhandener Datei fehlschlagen. Ursache ist häufig nicht die Erweiterung selbst, sondern eine fehlende oder inkompatible Abhängigkeit (z. B. weitere DLLs) oder eine Vermischung von 32-bit/64-bit-Komponenten. Zusätzlich können mehrere GIS-Installationen dazu führen, dass Windows eine falsche DLL-Version aus dem Suchpfad lädt (ugs. „DLL-Hell“ genannt). 


Es gibt mehrere Ansätze dieses Problem zu lösen.

---unfertig---

### 4.1.4   Installation von DB Browser for SQLite (optional)

Der Einsatz von **DB Browser for SQLite** nicht zwingend erforderlich,
da der Zugriff auf die Datenbank vollständig über Python und SQL erfolgt. Das Werkzeug kann jedoch
als unterstützendes Hilfsmittel zur manuellen Inspektion der Datenbank, zur Kontrolle der
Tabellenstruktur sowie zur Ausführung einzelner SQL-Abfragen genutzt werden.

DB Browser for SQLite kann von der [offiziellen Projektseite](https://sqlitebrowser.org/) heruntergeladen werden. Es stehen zwei Version zur Verfügung. Zum einen *DB Browser for SQLite - Standard installer* für die Nutzung eines grafischen Installers, wie man es herkommlicherweise von Windows-Anwednungen kennt. Zum anderen *DB Browser for SQLite - . zip (no installer)*, für welche die Installation, wie bei SQLite und SpatiaLite vorgenommen wird.

## 4.2 Setup der Projektumgebung

Dieses Kapitel beschreibt die projektspezifischen Einrichtungsschritte, die nach der Installation
der benötigten Softwarekomponenten erforderlich sind. Ziel des Setups ist es, die Projektdateien
so zu konfigurieren, dass die Python-Anwendungen ohne weitere Anpassungen ausgeführt werden können.

#### 4.2.1 Ablage der Projektdateien

Die Projektdateien werden lokal auf dem Rechner abgelegt. Dabei ist sicherzustellen, dass die
vorgesehene Projekt- und Verzeichnisstruktur entweder unverändert erhalten bleibt oder eine neue koherente Struktur angelegt wird, die der in dieser Dokumentation beschriebenen Struktur nachempfunden ist. Bei letzterem ist zu beachten, dass die Speicherorte von ``dbparam.py``, ``queries.py``, der Datenbankdatei, der SQLite- und SpatiaLite-Installation bekannt sind oder sich im gleichen Ordner befinden, wie die Auswertungsskripte. Der Speicherort kann frei gewählt werden, muss jedoch im weiteren Verlauf des
Setup explizit konfiguriert werden.

#### 4.2.2 Konfiguration der Datenbankschnittstelle

Die zentrale Konfiguration der Datenbankverbindung erfolgt in der Datei `dbparam.py`. In dieser
Datei sind die systemabhängigen Pfade hinterlegt, die für den Zugriff auf die Datenbank und das
Laden der SpatiaLite-Erweiterung erforderlich sind.

Folgende Parameter müssen an die jeweilige Systemumgebung angepasst werden:

- der Pfad zur SQLite-Datenbankdatei (`DB_PATH`),
- der Pfad zum Verzeichnis der SpatiaLite-Bibliotheken (`SPATIALITE_DIR`),
- der Pfad zur SpatiaLite-Erweiterungsdatei (`SPATIALITE_DLL`).

Diese Pfade sind abhängig vom Speicherort der Projektdateien sowie von der lokalen Installation
von SpatiaLite. Ohne eine korrekte Anpassung dieser Parameter ist kein erfolgreicher Aufbau der
Datenbankverbindung möglich.

Die Konfiguration erfolgt einmalig vor der ersten Ausführung der Anwendungen.

#### 4.2.3 Voraussetzungen für die Ausführung

Vor dem Start der Python-Skripte muss sichergestellt sein, dass:

- die im Kapitel *Installation der benötigten Softwarekomponenten* beschriebenen Programme
  installiert sind,
- die Projektdateien vollständig vorliegen,
- die Pfade in `dbparam.py` korrekt gesetzt sind,

Sind diese Voraussetzungen erfüllt, ist keine weitere Initialisierung oder Vorbereitung
erforderlich.

# Implementierung

## 3.1 Datenbankmigration

Die Migration der bestehenden MS-SQL-Server-Datenbank nach SQLite erfolgt mit zwei Werkzeugen:

- **DB Browser for SQLite (DBBrowser)** für die Erstellung des Schemas und der Datenbankdatei
- **Feature Manipulation Engine (FME)** für die Übertragung der Tabelleninhalte

Da beide Systeme unterschiedliche SQL-Dialekte verwenden, ist ein direkter Import des Datenbankschemas (bspw. via SQL-Datei) in SQLite nicht möglich. Obwohl es Erweiterungen für MS SSMS gibt, die eine Datenmigration nach SQLite ermöglichen, wurde der Migrationsprozess stattdessen mit der Software Feature Manipulation Engine (FME) durchgeführt. Ausschlaggebend hierfür war die Verfügbarkeit der Software in den Laboreinrichtungen der GI-Fakultät sowie vorhandene Vorkenntnisse im Umgang mit FME.

### 3.1.1 Erstellen des Datenbankschemas mit DB Browser for SQLite

Im DBBrowser for SQLite wird eine neue Datenbank erstellt und das Datenbankschema durch das Anlegen von Tabellen mit Schlüsselattributen und Constraints definiert. Die Datenbank heißt, entsprechend ihrem Gegenstück in MS SSMS, „gm23s87650.db“. Im Fenster „SQL ausführen“ werden dazu die nötigen SQL-Befehle ausgeführt. Das folgende Beispiel zeigt das SQL-Statement zum Erstellen der Tabelle *Bestand*.

```sql
CREATE TABLE Bestand (
    Artnr INTEGER NOT NULL,
    Shop_ID INTEGER NOT NULL,
    Menge INTEGER,
    CONSTRAINT PK_Bestand PRIMARY KEY(Shop_ID, Artnr),
    CONSTRAINT FK_Artnr FOREIGN KEY (Artnr) REFERENCES Artikel(Artnr),
    CONSTRAINT FK_Shop_id FOREIGN KEY (Shop_ID) REFERENCES Shop(Shop_ID)
);
```

Damit liegt eine leere, aber strukturell vorbereitete SQLite-Datenbank vor, die anschließend durch FME mit Inhalten befüllt wird.

### Unterschiede der Datentypen

Es ist zu beachten, dass sich die Datentypen der SQLite-Datenbank von denen der ursprünglichen MS-SQL-Server-Datenbank unterscheiden. SQLite besitzt lediglich fünf Datentypen:

- **NULL**
- **INTEGER**
- **REAL**
- **TEXT**
- **BLOB**

Dadurch kann die Bandbreite an Datentypen, welche SQL-Server/ Transact-SQL unterstützt nicht widergespiegelt werden. Beim Erstellen des Schemas werden daher die ursprünglichen Datentypen wie folgt in SQLite abgebildet:

- **int** wird zu **INTEGER**
- **money** wird zu **REAL**
- **date** wird zu **TEXT**
- **varchar** wird zu **TEXT**
- **geography** wird zu **BLOB**


### 3.1.2 Übertragung der Tabelleninhalte mit FME

Die eigentliche Migration der Datensätze erfolgt mithilfe von FME.  
Dazu wird ein Reader für die Originaldatenbank angelegt und anschließend ein Writer für die Zieldatenbank konfiguriert.

### Schritt 1: Reader konfigurieren (detaillierter ausarbeiten mit mehr Abbildungen)

- In FME wird ein neuer **Reader** hinzugefügt.
- Als Format wird **„Microsoft SQL Server Spatial“** gewählt.
- Im sich öffnenden Verbindungsfenster werden die gleichen Parameter eingetragen wie in MS SSMS (Servername, Datenbankname, Authentifizierung).
- Unter *Parameters → Constraints → Tables* werden die Tabellen ausgewählt, die übertragen werden sollen.
- Weitere Einstellungen sind nicht erforderlich.

Nach Bestätigung mit **OK** erzeugt FME für jede gewählte Tabelle ein Reader-Objekt im Canvas.

### Schritt 2: Writer konfigurieren (detaillierter ausarbeiten mit mehr Abbildungen)

- Für jeden Reader wird ein **Writer** hinzugefügt.
- Als Format wird **„SpatiaLite“** gewählt.
- Unter *Dataset* wird der Pfad zur zuvor erstellten Datei `gm23s87650.db` angegeben.
- Nach Bestätigung mit **OK** erscheint für jede Tabelle ein Writer-Objekt im Canvas.

### Schritt 3: Reader und Writer verbinden

- Jede Reader-Komponente wird mit ihrem zugehörigen Writer verbunden.
- Dies wird für alle Tabellen wiederholt.

![Abbildung mit verbundenen Readern und Writern]()

### Schritt 4: Prozess ausführen

- Der gesamte Prozess wird mit **Run** gestartet.
- FME liest die Daten aus MS SQL Server ein und schreibt sie in die SQLite-Datenbank.

![Abbildung des FME-Fensters mit markierten RUN-Button]()

Damit sind alle Tabelleninhalte in die SQLite-Datenbank übertragen worden.

### 3.1.3 Ergebnis des Migrationsprozesses

### Prüfung des Datenbankschemas

Nach der Übertragung folgt die Prüfung, ob der Migrationprozess in das neue System vollständig und korrekt durchgeführt wurde. Für diesen Schritt wird ein ER-Diagramm der neuen Datenbank erstellt. Da SQLite selbst keine Funktion zur Generierung eines ER-Diagramms bereitstellt, wird hierfür eine Drittsoftware genutzt.  

Zum Einsatz kommt die **DBeaver Community Edition**, ein Open-Source-Client zur Verwaltung verschiedener Datenbanksysteme. Dafür kann auch jede andere Software genutzt werden, welche im Stande ist, ER-Diagramme anhand einer Datenbankverbindung zu generieren, beispielsweise DBVisualizer. Die nachfolgende Abbildung zeigt das mithilfe von DBeaver erzeugte ER-Diagramm in der Martin-Notation.

![ER_Diagramm des Datenbankschemas](media/ER_Diagramm_SQLite_DB.png)

In DBeaver lassen sich zusätzlich die zugehörigen Constraints einsehen. Durch Auswahl der jeweiligen Beziehung im ER-Diagramm werden die betroffenen Attribute angezeigt.  

![ER_Diagram mit gewählter Beziehung](media/ER_Diagramm_Beziehung.png)

Das ER-Digramm zeigt, dass das Schema der SQLite-Datenbank, mit Ausnhame der Datentypen, identisch zur Originaldatenbank in SQL-Server ist.

### Prüfung der Tabelleninhalte

Das Überprüfen der Tabelleninhalte wird stichprobenartig und anhand quantitativer Kennwerte
vorgenommen. Ziel ist es, zu verifizieren, dass die Datenübertragung vollständig erfolgt ist und
die Inhalte der Tabellen in SQLite mit jenen der ursprünglichen MS-SQL-Server-Datenbank
übereinstimmen. Da einzelne Tabellen (z. B. `Verkauf`) zu groß für eine rein visuelle Kontrolle
sind, werden SQL-Anweisungen genutzt.

1. den Vergleich der Zeilenzahl (Vollständigkeit)
4. den Vergleich einfacher Aggregat-Signaturen (Plausibilitätsnachweis)
5. Deterministische Stichproben (reproduzierbare Sichtprüfung)

Die folgenden Unterabschnitte dokumentieren diese Prüfungen für die einzelnen Tabellen.

**Zeilenzahl**

Für den Vergleich der Zeilenanzahlen wird in beiden Systemen folgende SQL-Anweisung ausgeführt:

```sql
SELECT COUNT(*) AS count FROM Artikel;
```

| Tabellenname | Zeilenanzahl MS SSMS    | Zeilenanzahl SQLite |
|--------|-----------------------------------|------------------------------------------------------------------------------|
| Artikel    |200|200|
| Bestand    |3800|3800|
| Geografie    |47|47|
| Mitarbeiter    |53|53|
| Shop    |21|21|
| Verkauf    |310547|310547|

Da die Zeilenanzahlen der Tabellen beider Datenbanken identisch sind, ist davon auszugehen, dass die Datensätze vollständig übernommen wurden. Um zu Überprüfen, ob das tatsächlich zutrifft, werden Stichproben von zehn zufälligen Datensätzen aus der SQLite-Datenbank entnommen und im Anschluss in MS SSMS genau diese Datensätze ermittelt. Sind die Datensätze in der Referenzdatenbank vorhanden wird davon ausgegangen, dass die jeweiligen Tabellen in beiden Systemen übereinstimmen. Anahnd der Tabelle *Artikel* wird dieser Vorgang demonstriert. Mithilfe dieses SQL-Statements erfolgt zunächst die Entnahme 10 zufälliger Datensätze:

```sql
SELECT *
FROM (
    SELECT *
    FROM Artikel
    ORDER BY RANDOM()
    LIMIT 10
)
ORDER BY Artnr ASC
```

Die Unterabfrage gibt 10 zufällige Datensätze aus der Tabelle aus. Die übergeordnete Abfrage sortiert diese nach aufsteigender Artnr, um die Ausgaben visuell besser vergleichen zu können.

![Ergebnis der SQL-Abfrage in SQLite](media/Validierung_SQLite.png)

In MS SSMS wird folgende Abfrage genutzt, um die Datensätze in der Referenzdatenbank abzufragen:

```sql
SELECT * FROM Artikel
WHERE Artnr in (1102,1109,1512,1708,2001,2109,2112,2208,2306,2311)
ORDER BY Artnr ASC;
```

Die Ausgabe ist identisch zu ihrem Gegenstück in SQLite.

![Ergebnis der Überprüfung der Datensätze in MS SSMS](media/Validierung_SQLite2.png)

Somit ist davon auszugehen, dass beide Tabellen identisch sind. Die Ergebnisse dieser Analyse für die restlichen Tabellen (Anhang) zeigt, dass diese ebenfalls übereinstimmen. Somit ist bestätigt, dass die Datenbank für das Auslesen mithilfe von Python geeigent ist.

## 3.2 Python-Programmierung

Wie schon im Kapitel *Systementwurf* beschrieben, sind die Python-Anwendungen  modular aufgebaut: Kernfunktionen für den Datenbankzugriff und die Verwaltung der SQL-Anweisungen sind in eigenständigen Modulen gekapselt, während die Datenauswertung als schlanke Skripte implementiert sind, die diese Bausteine lediglich orchestrieren.

### 3.2.1 Verbindungslogik zur Datenbank (`dbparam.py`)

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

## 3.2.2 Verwaltung der SQL-Anweisungen (`queries.py`)

Das Modul `queries.py` dient der zentralen Verwaltung sämtlicher im Projekt verwendeter
SQL-Anweisungen. Alle Abfragen werden in einem Dictionary namens `SQL_QUERIES` hinterlegt, das die
SQL-Statements eindeutig identifizierbar und modular nutzbar macht.

### Struktur des Moduls

`SQL_QUERIES` ist wie folgt aufgebaut:

- **Schlüssel**  
  - kompakt, sprechend und eindeutig  
  - vollständig in **Großschreibung**  
  - Worttrennung über **Unterstriche**  

- **Werte**  
  - mehrzeilige SQL-Statements  
  - jeweils vollständig formulierte Abfragen  
  - werden unverändert in den Auswertungsskripten ausgeführt

Zur Veranschaulichung zeigt das folgende Codebeispiel einen Ausschnitt aus dem Anfang des Dictionary mit den SQL-Satements `GEBURTSTAGSKALENDER` und `MITARBEITER_WOHNORT`:

```python
SQL_QUERIES = {
    "GEBURTSTAGSKALENDER": """
        SELECT Name, Gebdat
        FROM Mitarbeiter
        ORDER BY
        CAST(substr(Gebdat, 5, 2) AS INTEGER),
        CAST(substr(Gebdat, 7, 2) AS INTEGER);
    """,

    "MITARBEITER_WOHNORT": """
        SELECT 
            M.Name AS Mitarbeiter, 
            M.Ort AS Wohnort, 
            S.Ort AS Arbeitsort
        FROM Mitarbeiter M
        JOIN Shop S ON M.Shop_ID = S.Shop_ID
        WHERE M.Ort != S.Ort;
    """,

    [...]
```

Die Auswertungsskripte importieren das Dictionary und greifen ausschließlich über den passenden
Schlüssel auf die benötigte Abfrage zu. Dadurch entfällt die Notwendigkeit, SQL-Strings in jedem
Skript separat zu pflegen und sie können bei Bedarf in weiteren Skripten wiederverwendet werden.

### Anpassung der SQL-Statements für SQLite

Die SQL-Anweisungen entsprechen nicht in allen Fällen ihren ursprünglichen Varianten aus der
MS-SQL-Server-Umgebung. Grund hierfür sind Unterschiede in den SQL-Dialekten von MS SQL-Server (Transact-SQL) und SQLite. Zum Ausdruck kommt dies im Projektkontext durch abweichende Datenypen und fehlende oder anders benannte SQL-Funkitonen. 

Ein exemplarisches Beispiel ist das Statement `GEBURTSTAGSKALENDER`. Das ursprüngliche Transact-SQL-Statement sieht folgendermaßen aus:

```sql
SELECT Name, gebdat
FROM Mitarbeiter
ORDER BY MONTH(gebdat), DAY(gebdat);
```

Dies musste angepasst werden. Zum einen besitzt das Attribut `gebdat` den Datentyp `date`, welcher in SQLite nicht vorhanden ist. Zum anderen werden für das Erstellen des Geburtstagskalenders der Mitarbeiter die Funktionen `MONTH()` und `DAY()` genutzt, welche in SQLite ebenfalls nicht zur Verfüfung stehen. Wie bereits im Kapitel *Datenbankmigration* beschrieben, wird `gebdat` in SQLite als `TEXT` im Format `YYYYMMDD` abgebildet. Da es zudem keine Funktionen wie `DAY()` oder `MONTH()` gibt, müssen Monat und Tag aus dem Text extrahiert werden:

```sql
CAST(substr(GebDat, 5, 2) AS INTEGER) AS Monat,
CAST(substr(GebDat, 7, 2) AS INTEGER) AS Tag
```

Diese Anpassung ermöglicht es, die fachliche Logik der MS SQL-Server-Aufgabe trotz genannter Abweichungen beizubehalten. Das vollständige SQL-Statement in SQLite sieht folgendermaßen aus:

```sql
SELECT Name, Gebdat
        FROM Mitarbeiter
        ORDER BY
        CAST(substr(Gebdat, 5, 2) AS INTEGER),
        CAST(substr(Gebdat, 7, 2) AS INTEGER);
```

## 3.2.3 Python-Anwendungen für die Sachdatenwiedergabe

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

## 3.2.4 Python-Anwendungen für Geodatenwiedergabe

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

# Nutzung der Software auf anderem Desktop

Dieses Kapitel beschreibt die Voraussetzungen und notwendigen Schritte zur Nutzung
und Wartung der entwickelten Softwarelösung auf einem anderen Desktop-Rechner.
Ziel ist es, die Übertragbarkeit der Projektartefakte sicherzustellen und eine
Weiterverwendung der Anwendungen unabhängig vom ursprünglichen Entwicklungsrechner
zu ermöglichen.

Die entwickelte Softwarelösung ist so aufgebaut, dass sie
auf anderen Windows-Arbeitsrechnern ausgeführt oder nachgebildet werden kann, sofern die im Kapitel
*Installation und Setup* beschriebenen Voraussetzungen erfüllt sind.

Für die Nutzung auf einem anderen Rechner sind folgende Schritte
erforderlich:

1. **Übertragung der Projektdateien**  
   Das vollständige Projektverzeichnis, bestehend aus den angefertigten Python-Skripten und -Modulen sowie der SQLite-Datenbankdatei
   wird auf den Zielrechner kopiert. Eine Installation im klassischen Sinne
   ist nicht notwendig.

2. **Anpassung systemabhängiger Pfade**  
   In der Datei `dbparam.py` sind Pfade zur SQLite-Datenbank, zum
   SpatiaLite-Verzeichnis sowie zur SpatiaLite-Erweiterungsdatei hinterlegt. Diese Pfade müssen auf dem Zielrechner
   überprüft und an die dortige Verzeichnisstruktur angepasst
   werden.

3. **Überprüfung der Laufzeitumgebung**  
   Vor der Ausführung der Anwendungen ist sicherzustellen, dass Python,
   die benötigten Python-Bibliotheken sowie SQLite und SpatiaLite korrekt
   installiert sind. Die Funktionsfähigkeit kann durch die Ausführung eines Python-Skripts überprüft werden.
   
   Empfohlen ist die Ausführung der Anwendungen:
   
   - `01_geburtstagskalender.py` für das Überprüfen der Funktionsfähigkeit des übertragenen Gesamtsystems. Die Anwendung funktioniert auch ohne SpatiaLite-Erweiterung, da keine räumlichen Funktionen im SQL-Statement verwendet werden. Zudem ist sie im *3.2.3 Python-Anwendungen für die Sachdatenwiedergabe* detalliert erklärt, was einen möglichen Fehlerfindungsprozess unterstützt.

   - `04_abstand_shops_zur_HTW.py` für das Überprüfen der Funktionsfähigkeit der SpatiaLite-Erweiterung. Die dort referenzierte SQL-Anweisung mit dem Schlüssel `ABSTAND_SHOPS_ZUR_HTW` enthält mehrere räumliche Funktionen, welche durch SpatiaLite bereitsgestellt werden. Sollte die Ausführung dieser Anwendung fehlschlagen, jedoch die von `01_geburtstagskalender.py` nicht, **kann** das Problem auf die SpatiaLite-Erweiterung eingegrenzt werden.

   **Anmerkung:** Es ist dennoch empfohlen für eine Lokation auftretender Fehlern, die während der Laufzeit der Anwendungen auftretenden Fehlermeldungen heranzuziehen. Fehlende oder fehlerhaft installierte Python-Bibliotheken sind ebenfalls auf diesem Weg identifizierbar.

Nach Durchführung dieser Schritte können die Python-Anwendungen auf dem neuen
Rechner ausgeführt werden. Die Programme verhalten sich dabei
identisch zur ursprünglichen Entwicklungsumgebung, da alle datenbankseitigen
Operationen vollständig innerhalb der SQLite-Datei gekapselt sind.

# Anpassung und Erweiterung der Software

Die entwickelte Softwarelösung ist modular aufgebaut und ermöglicht sowohl Anpassungen als auch Erweiterungen, ohne dass die bestehende Gesamtarchitektur verändert werden muss. Durch die klare Trennung von Datenbankzugriff, SQL-Verwaltung und Auswertungsskripten können neue Anforderungen schrittweise umgesetzt und bestehende Funktionalitäten gezielt angepasst werden.

## Anpassung an neue Systemumgebungen

Systemabhängige Parameter sind zentral im Modul `dbparam.py` gekapselt. Änderungen
an Speicherorten der Datenbankdatei oder der SpatiaLite-Erweiterung können durch
Anpassung der dort hinterlegten Pfade vorgenommen werden, ohne dass Änderungen an
den eigentlichen Auswertungsskripten notwendig sind (siehe Kapitel *4.2.2 Konfiguration der Datenbankschnittstelle*). Dadurch bleibt der Wartungsaufwand bei einem Wechsel der Arbeitsumgebung gering.

## 6.2 Erweiterung der SQL-Verwaltung

Neue SQL-Anweisungen können durch Ergänzung des Dictionaries ``SQL_QUERIES`` im Modul ``queries.py`` integriert werden. Jede Abfrage wird dabei unter einem eindeutigen, sprechenden Schlüssel abgelegt und kann von bestehenden oder neuen Python-Skripten referenziert werden.

Zur Demonstration wird eine einfache SELECT-Abfrage ergänzt:

```python
"ALLES_SELEKTIEREN": """
        SELECT * 
        FROM Mitarbeiter;
    """
```
Wie bereits im Kapitel *3.2.3 Python-Anwendungen für die Sachdatenwiedergabe* beschrieben, muss diese Abfrage lediglich im jeweiligen Auswertungsskript über ihren Schlüssel referenziert werden. Das folgende Beispiel zeigt ein demonstratives Skript namens `00_beispiel.py`:

```python
# Beispiel zur Demonstration des Einbindens zusätzlicher SQL-Statements

# Import der notwendigen Bibliotheken
import pandas as pd
from dbparam import connection
from queries import SQL_QUERIES

# Auswahl des SQL-Statements
query = SQL_QUERIES['ALLES_SELEKTIEREN']

# Einlesen der Tabelle unter Verwendung des Kontextmanagers
with connection() as conn:
    df = pd.read_sql(query, conn)

# Ausgabe der Daten
print("\n Die gesamte Tabelle Mitarbeiter:\n")
print(df)
```
Die neue SQL-Anweisung wird dabei an folgender Stelle referenziert:

```python
query = SQL_QUERIES['ALLES_SELEKTIEREN']
```

Alternativ ist es möglich, ein vollständig neues Dictionary für SQL-Anweisungen zu verwenden. Dazu wird eine neue Python-Datei angelegt, in der das Dictionary definiert ist, beispielsweise:

```python
NEW_SQL_QUERIES = {
    "ALLES_SELEKTIEREN": """
        SELECT * FROM Mitarbeiter;
    """
}
```
Dieses Dictionary wird in einer Datei `new_queries.py` gespeichert und kann anschließend in einem Auswertungsskript importiert werden:

```python
from new_queries import NEW_SQL_QUERIES
```

Das Auswertungsskript 00_beispiel.py muss dann entsprechend angepasst werden:

```python
# Beispiel zur Demonstration des Einbindens zusätzlicher SQL-Statements

import pandas as pd
from dbparam import connection
from new_queries import NEW_SQL_QUERIES

query = NEW_SQL_QUERIES['ALLES_SELEKTIEREN']

with connection() as conn:
    df = pd.read_sql(query, conn)

print("\n Die gesamte Tabelle Mitarbeiter:\n")
print(df)
```

In beiden Varianten ist ersichtlich, dass nur minimale Änderungen erforderlich sind, um neue SQL-Abfragen in das bestehende System zu integrieren.

## 6.3 Erweiterung der Datenverarbeitung

Zusätzliche Auswertungen oder Visualisierungen können als eigenständige Python-Skripte umgesetzt oder durch Anpassung bestehender Skripte realisiert werden. Das Kapitel *3.2.3 Python-Anwendungen für die Sachdatenwiedergabe* dient dabei als Orientierung. Neben der Datenbankabfrage können die eingelesenen Daten mithilfe von pandas auf Anwendungsebene weiterverarbeitet und angepasst werden. Um dies exemplarisch zu demonstrieren, wird der durch das Skript `01_geburtstagskalender.py` erzeugte Geburtstagskalender erweitert.

Das Attribut ``Gebdat``, das als Text im Format ``YYYYMMDD`` vorliegt, wird dabei in separate Spalten für Jahr, Monat und Tag zerlegt. Die hierfür benötigten pandas-Methoden werden nach dem ``with``-Block angewendet.

```python
# Zerlegen des Datumsfeldes (YYYYMMDD) in Jahr, Monat und Tag
df["Jahr"]  = df["Gebdat"].str[0:4].astype(int)
df["Monat"] = df["Gebdat"].str[4:6].astype(int)
df["Tag"]   = df["Gebdat"].str[6:8].astype(int)
```

Der vollständige Code des erweiterten Skripts lautet:

```python
#abgeleitet von MS SQL 1 - Aufbau einer OLTP-Datenbank im MS SQL Server - Aufgabe 8

import pandas as pd
from dbparam import connection
from queries import SQL_QUERIES

query = SQL_QUERIES['GEBURTSTAGSKALENDER']

with connection() as conn:
    df = pd.read_sql(query, conn)

df["Jahr"]  = df["Gebdat"].str[0:4].astype(int)
df["Monat"] = df["Gebdat"].str[4:6].astype(int)
df["Tag"]   = df["Gebdat"].str[6:8].astype(int)

print("\n Die Geburtstage der Mitarbeiter - sortiert nach Monat und Tag:\n")
print(df.to_string(index=False))
```

Die kartografische Darstellungsweise der Geodaten kann gezielt weiter angepasst werden. Exemplarisch wird dies am Skript ``07_geometrie_darstellen.py`` gezeigt. Die zuvor einheitliche Darstellung der Bundesländer wird erweitert, sodass jede Fläche eine eigene Farbe erhält. Dies erfolgt durch die Nutzung zusätzlicher Parameter der GeoPandas-/Matplotlib-Funktion ``.plot()``.

Zuvor wurde diese ohne die Angabe weiterer Parameter aufgerufen:

```python
# Visualisierung der Geodaten
gdf1.plot()
gdf2.plot()
plt.show()
```

Die neuen Parameter werden einfach der gewünschten `.plot()`-Funktion übergeben:

```python
gdf1.plot(
    column="Bundesland",
    categorical=True,
    edgecolor="black",
    linewidth=0.5
)
gdf2.plot()
plt.show()
```

Die Ausführung des Skriptes nun folgendes Ergebnis:

![neu eingefärbte Bundesländer](media\bunte_Bundeslaender.png)

# Testen der Software

Dieses Kapitel beschreibt die Überprüfung der entwickelten Softwarelösung hinsichtlich ihrer
fachlichen Korrektheit und Vergleichbarkeit mit der Referenzumgebung aus den MS-SQL-Server-Übungen
(MS SSMS). Ziel ist es, nachvollziehbar zu dokumentieren, ob (1) die Migration der Datenbank nach
SQLite/SpatiaLite vollständig und konsistent erfolgt ist und ob (2) die implementierten
SQL-Abfragen und Python-Auswertungen Ergebnisse liefern, die den Resultaten aus der MS-SQL-Umgebung
entsprechen.

Die Tests sind so gewählt, dass sie die zuvor definierten Anforderungen abdecken:
- Datenbankbezogen: **Tabellenstruktur, Relationen, inhaltliche Übereinstimmung** (ND1–ND3),
  sowie funktionale Anforderungen wie **Aggregation/Views, räumliche Abfragen, Berechnungen und Indizes**
  (FD1–FD5).
- Python-bezogen: **Datenbankverbindung inkl. SpatiaLite, Ausführung von SQL, tabellarische Ausgabe
  sowie Visualisierung von Geodaten** (FP1–FP6).

## Referenzdaten

Als Referenz dienen die Ergebnisse der im Modul *Datenbanktechnologien* durchgeführten Übungen in
Microsoft SQL Server (MS SSMS). Für jeden Testfall wird eine fachlich äquivalente Abfrage in der
neuen Umgebung (SQLite/SpatiaLite + Python) ausgeführt und mit dem Resultat aus MS SSMS verglichen.

Der Vergleich erfolgt abhängig vom Testtyp über:
- **exakte Übereinstimmung** (z. B. Zeilenzahlen, Join-Ergebnisse, Aggregationen),
- **stichprobenbasierte Übereinstimmung** bei großen Tabellen (z. B. Zufallsstichproben),
- **toleranzbasierte Übereinstimmung** bei räumlichen Berechnungen (z. B. Fläche/Distanz),
  sofern unterschiedliche Rechenmodelle/Einheiten zwischen den Systemen auftreten können.

## Testfälle

Die folgenden Tabellen listen die Testfälle auf. Jeder Testfall ist einer Kategorie
zugeordnet und referenziert explizit die zugrundeliegenden Anforderungen aus der
Anforderungsanalyse.

### Testfälle zur Überprüfung der Datenbankmigration

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T01 | Migration/Schema | Tabellen vorhanden | ND1 | identische Tabellen |
| T02 | Migration/Schema | PKs korrekt | ND2 | PK wie MS |
| T03 | Migration/Daten | Zeilenzahlen je Tabelle | ND3 | Counts identisch |

### Testfälle zur Überprüfung der Datenbankintegrität

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T04 | Integrität | PK eindeutig (einfach) | ND2 | 0 Duplikate |
| T05 | Integrität | PK eindeutig (zus.) | ND2 | 0 Duplikate |
| T06 | Integrität | FK-Orphans | ND2 | 0 Orphans |

### Testfälle zur Überprüfung der Daten

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T07 | Sachdaten | Geburtstagskalender | FD4, FP3, FP5 | gleiche Reihenfolge |
| T08 | Sachdaten | Join Mitarbeiter–Shop | FD4, FP3, FP4 | gleiche Ergebnismenge |
| T09 | Sachdaten | Aggregation / View | FD4, FP3 | gleiche Summen |
| T10 | Sachdaten | Verkauf Filter / Aggregat | FD4, FP3 | gleiche Werte |
| T11 | Räumlich | Geometrien nicht NULL | FD1 | COUNT NULL | identisch / 0 |
| T12 | Räumlich | Shops in Bundesland | FD2, FP3 | räumliche Query | gleiche Shop-Liste |
| T13 | Räumlich | Nachbar-Bundesländer | FD2, FP3 | gleiche Liste |
| T14 | Räumlich | Flächenberechnung BL | FD3, FP3 | innerhalb Toleranz |
| T15 | Räumlich | Distanz Shop–HTW | FD3, FP3 | innerhalb Toleranz |

### Testfälle zur Überprüfung der Systemintegration

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T16 | Python | SpatiaLite geladen | FP1, FP2 | keine Exception |
| T17 | Python/Geo | WKB → Shapely → Plot | FP6 | Plot ohne Fehler |
| T18 | Optimierung | Indexwirkung | FD5 | Index sichtbar |

## Testergebnisse

Nach Abschluss der Migration wird überprüft, ob die Datenbank vollständig und korrekt in
das neue Zielsystem überführt wurde. Diese Prüfung dient der Validierung der strukturellen
Integrität der migrierten Datenbank und entspricht den Testfällen **T01 (Vorhandensein der
Tabellen)** und **T02 (Primärschlüsseldefinitionen)**.

Für die schematische Analyse wird ein ER-Diagramm der SQLite-Datenbank herangezogen. Da SQLite
keine native Funktion zur Generierung von ER-Diagrammen bereitstellt, wird hierfür eine
Drittsoftware eingesetzt. Zum Einsatz kommt die **DBeaver Community Edition**, ein Open-Source-Client
zur Verwaltung verschiedener Datenbanksysteme. Alternativ können auch andere Werkzeuge verwendet
werden, die ER-Diagramme auf Basis einer Datenbankverbindung erzeugen, beispielsweise DBVisualizer.

Die folgende Abbildung zeigt das mithilfe von DBeaver erzeugte ER-Diagramm in der Martin-Notation:

![ER-Diagramm des Datenbankschemas](media/ER_Diagramm_SQLite_DB.png)

Zusätzlich lassen sich in DBeaver die definierten Constraints einsehen. Durch Auswahl einer
Beziehung im ER-Diagramm werden die beteiligten Attribute sowie deren Kardinalitäten angezeigt.

![ER-Diagramm mit gewählter Beziehung](media/ER_Diagramm_Beziehung.png)

Das ER-Diagramm zeigt, dass das Schema der SQLite-Datenbank – mit Ausnahme der Datentypen –
strukturell identisch zur ursprünglichen Datenbank in Microsoft SQL Server ist. Insbesondere sind
alle Tabellen vorhanden, die Primärschlüssel korrekt definiert und die Fremdschlüsselrelationen
vollständig abgebildet. Damit gelten die Testfälle **T01** und **T02** als erfolgreich
durchgeführt.

### Validierung der Tabelleninhalte mittels Aggregat-Signaturen

Die inhaltliche Überprüfung der migrierten Tabellen erfolgt nicht durch manuelle Sichtproben,
sondern ausschließlich über aggregierte Kennzahlen (Aggregat-Signaturen). Dieses Vorgehen ist
insbesondere für große Tabellen geeignet und erlaubt eine reproduzierbare, systematische
Validierung der Datenübertragung.

Die zugrunde liegende Annahme ist, dass beim Migrationsprozess Abweichungen
auf Zeilenebene zwangsläufig zu Veränderungen aggregierter Kennzahlen führen würden. Stimmen
diese Kennzahlen zwischen Referenz- und Zielsystem überein, ist mit hoher Wahrscheinlichkeit von
einer vollständigen und konsistenten Migration auszugehen.

Die Ausgabe der Kennzahlen wird beispielhaft an der Überprüfung der Tabelle *Artikel* vorgenommen. Das folgende SQL-Statement wird zunächst in MS SSMS ausgeführt:

```sql
SELECT
  COUNT(*)                          AS cnt_rows,
  COUNT(DISTINCT Artnr)             AS cnt_distinct_pk,
  MIN(Preis)                        AS min_preis,
  MAX(Preis)                        AS max_preis,
  ROUND(SUM(CAST(Preis AS float)), 2) AS sum_preis,
  SUM(CASE WHEN Marke IS NULL THEN 1 ELSE 0 END)       AS null_marke,
  SUM(CASE WHEN Bezeichnung IS NULL THEN 1 ELSE 0 END) AS null_bezeichnung,
  SUM(CASE WHEN Artgruppe IS NULL THEN 1 ELSE 0 END)   AS null_artgruppe
FROM Artikel;
```

Um die Funktionsweise zu erläutern wird dieses Statement zeilenweise erklärt. Es beginnnt mit

```sql
  COUNT(*)                          AS cnt_rows,
```

, welche die Zeilenzahlen der Tabelle wiedergibt. Gefolgt von:

```sql
  COUNT(DISTINCT Artnr)             AS cnt_distinct_pk,
```

, um die eindeutigen Primärschlüsselattribute festzustellen. Stimmen beide ausgegebenen Werte überein ist die Eindeutigkeit des Primärschlüsselattributs gegeben.
Mithilfe der der beiden Zeilen

```sql
  MIN(Preis)                        AS min_preis,
  MAX(Preis)                        AS max_preis,
```

werden der jeweils höchste und niedrigste Wert des Attributes *Preis* ausgegben, um Ausreißer festzustellen. 

```sql
  SUM(CASE WHEN Marke IS NULL THEN 1 ELSE 0 END)       AS null_marke,
  SUM(CASE WHEN Bezeichnung IS NULL THEN 1 ELSE 0 END) AS null_bezeichnung,
  SUM(CASE WHEN Artgruppe IS NULL THEN 1 ELSE 0 END)   AS null_artgruppe
```

Anschließend wird die Gesamtsumme aller Preise berechnet:

```sql
  ROUND(SUM(CAST(Preis AS float)), 2) AS sum_preis,
```

und letztendlich werden unter Nutzung des CASE-Statements NULL-Werte der Attribute *Marke*, *Bezeichnung* und *Artgruppe* festgestellt. Das Ausführen des gesamten Statements erzeugt folgendes Resultset:

![ER-Diagramm mit gewählter Beziehung](media/Artikel_Vali_SSMS.png)

Um Vergleichswerte zu generieren wird das für die Ausgabe genutzte SQL-Statement von T-SQL auf SQLite angepasst:

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT Artnr) AS cnt_distinct_pk,
  MIN(Preis) AS min_preis,
  MAX(Preis) AS max_preis,
  ROUND(SUM(CAST(Preis AS REAL)), 2) AS sum_preis_r2,
  SUM(CASE WHEN Marke IS NULL THEN 1 ELSE 0 END) AS null_marke,
  SUM(CASE WHEN Bezeichnung IS NULL THEN 1 ELSE 0 END) AS null_bezeichnung,
  SUM(CASE WHEN Artgruppe IS NULL THEN 1 ELSE 0 END) AS null_artgruppe
FROM Artikel;
```

Die Ausführung werfolgt in DB Brwoser für SQLite und erzeugt folgende Ausgabe:

![ER-Diagramm mit gewählter Beziehung](media/Artikel_Vali_SQLite.png)

Die aggregierten Kennzahlen in Referenz- und Zielsystem gleichen sich, somit ist mit hoher Wahrscheinlichkeit davon auszugehen, dass die Tabelle vollständig und korrekt übertragen wurde.

### Validierung der Tabelle *Mitarbeiter*

Die Validierung der Tabelle *Mitarbeiter* erfolgt analog zur zuvor beschriebenen
Aggregat-Signatur der Tabelle *Artikel*. Ziel ist es, die Vollständigkeit und
inhaltliche Übereinstimmung der migrierten Personaldaten zwischen der Referenzumgebung
(MS SSMS) und dem Zielsystem (SQLite) zu überprüfen. Die Prüfung adressiert die
Testfälle **T03 (Vollständigkeit der Daten)** sowie **T04 (Integrität des Primärschlüssels)**.

Für die Überprüfung wird in **MS SSMS** folgendes SQL-Statement ausgeführt:

```sql
SELECT
  COUNT(*)                      AS cnt_rows,
  COUNT(DISTINCT Mitnr)         AS cnt_distinct_pk,
  MIN(Gehalt)                   AS min_gehalt,
  MAX(Gehalt)                   AS max_gehalt,
  SUM(CAST(Gehalt AS bigint))   AS sum_gehalt,
  SUM(CASE WHEN Gebdat IS NULL THEN 1 ELSE 0 END) AS null_gebdat,
  SUM(CASE WHEN Shop_ID IS NULL THEN 1 ELSE 0 END) AS null_shopid
FROM Mitarbeiter;
```

Zur Generierung der Vergleichswerte wird in SQLite das äquivalente Statement ausgeführt:

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT Mitnr) AS cnt_distinct_pk,
  MIN(Gehalt) AS min_gehalt,
  MAX(Gehalt) AS max_gehalt,
  SUM(COALESCE(Gehalt, 0)) AS sum_gehalt,
  SUM(CASE WHEN Gebdat IS NULL THEN 1 ELSE 0 END) AS null_gebdat,
  SUM(CASE WHEN Shop_ID IS NULL THEN 1 ELSE 0 END) AS null_shopid
FROM Mitarbeiter;
```

Der Vergleich enthält neben der Zeilenanzahl und der Anzahl eindeutiger
Primärschlüsselwerte (*Mitnr*) auch Kennzahlen zum Attribut *Gehalt*
(Minimum, Maximum und Summe) sowie die Anzahl von `NULL`-Werten in den
Attributen *Gebdat* und *Shop_ID*. 

Die Anpassungen zwischen beiden SQL-Dialekten betreffen hierbei
ausschließlich die Summenbildung: In MS SSMS wird *Gehalt* explizit auf
`bigint` gecastet, während in SQLite `COALESCE(Gehalt, 0)` verwendet wird,
um mögliche `NULL`-Werte bei der Summation neutral zu behandeln.
 
Die ermittelten Kennzahlen stimmen zwischen MS SSMS und SQLite überein.
Damit ist davon auszugehen, dass die Tabelle *Mitarbeiter* vollständig
und konsistent in das Zielsystem überführt wurde.

| Kennzahl           | MS SSMS     | SQLite     |
|--------------------|-------------|------------|
| `cnt_rows`         | 52 | 52 |
| `cnt_distinct_pk`  | 52 | 52 |
| `min_gehalt`       | 1060 | 1060 |
| `max_gehalt`       | 4310 | 4310 |
| `sum_gehalt`       | 138935 | 138935 |
| `null_gebdat`      | 0 | 0 |
| `null_shopid`      | 0 | 0 |

Die Testfälle **T03** und **T04** gelten für diese Tabelle als erfolgreich durchgeführt.

### Validierung der Tabelle *Bestand*

Die Validierung der Tabelle *Bestand* erfolgt analog zu den zuvor beschriebenen
Aggregat-Signaturen der Tabellen *Artikel* und *Mitarbeiter*. Ziel ist es, die
Vollständigkeit und inhaltliche Konsistenz der Bestandsdaten zwischen der
Referenzumgebung (MS SSMS) und dem Zielsystem (SQLite) zu überprüfen. Die Prüfung
adressiert die Testfälle **T03 (Vollständigkeit der Daten)** sowie **T05
(Integrität zusammengesetzter Primärschlüssel)**.

Die Tabelle *Bestand* besitzt keinen einfachen Primärschlüssel, sondern einen
zusammengesetzten Primärschlüssel bestehend aus den Attributen *Artnr* und
*Shop_ID*. Zur Überprüfung der Eindeutigkeit dieser Schlüsselkombination wird
daher die Anzahl unterschiedlicher Kombinationen aus beiden Attributen ermittelt.

Für die Überprüfung wird in **MS SSMS** folgendes SQL-Statement ausgeführt:

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT CONCAT(Artnr, '-', Shop_ID)) AS cnt_distinct_pk_combo,
  MIN(Menge) AS min_menge,
  MAX(Menge) AS max_menge,
  SUM(CAST(COALESCE(Menge, 0) AS bigint)) AS sum_menge,
  SUM(CASE WHEN Menge IS NULL THEN 1 ELSE 0 END) AS null_menge
FROM Bestand;
```

Zur Erzeugung der Vergleichswerte wird in SQLite das äquivalente Statement
ausgeführt:


```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT CAST(Artnr AS TEXT) || '-' || CAST(Shop_ID AS TEXT)) AS cnt_distinct_pk_combo,
  MIN(Menge) AS min_menge,
  MAX(Menge) AS max_menge,
  SUM(COALESCE(Menge, 0)) AS sum_menge,
  SUM(CASE WHEN Menge IS NULL THEN 1 ELSE 0 END) AS null_menge
FROM Bestand;
```

Der Vergleich enthält neben der Zeilenanzahl auch die Anzahl eindeutiger
Primärschlüsselkombinationen (*Artnr*, *Shop_ID*), wodurch die Eindeutigkeit des
zusammengesetzten Primärschlüssels überprüft wird. Zusätzlich werden zentrale
Kennzahlen des Attributs *Menge* (Minimum, Maximum und Summe) sowie die Anzahl
möglicher `NULL`-Werte ermittelt.

Die Unterschiede zwischen beiden SQL-Dialekten betreffen ausschließlich die
technische Umsetzung der Schlüsselaggregation und der Summenbildung. In
MS SSMS wird die Schlüsselprüfung über `CONCAT()` realisiert und die Summation
explizit auf `bigint` gecastet, während in SQLite eine Zeichenkettenverkettung
sowie `COALESCE(Menge, 0)` verwendet werden, um `NULL`-Werte neutral zu behandeln.

#### Gegenüberstellung der Kennzahlen

| Kennzahl                    | MS SSMS        | SQLite        |
|-----------------------------|----------------|---------------|
| `cnt_rows`                  | 3800 | 3800 |
| `cnt_distinct_pk_combo`     | 3800  | 3800 |
| `min_menge`                 | 4  | 4 |
| `max_menge`                 | 150  | 150 |
| `sum_menge`                 | 291782  | 291792 |
| `null_menge`                | 0 | 0 |

Die ermittelten Kennzahlen stimmen zwischen MS SSMS und SQLite vollständig
überein. Damit ist davon auszugehen, dass die Tabelle *Bestand* vollständig,
konsistent und ohne Verletzung der zusammengesetzten Primärschlüssel in das
Zielsystem übertragen wurde. Die Testfälle **T03** und **T05** gelten für diese
Tabelle als erfolgreich durchgeführt.

### Validierung der Tabelle *Verkauf*

Die Tabelle *Verkauf* stellt die größte und inhaltlich komplexeste Tabelle der Datenbank dar.
Sie besitzt einen zusammengesetzten Primärschlüssel, bestehend aus den Attributen *Artnr*,
*Shop_ID* und *Datum*. Entsprechend liegt der Fokus der Validierung auf der Überprüfung der
Eindeutigkeit dieser Schlüsselkombination sowie auf der Konsistenz zentraler mengen- und
preisbezogener Kennzahlen. Die Prüfung adressiert die Testfälle **T03 (Vollständigkeit der Daten)**
und **T05 (Integrität zusammengesetzter Primärschlüssel)**.

Für die Referenzumgebung **MS SSMS** wird folgendes SQL-Statement ausgeführt:

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT CONCAT(Artnr, '-', Shop_ID, '-', CONVERT(varchar(32), Datum, 126))) AS cnt_distinct_pk_combo,
  MIN(Datum) AS min_datum,
  MAX(Datum) AS max_datum,
  MIN(Menge) AS min_menge,
  MAX(Menge) AS max_menge,
  SUM(CAST(COALESCE(Menge, 0) AS bigint)) AS sum_menge,
  ROUND(SUM(CAST(COALESCE(Verkaufspreis, 0) AS float)), 2) AS sum_verkaufspreis_r2,
  ROUND(SUM(CAST(COALESCE(Verkaufspreis, 0) AS float) * CAST(COALESCE(Menge, 0) AS float)), 2) AS sum_umsatz_r2,
  SUM(CASE WHEN Verkaufspreis IS NULL THEN 1 ELSE 0 END) AS null_verkaufspreis,
  SUM(CASE WHEN Menge IS NULL THEN 1 ELSE 0 END) AS null_menge
FROM Verkauf;
```

Zur Ermittlung der Vergleichswerte wird in SQLite das folgende dialektspezifisch angepasste Statement ausgeführt:

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT CAST(Artnr AS TEXT) || '-' || CAST(Shop_ID AS TEXT) || '-' || CAST(Datum AS TEXT)) AS cnt_distinct_pk_combo,
  MIN(Datum) AS min_datum,
  MAX(Datum) AS max_datum,
  MIN(Menge) AS min_menge,
  MAX(Menge) AS max_menge,
  SUM(COALESCE(Menge, 0)) AS sum_menge,
  ROUND(SUM(COALESCE(Verkaufspreis, 0.0)), 2) AS sum_verkaufspreis_r2,
  ROUND(SUM(COALESCE(Verkaufspreis, 0.0) * COALESCE(Menge, 0)), 2) AS sum_umsatz_r2,
  SUM(CASE WHEN Verkaufspreis IS NULL THEN 1 ELSE 0 END) AS null_verkaufspreis,
  SUM(CASE WHEN Menge IS NULL THEN 1 ELSE 0 END) AS null_menge
FROM Verkauf;
```

Der Vergleich umfasst neben der Gesamtanzahl der Datensätze auch die Anzahl eindeutiger
Primärschlüsselkombinationen (*Artnr*, *Shop_ID*, *Datum*), wodurch die Integrität des
zusammengesetzten Primärschlüssels überprüft wird. Zusätzlich werden zeitliche Randwerte
(*min_datum*, *max_datum*), mengenbezogene Kennzahlen (*min_menge*, *max_menge*, *sum_menge*),
preisbezogene Kennzahlen (*sum_verkaufspreis*) sowie der daraus abgeleitete Gesamtumsatz
(*sum_umsatz*) betrachtet. Ergänzend wird die Anzahl möglicher `NULL`-Werte in den Attributen
*Verkaufspreis* und *Menge* ermittelt.

Die Unterschiede zwischen den SQL-Dialekten betreffen ausschließlich die technische Umsetzung.
In MS SSMS wird die Schlüsselkombination mittels `CONCAT()` und einer expliziten
Datumsumwandlung erzeugt, während SQLite eine Zeichenkettenverkettung mit `CAST()` verwendet.
Bei der Aggregation numerischer Werte werden in beiden Systemen `COALESCE`-Konstrukte genutzt,
um `NULL`-Werte neutral zu behandeln; zusätzlich sind in MS SSMS explizite Typkonvertierungen
auf `bigint` bzw. `float` erforderlich.

#### Gegenüberstellung der Kennzahlen

| Kennzahl                  | MS SSMS        | SQLite        |
|---------------------------|----------------|---------------|
| `cnt_rows`                | 310547  | 310547 |
| `cnt_distinct_pk_combo`   | 310547  | 310547 |
| `min_datum`               | 2023-01-02  | 20230102 |
| `max_datum`               | 2023-04-29  | 20230429 |
| `min_menge`               | 5  | 5 |
| `max_menge`               | 120  | 120 |
| `sum_menge`               | 19450947  | 19450947 |
| `sum_verkaufspreis_r2`    | 640179,17  | 640179,17 |
| `sum_umsatz_r2`           | 40088798,1  | 40088798,1 |
| `null_verkaufspreis`      | 0  | 0 |
| `null_menge`              | 0  | 0 |

Die aggregierten Kennzahlen stimmen zwischen MS SSMS und SQLite vollständig überein. Damit ist
davon auszugehen, dass die Tabelle *Verkauf* vollständig, konsistent und ohne Verletzung des
zusammengesetzten Primärschlüssels in das Zielsystem übertragen wurde. Die Testfälle **T03**
und **T05** gelten für diese Tabelle als erfolgreich durchgeführt.

### Validierung der Tabelle Geografie

Die Validierung der Tabelle *Geografie* erfolgt getrennt von der Implementierung und dient der
Überprüfung, ob die räumlichen und attributiven Inhalte der Tabelle vollständig und konsistent
von der Referenzdatenbank in Microsoft SQL Server nach SQLite/SpatiaLite übertragen wurden.
Da es sich um eine Geodatentabelle handelt, kombiniert die Prüfung quantitative Kennzahlen mit
einer räumlichen Plausibilitätskontrolle.

#### Quantitative Validierung mittels Kennzahlen

Zunächst werden aggregierte Kennzahlen ermittelt, um die Vollständigkeit der Tabelle sowie die
Konsistenz der Schlüssel- und Attributwerte zu überprüfen. Dazu wird in beiden Systemen ein
äquivalentes SQL-Statement ausgeführt.

**MS SSMS:**

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT Land_ID) AS cnt_distinct_pk,
  SUM(CASE WHEN Flaeche IS NULL THEN 1 ELSE 0 END) AS null_geom,
  COUNT(DISTINCT Staat) AS cnt_staat,
  COUNT(DISTINCT Bundesland) AS cnt_bundesland
FROM Geografie;
```

**SQLite:**

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT Land_ID) AS cnt_distinct_pk,
  SUM(CASE WHEN Flaeche IS NULL THEN 1 ELSE 0 END) AS null_geom,
  COUNT(DISTINCT Staat) AS cnt_staat,
  COUNT(DISTINCT Bundesland) AS cnt_bundesland
FROM Geografie;
```

Der Vergleich umfasst neben der Gesamtanzahl der Datensätze auch die Anzahl eindeutiger
Primärschlüsselwerte (*Land_ID*), wodurch die Eindeutigkeit des Primärschlüssels überprüft wird.
Zusätzlich wird die Anzahl von Datensätzen ohne zugeordnete Geometrie ermittelt.

Dabei ist zu berücksichtigen, dass in der Tabelle *Geografie* ein Datensatz bewusst ohne
Geometrie hinterlegt ist. Entscheidend ist daher, dass die Anzahl der `NULL`-Geometrien zwischen
Referenz- und Zielsystem übereinstimmt.

Die Anzahl unterschiedlicher Werte in den Attributen *Staat* und *Bundesland* dient als
Plausibilitätskennzahl für die fachliche Struktur der Tabelle.

| Kennzahl          | MS SSMS        | SQLite        |
|-------------------|----------------|---------------|
| `cnt_rows`        | 47  | 47 |
| `cnt_distinct_pk` | 47  | 47 |
| `null_geom`       | 1              | 1             |
| `cnt_staat`       | 4  | 4 |
| `cnt_bundesland`  | 47  | 47 |

Die aggregierten Kennzahlen stimmen zwischen MS SSMS und SQLite vollständig überein. Insbesondere
wird der erwartete Datensatz ohne Geometrie in beiden Systemen identisch abgebildet. Damit ist
davon auszugehen, dass die Tabelle *Geografie* vollständig und korrekt übertragen wurde.
Die Testfälle **T01**, **T03** und **T11** gelten damit für diese Tabelle als erfolgreich
durchgeführt.

#### Räumliche Plausibilitätsprüfung

Ergänzend zur quantitativen Analyse wird eine visuelle Prüfung der Geometrien vorgenommen. Dazu
wird die Tabelle *Geografie* in einer GIS-Umgebung (QGIS) geladen. Ziel dieser Prüfung ist es, sicherzustellen, dass die
vorhandenen Geometrien fachlich plausibel sind, korrekt positioniert vorliegen und keine
offensichtlichen räumlichen Artefakte (z. B. verschobene, invertierte oder degenerierte Flächen)
enthalten.

Im QGIS wird zunächst eine Verbindung zur SQLite-Datenbank hergestellt.

![ER-Diagramm mit gewählter Beziehung](media/Add_DBC_QGIS.png)

Die entsprechende Tabelle wird anschließend aus der Baumstruktur mittels eines Doppelklicks als Layer hinzugefügt.

![ER-Diagramm mit gewählter Beziehung](media/Add_Layer_QGIS.png)

Zur Überprüfung der Lagegenauigkeit wird OpenStreetMap als Grundkarte hinzugefügt. Die untenstehende Abbildung zeigt die dargestellten Geometrien.

![ER-Diagramm mit gewählter Beziehung](media/Map_QGIS.png)

Die visuelle Kontrolle bestätigt, dass alle vorhandenen Flächengeometrien korrekt dargestellt
werden und die räumliche Lage der Bundesländer den fachlichen Erwartungen entspricht. Der
Datensatz ohne Geometrie wird erwartungsgemäß nicht visualisiert.

### Validierung der Tabelle Shop

Die Validierung der Tabelle *Shop* dient der Überprüfung, ob die attributiven Inhalte sowie die
punktförmigen Geometrien der Shops vollständig und konsistent von der Referenzdatenbank in
Microsoft SQL Server nach SQLite/SpatiaLite übertragen wurden. Analog zur Tabelle *Geografie*
erfolgt die Prüfung durch eine Kombination aus quantitativer Kennzahlenanalyse und räumlicher
Plausibilitätskontrolle.

#### Quantitative Validierung mittels Kennzahlen

Zunächst werden aggregierte Kennzahlen herangezogen, um die Vollständigkeit der Tabelle, die
Eindeutigkeit des Primärschlüssels sowie die Konsistenz der relevanten Attribute zu überprüfen.
Hierfür werden in beiden Systemen äquivalente SQL-Statements ausgeführt.

**MS SSMS:**

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT Shop_ID) AS cnt_distinct_pk,
  SUM(CASE WHEN Coordinate IS NULL THEN 1 ELSE 0 END) AS null_geom,
  COUNT(DISTINCT Land_ID) AS cnt_land,
  COUNT(DISTINCT Ort) AS cnt_ort
FROM Shop;
```

```sql
SELECT
  COUNT(*) AS cnt_rows,
  COUNT(DISTINCT Shop_ID) AS cnt_distinct_pk,
  SUM(CASE WHEN Coordinate IS NULL THEN 1 ELSE 0 END) AS null_geom,
  COUNT(DISTINCT Land_ID) AS cnt_land,
  COUNT(DISTINCT Ort) AS cnt_ort
FROM Shop;
```

Der Vergleich umfasst die Gesamtanzahl der Datensätze sowie die Anzahl eindeutiger
Primärschlüsselwerte (Shop_ID), womit die Eindeutigkeit des Primärschlüssels überprüft wird.
Darüber hinaus wird die Anzahl von Datensätzen ohne zugeordnete Punktgeometrie ermittelt.
Da jeder Shop fachlich eindeutig lokalisiert sein muss, wird erwartet, dass keine
NULL-Geometrien vorliegen.


| Kennzahl          | MS SSMS | SQLite |
|-------------------|---------|--------|
| `cnt_rows`        | 21      | 21     |
| `cnt_distinct_pk` | 21      | 21     |
| `null_geom`       | 0       | 0      |
| `cnt_land`        | 11 | 11 |
| `cnt_ort`         | 20 | 20 |

Die ermittelten Kennzahlen stimmen zwischen MS SSMS und SQLite vollständig überein. Damit ist davon auszugehen, dass die Tabelle Shop vollständig und konsistent in das Zielsystem
übertragen wurde. Die Testfälle T01, T03 und T11 gelten für diese Tabelle als
erfolgreich durchgeführt.

#### Räumliche Plausibilitätsprüfung

Ergänzend zur quantitativen Analyse wird eine visuelle Prüfung der Punktgeometrien vorgenommen.
Hierfür wird die Tabelle *Shop* in derselben GIS-Umgebung geladen, die bereits für die Validierung
der Tabelle *Geografie* verwendet wurde. Die Shops werden gemeinsam mit den Flächengeometrien der
Bundesländer dargestellt, um ihre räumliche Lage fachlich einordnen zu können.

![ER-Diagramm mit gewählter Beziehung](media/Shops_QGIS.png)

Die visuelle Kontrolle zeigt, dass alle Shops innerhalb der erwarteten Bundesländer liegen und
keine offensichtlichen räumlichen Auffälligkeiten wie stark verschobene oder falsch zugeordnete
Punkte auftreten. Damit ist auch die räumliche Plausibilität der Tabelle *Shop* gegeben.

### Validierung der Sachdatenabfragen

#### T07 – Sortierte Sachdatenabfrage (Geburtstagskalender)

Ziel dieses Testfalls ist die Validierung einer fachlich äquivalenten,
sortierten Sachdatenabfrage zwischen der Referenzumgebung
(Microsoft SQL Server, MS SSMS) und der Zielumgebung (SQLite in Kombination
mit Python). Am Beispiel des Geburtstagskalenders wird überprüft, ob das
System in der Lage ist, Datensätze korrekt auszugeben und anhand definierter
Attribute deterministisch zu sortieren.

Der Testfall adressiert die funktionalen Anforderungen **FP3 (Ausführung von
SQL-Anweisungen)** sowie **FP5 (tabellarische Ausgabe von Sachdaten)**.

Verglichen werden die Resultsets beider Systeme mit dem Ziel, sicherzustellen,
dass die Abfrage in beiden Umgebungen identische Datensätze in identischer,
durch die SQL-Abfrage vorgegebener Sortierreihenfolge liefert.

Für den Vergleich gelten folgende Kriterien:

- identische Anzahl der Ergebniszeilen,
- identische Datensätze,
- identische Sortierreihenfolge gemäß der in der Abfrage definierten
  `ORDER BY`-Klausel,
- Übereinstimmung der Attributwerte `Name` und `Gebdat` je Datensatz.

Zur Durchführung des Testfalls wird in der Referenzumgebung Microsoft SQL Server
Management Studio (MS SSMS) die entsprechende Referenzabfrage ausgeführt und das
Resultset ausgegeben. Anschließend wird in der Zielumgebung SQLite das fachlich
äquivalente SQL-Statement über das Python-Skript
`01_geburtstagskalender.py` ausgeführt. Die erzeugten Ergebnislisten werden
einander gegenübergestellt und anhand der definierten Vergleichskriterien
überprüft.

Aufgrund der Größe der Ergebnismenge wird auf eine vollständige visuelle
Darstellung des Resultsets in der Projektdokumentation verzichtet und die
Darstellung auf eine repräsentative Teilausgabe (erste 15 Zeilen) begrenzt.

![ER-Diagramm mit gewählter Beziehung](media/Gebkalender_SSMS.png)

![ER-Diagramm mit gewählter Beziehung](media/Gebkalender_Py.png)

Die Resultsets beider Systeme weisen identische Datensätze sowie eine vollständig
übereinstimmende Sortierreihenfolge auf.

Damit ist nachgewiesen, dass die Zielumgebung SQLite sortierte
Sachdatenabfragen fachlich korrekt und reproduzierbar ausführen kann.

#### T08 – Join Mitarbeiter–Shop

Ziel dieses Testfalls ist die Validierung einer fachlich äquivalenten
Join-Abfrage zwischen der Referenzumgebung (Microsoft SQL Server, MS SSMS)
und der Zielumgebung (SQLite in Kombination mit Python). Untersucht wird,
ob das System in der Lage ist, relationale Verknüpfungen zwischen mehreren
Tabellen korrekt auszuführen und gefilterte Sachdaten reproduzierbar
auszugeben.

Der Testfall adressiert die funktionalen Anforderungen **FP3 (Ausführung von
SQL-Anweisungen)** sowie **FP4 (Einlesen gefilterter Datenlagen)**.

Bei der zugrunde liegenden Abfrage handelt es sich um einen **INNER JOIN**
zwischen den Tabellen `Mitarbeiter` und `Shop` über das gemeinsame
Schlüsselattribut `Shop_ID`. Zusätzlich wird eine Filterbedingung angewendet,
die ausschließlich jene Datensätze berücksichtigt, bei denen der Wohnort eines
Mitarbeiters vom zugehörigen Arbeitsort abweicht. Diese Abfrage entspricht der
Lösung der Aufgabe 8 aus der Übung *MS SQL 1 – Aufbau einer OLTP-Datenbank im
MS SQL Server* und wird als fachliche Referenz herangezogen.

Verglichen werden die Resultsets beider Systeme mit dem Ziel, sicherzustellen,
dass die Join-Operation und die Filterlogik in beiden Umgebungen identische
Ergebnisse liefern.

Für den Vergleich gelten folgende Kriterien:

- identische Anzahl der Ergebniszeilen,
- identische Kombinationen der Attribute `Mitarbeiter`, `Wohnort` und
  `Arbeitsort`,
- Übereinstimmung der ausgegebenen Attributwerte je Datensatz.

Zur Durchführung des Testfalls wird in der Referenzumgebung Microsoft SQL Server
Management Studio (MS SSMS) die entsprechende Join-Abfrage ausgeführt und das
Resultset ausgegeben. Anschließend wird in der Zielumgebung SQLite das fachlich
äquivalente SQL-Statement über das Python-Auswertungsskript
`02_mitarbeiter_wohnort.py` ausgeführt. Dieses dient der Übergabe der
SQL-Anweisung an die Datenbank sowie der tabellarischen Ausgabe der Ergebnisse.

Aufgrund der Größe der Ergebnismenge wird auf eine vollständige visuelle
Darstellung des Resultsets in der Projektdokumentation verzichtet. Stattdessen
wird eine repräsentative Teilausgabe herangezogen. Die vollständige
Ergebnismenge ist durch erneute Ausführung der Abfragen in beiden Systemen
reproduzierbar.

![Join-Ergebnis Mitarbeiter–Shop in MS SSMS](media/join_vali_t08_SSMS.png)

![Join-Ergebnis Mitarbeiter–Shop in SQLite (Python-Ausgabe)](media/join_vali_t08_SQLite.png)

Die Resultsets beider Systeme weisen identische Datensätze sowie übereinstimmende
Zuordnungen zwischen Mitarbeitern und Arbeitsorten auf. Die angewendete
Filterbedingung liefert in beiden Umgebungen konsistente Ergebnisse; Abweichungen
in der Verknüpfung der Datensätze konnten nicht festgestellt werden.

Damit ist nachgewiesen, dass die Zielumgebung SQLite relationale
JOIN-Operationen und Filterbedingungen fachlich korrekt ausführen kann. Der
Testfall bildet zugleich die Grundlage für den nachfolgenden Testfall
**T09 (Aggregation / View)**, in dem aufbauend auf korrekt verknüpften
Datensätzen Aggregatfunktionen überprüft werden.

#### T09 – Aggregation von Sachdaten (Gruppierung)

Ziel dieses Testfalls ist die Validierung einer fachlich äquivalenten
Aggregationsabfrage zwischen der Referenzumgebung (Microsoft SQL Server, MS SSMS)
und der Zielumgebung (SQLite in Kombination mit Python). Untersucht wird, ob das
System in der Lage ist, Aggregatfunktionen und Gruppierungen auf korrekt
verknüpften Datensätzen auszuführen und aggregierte Sachdaten reproduzierbar
bereitzustellen.

Der Testfall adressiert die funktionalen Anforderungen **FD4 (Aggregation und
Views)** sowie **FP3 (Ausführung von SQL-Anweisungen)** und **FP5 (tabellarische
Ausgabe aggregierter Sachdaten)**.

Als fachliche Referenz dient die Lösung der dritten Teilaufgabe von Aufgabe 8
des Moduls *Datenbankentechnologien* (*MS SQL 1 – Aufbau einer OLTP-Datenbank im
MS SQL Server*). In dieser Teilaufgabe wird der wertmäßige Gesamtbestand aller
Waren je Bundesland ermittelt. Die Berechnung erfolgt mittels einer
Aggregationsfunktion (Summe aus Menge und Preis) und wird in der
Referenzumgebung explizit in Form eines Views umgesetzt. Diese Referenz bildet
den Maßstab für die Validierung der Aggregations- und Gruppierungslogik in der
Zielumgebung SQLite.

Verglichen werden die Resultsets beider Systeme mit dem Ziel, sicherzustellen,
dass die Aggregationslogik in beiden Umgebungen identische Gruppierungsergebnisse
und übereinstimmende aggregierte Werte liefert.

Für den Vergleich gelten folgende Kriterien:

- identische Anzahl der Aggregationsergebnisse,
- identische Gruppierungsschlüssel (Bundesländer),
- Übereinstimmung der berechneten Aggregatwerte je Gruppe.

Zur Durchführung des Testfalls wird in der Referenzumgebung Microsoft SQL Server
Management Studio (MS SSMS) der zuvor angelegte View abgefragt, welcher die
aggregierten Bestandswerte je Bundesland bereitstellt. In der Zielumgebung
SQLite wird die fachlich äquivalente Aggregationsabfrage über ein
Python-Auswertungsskript ausgeführt, das die SQL-Anweisung an die Datenbank
übermittelt und die Ergebnisse tabellarisch ausgibt.

Die in beiden Systemen erzeugten Ergebnislisten werden einander
gegenübergestellt und anhand der definierten Vergleichskriterien überprüft. Da
Aggregationsabfragen im Vergleich zu vollständigen Tabellen eine reduzierte
Ergebnismenge liefern, ist eine visuelle Gegenüberstellung der Resultsets
möglich und ausreichend.

Die Reihenfolge der ausgegebenen Gruppierungsergebnisse ist ohne explizite
`ORDER BY`-Klausel nicht deterministisch und stellt daher kein
Vergleichskriterium dar. Der Vergleich erfolgt mengenbasiert anhand der Paare
(Bundesland, aggregierter Bestandswert).

![Aggregierter Gesamtbestand je Bundesland (MS SSMS)](media/agg_view_T09_SSMS.png)

![Aggregierter Gesamtbestand je Bundesland (SQLite / Python-Ausgabe)](media/agg_view_T09_SQLite.png)

Die Resultsets beider Systeme weisen identische Gruppierungsschlüssel sowie
übereinstimmende Werte der berechneten Aggregatfunktionen auf. Abweichungen in
der Anzahl der Gruppen oder in den berechneten Bestandswerten konnten nicht
festgestellt werden.

Damit ist nachgewiesen, dass die Zielumgebung SQLite Aggregatfunktionen,
Gruppierungen und die Bereitstellung aggregierter Sachdaten fachlich korrekt
ausführen kann. Der Testfall baut auf den zuvor validierten
JOIN-Operationen aus **T08** auf und schließt die Prüfung der zentralen
Sachdatenfunktionen ab.

#### T10 – Darstellung von Flächengeometrien

Ziel dieses Testfalls ist die Überprüfung, ob die Zielumgebung (SQLite in
Kombination mit SpatiaLite und Python) in der Lage ist, gespeicherte
Flächengeometrien korrekt auszulesen, zu interpretieren und visuell darzustellen.
Der Testfall dient dem Nachweis einer grundlegenden räumlichen Kernfunktionalität
und bildet die Voraussetzung für nachfolgende räumliche Abfragen und
Berechnungen.

Der Testfall adressiert die funktionalen Anforderungen **FD1 (Speicherung von
Geometrien in einer SpatiaLite-Datenbank)** sowie **FP6 (Visualisierung
räumlicher Daten)**.

Grundlage des Testfalls ist das Python-Skript `07_geometrie_darstellen.py`, das
zur Überprüfung der Fähigkeit eingesetzt wird, Flächengeometrien aus der
Datenbank auszulesen, in ein geeignetes Geometrieformat zu überführen und
visuell darzustellen.

Die im Skript verwendeten SQL-Abfragen liefern neben attributiven Informationen
die Flächengeometrien im Well-Known-Binary-Format (WKB). Die Geometrien werden im
Anschluss im Arbeitsspeicher mithilfe der Bibliothek *Shapely* interpretiert und
in GeoDataFrames überführt.

Zur Visualisierung werden die erzeugten GeoDataFrames in einer Kartenansicht
dargestellt. Ziel ist es zu überprüfen, ob die Geometrien vollständig gelesen,
korrekt interpretiert und ohne Laufzeitfehler visualisiert werden können.

Für den Test gelten folgende Kriterien:

- das Python-Skript wird ohne Fehler ausgeführt,
- die Geometrien können aus dem WKB-Format korrekt rekonstruiert werden,
- die Visualisierung der Flächengeometrien erfolgt ohne Laufzeitfehler

Durch Ausführung der Anwendung wird folgendes Ergebnis erzeugt:

![Aggregierter Gesamtbestand je Bundesland (SQLite / Python-Ausgabe)](media/Plots_Geodaten.png)

Die erfolgreiche Ausführung des Skripts und die korrekte Darstellung der
Flächengeometrien zeigen, dass die Zielumgebung räumliche Geometrien korrekt
verarbeiten und visualisieren kann.

Damit ist nachgewiesen, dass die grundlegende Verarbeitung und Darstellung
räumlicher Daten in der Zielumgebung möglich ist.

#### T11 – Räumliche Selektion: Punkt-in-Polygon

Ziel dieses Testfalls ist die Überprüfung, ob die Zielumgebung (SQLite in
Kombination mit SpatiaLite und Python) in der Lage ist, räumliche Prädikate
korrekt anzuwenden. Konkret wird untersucht, ob Punktgeometrien (Shops) anhand
einer Flächengeometrie (Bundesland) räumlich selektiert werden können
(Punkt-in-Polygon-Abfrage).

Der Testfall adressiert die funktionalen Anforderungen **FD2 (Räumliche
Abfragen)** sowie **FP3 (Ausführung von SQL-Anweisungen)**.

Aufbauend auf dem Testfall **T10**, in dem nachgewiesen wurde, dass
Flächengeometrien korrekt aus der Datenbank gelesen und dargestellt werden
können, wird in diesem Testfall erstmals eine räumliche Funktion angewendet.
Dabei wird geprüft, ob die räumliche Beziehung zwischen Punkt- und
Flächengeometrien fachlich korrekt ausgewertet wird.

Als fachliche Referenz dient eine räumliche Abfrage in der Referenzumgebung
Microsoft SQL Server (MS SSMS), bei der alle Shops ermittelt werden, deren
Punktgeometrie innerhalb der Fläche eines ausgewählten Bundeslands liegt. In
der Zielumgebung wird eine fachlich äquivalente Abfrage mithilfe der
SpatiaLite-Funktionen ausgeführt.

Verglichen werden die Resultsets beider Systeme mit dem Ziel, sicherzustellen,
dass die räumliche Selektion identische Shops liefert.

Für den Vergleich gelten folgende Kriterien:

- identische Anzahl der selektierten Shops,
- identische Menge der ermittelten `Shop_ID`,
- Übereinstimmung der zugehörigen attributiven Informationen je Datensatz.

Zur Durchführung des Testfalls wird in beiden Systemen eine räumliche
Punkt-in-Polygon-Abfrage ausgeführt. In der Zielumgebung erfolgt die Ausführung
über ein Python-Skript, welches die SQL-Anweisung an die Datenbank übermittelt
und die Ergebnisse tabellarisch ausgibt.

Da die Reihenfolge der Ergebniszeilen ohne explizite `ORDER BY`-Klausel nicht
deterministisch ist, stellt sie kein Vergleichskriterium dar. Der Vergleich
erfolgt mengenbasiert anhand der ermittelten `Shop_ID`.

![Aggregierter Gesamtbestand je Bundesland (SQLite / Python-Ausgabe)](media/Shops_Bundeslaender.png)

Die Resultsets beider Systeme liefern identische Mengen an Shops innerhalb des
ausgewählten Bundeslands. Abweichungen in der Anzahl oder in der Zuordnung der
Shops konnten nicht festgestellt werden.

Damit ist nachgewiesen, dass die Zielumgebung SQLite/SpatiaLite räumliche
Punkt-in-Polygon-Abfragen fachlich korrekt ausführen kann.

Der Testfall **T11 – Räumliche Selektion: Punkt-in-Polygon** gilt somit als
erfolgreich durchgeführt.

#### T12 – Räumliche Berechnung: Flächenberechnung von Bundesländern

Ziel dieses Testfalls ist die Überprüfung, ob die Zielumgebung (SQLite in
Kombination mit SpatiaLite und Python) in der Lage ist, räumliche Berechnungen
auf Flächengeometrien korrekt durchzuführen. Konkret wird untersucht, ob die
Flächen der Bundesländer auf Basis ihrer Polygongeometrien berechnet werden
können und fachlich plausible sowie mit der Referenzumgebung vergleichbare
Ergebnisse liefern.

Der Testfall adressiert die funktionalen Anforderungen **FD3 (Räumliche
Berechnungen)** sowie **FP3 (Ausführung von SQL-Anweisungen)**.

Aufbauend auf den vorangegangenen Testfällen **T10**, in denen die korrekte
Verarbeitung und Darstellung von Flächengeometrien nachgewiesen wurde, sowie
**T11**, in denen räumliche Beziehungen zwischen Punkt- und Flächengeometrien
überprüft wurden, wird in diesem Testfall erstmals eine metrische räumliche
Berechnung durchgeführt.

Als fachliche Referenz dient die Flächenberechnung in der Referenzumgebung
Microsoft SQL Server (MS SSMS), bei der die Flächen der Bundesländer auf Basis
der gespeicherten Geometrien berechnet werden. In der Zielumgebung erfolgt die
fachlich äquivalente Berechnung mithilfe von SpatiaLite-Funktionen, wobei die
Ergebnisse über ein Python-Skript tabellarisch ausgegeben werden.

Verglichen werden die Resultsets beider Systeme mit dem Ziel, sicherzustellen,
dass die berechneten Flächenwerte fachlich übereinstimmen.

Für den Vergleich gelten folgende Kriterien:

- identische Anzahl der berechneten Flächenwerte,
- eindeutige Zuordnung der berechneten Flächen zu identischen Bundesländern,
- Übereinstimmung der berechneten Flächenwerte innerhalb einer definierten
  relativen Toleranz.

Die Notwendigkeit des Festlegens einer relativen Toleranz ergibt sich aus geringfügigen numerischen Abweichungen bei Flächenberechnungen in unterschiedlichen räumlichen Datenbanksystemen. Ein Flächenwert gilt als übereinstimmend, wenn die relative Abweichung den
Toleranzwert von **0,5 %** nicht überschreitet.

![Aggregierter Gesamtbestand je Bundesland (SQLite / Python-Ausgabe)](media/flaeche_SSMS.png)

![Aggregierter Gesamtbestand je Bundesland (SQLite / Python-Ausgabe)](media/flaeche_SQLite.png)

Die Gegenüberstellung der berechneten Flächenwerte zeigt, dass sämtliche
Bundesländer innerhalb der definierten Toleranz liegen. Die maximal beobachtete
relative Abweichung liegt deutlich unterhalb von 0,5 % und tritt insbesondere
bei kleineren Flächen auf. Abweichungen, die über die erwarteten numerischen
Unterschiede hinausgehen, konnten nicht festgestellt werden.

Damit ist nachgewiesen, dass die Zielumgebung SQLite/SpatiaLite in der Lage ist,
räumliche Flächenberechnungen fachlich korrekt und mit ausreichender numerischer
Genauigkeit durchzuführen.

Der Testfall **T12 – Räumliche Berechnung: Flächenberechnung von
Bundesländern** gilt somit als erfolgreich durchgeführt.

#### T13 – Räumliche Berechnung: Referenzpunkt und Distanzberechnung

Ziel dieses Testfalls ist die Überprüfung, ob die Zielumgebung (SQLite in
Kombination mit SpatiaLite und Python) in der Lage ist, eine vollständige
räumliche Verarbeitungskette umzusetzen. Im Mittelpunkt steht dabei nicht
ausschließlich die Distanzberechnung, sondern die korrekte Erzeugung eines
Referenzpunkts, dessen Einbindung in das bestehende räumliche Datenmodell sowie
die darauf aufbauende Berechnung von Distanzen.

Der Testfall adressiert die funktionalen Anforderungen **FD3 (Räumliche
Berechnungen)** sowie **FP3 (Ausführung von SQL-Anweisungen)**.

Aufbauend auf den vorherigen Testfällen **T10** (Darstellung von
Flächengeometrien), **T11** (räumliche Selektion) und **T12**
(Flächenberechnung) wird in diesem Testfall geprüft, ob die Zielumgebung auch
punktbasierte räumliche Operationen korrekt durchführen kann.

Als fachliche Referenz dient die Lösung einer Übungsaufgabe aus dem Modul
*Datenbankentechnologien* (*MS SQL 2 – Verwaltung geografischer Informationen*),
in der ein fester Referenzpunkt (HTW Dresden) als Geometrie erzeugt und die
Entfernung aller Shops zu diesem Punkt berechnet wird. Die Ergebnisse dieser
Berechnung in Microsoft SQL Server (MS SSMS) bilden den Maßstab für die
Validierung der Zielumgebung.

In der Zielumgebung wird der Referenzpunkt aus seinen geografischen Koordinaten
(Längen- und Breitengrad) mithilfe der Funktion `MakePoint()` als
Punktgeometrie im Koordinatenreferenzsystem EPSG:4326 erzeugt. Um eine
Distanzberechnung in Metern zu ermöglichen, werden sowohl die Shop-Koordinaten
als auch der Referenzpunkt vor der Berechnung in das metrische
Koordinatenreferenzsystem ETRS89 / UTM Zone 32N (EPSG:25832) transformiert. Die
Distanzberechnung erfolgt anschließend mit `ST_Distance()` auf den projizierten
Punktgeometrien.

Verglichen werden die Resultsets der Referenz- und Zielumgebung mit dem Ziel,
sicherzustellen, dass die berechneten Distanzen fachlich übereinstimmen.

Für den Vergleich gelten folgende Kriterien:

- identische Anzahl der berechneten Distanzwerte,
- eindeutige Zuordnung der Distanzwerte zu identischen Shops,
- Übereinstimmung der berechneten Distanzen innerhalb einer definierten
  relativen Toleranz.

Da die Referenzumgebung eine geodätische Distanzberechnung auf dem Ellipsoid
verwendet, während die Zielumgebung eine Distanzberechnung auf projizierten
Koordinaten durchführt, ist mit geringfügigen numerischen Abweichungen zu
rechnen. Der Vergleich erfolgt daher nicht auf exakte Gleichheit. Stattdessen
wird eine relative Toleranz von **0,5 %** festgelegt. Ein Distanzwert gilt als übereinstimmend, wenn die relative Abweichung den
Toleranzwert von 0,5 % nicht überschreitet.

![Aggregierter Gesamtbestand je Bundesland (SQLite / Python-Ausgabe)](media/htw_distanz_SSMS.png)

![Aggregierter Gesamtbestand je Bundesland (SQLite / Python-Ausgabe)](media/htw_distanz_SQLite.png)

Die Gegenüberstellung der berechneten Distanzen zeigt, dass sämtliche
Shop-Distanzen innerhalb der definierten Toleranz liegen. Die maximal
beobachtete relative Abweichung liegt deutlich unterhalb des festgelegten
Grenzwerts und ist insbesondere bei größeren Entfernungen geringfügig höher,
was den erwarteten numerischen Unterschieden zwischen geodätischer und
projizierter Berechnung entspricht. Fachlich relevante Abweichungen konnten
nicht festgestellt werden.

Damit ist nachgewiesen, dass die Zielumgebung SQLite/SpatiaLite in der Lage ist,
einen externen Referenzpunkt korrekt als Geometrie zu erzeugen, räumlich in das
bestehende Datenmodell einzubinden und darauf aufbauend Distanzberechnungen
fachlich korrekt und mit ausreichender numerischer Genauigkeit
durchzuführen.

Der Testfall **T13 – Räumliche Berechnung: Referenzpunkt und
Distanzberechnung** gilt somit als erfolgreich durchgeführt.

# Ergebnisauswertung

Die durchgeführten Testfälle zeigen, dass die Zielumgebung (SQLite in Kombination mit SpatiaLite und Python) die zuvor definierten funktionalen Anforderungen erfüllt. Die Tests bilden jedoch ausschließlich einen Funktionsnachweis.

Im Verlauf der Implementierung sind weitere Erkenntnisse entstanden, die nicht unmittelbar aus den Testfällen hervorgehen, jedoch für die Einordnung der Zielumgebung gegnüber der MS-SQL-Server-Umgebung relevant sind. Diese betreffen Unterschiede in der Typisierung der Datenbanksysteme, den Umgang mit Geodaten, Abweichungen im SQL-Dialekt sowie den zusätzlichen Installations- und Integrationsaufwand von SQLite.

## Dialektspezifische Unterschiede in SQL

Neben den Datentypen unterscheiden sich auch die SQL-Dialekte beider Systeme. Transact-SQL (MS SQL Server) bietet eine Vielzahl komfortabler Funktionen, die in SQLite nicht oder nur in angepasster Form existieren. Dies betrifft insbesondere Datumsfunktionen, Typkonvertierungen, bestimmte Stringoperationen sowie einzelne Aggregations- und Formatierungsfunktionen. In der Praxis bedeutete dies, dass jedes nicht-triviale SQL-Statement angepasst werden musste. Die Abfragen konnten fachlich äquivalent umgesetzt werden, jedoch nie unverändert übernommen werden. SQLite erweist sich dennoch in den untersuchten Bereichen als funktional gleichwertig.

## Unterschiede in der Typisierung

Ein grundlegender Unterschied zwischen Microsoft SQL Server und SQLite liegt im Typisierungskonzept. Der SQL Server arbeitet streng typisiert. Die Datenbank erzwingt die Einhaltung des Typs bei jedem ``INSERT`` oder ``UPDATE``. Datentypen wie ``date``, ``money`` oder ``geography`` besitzen daher klar definierte Eigenschaften und sind an die Typdefinition der jeweiligen Spalte gebunden. Bei einer Typinkompatibilität (bspw. dem Einfügen von Text in einer numerischen Spalte) wird eine Fehlermeldung ausgelöst und der Prozess abgebrochen. Dafür stehen umfangreiche datentypspezifische Funktionalitäten bereit, wie beispielsweise ``MONTH()`` und ``DAY()`` für die Verarbeitung des Datumformats.

SQLite hingegen arbeitet mit einer dynamsichen Typisierung und kennt im Kern nur fünf Speichertypen (``NULL``, `INTEGER`, ``REAL``, ``TEXT``, ``BLOB``). Deklarierte Typen wie ``VARCHAR`` oder ``DATETIME`` werden diesen Klassen via *Type Affinity* zugeordnet. Im Rahmen der Migration führte dies zwangsläufig zu Vereinfachungen. Datumswerte wurden als ``TEXT`` gespeichert, Geldbeträge als ``REAL`` und Geodaten als ``BLOB``. Funktional ist diese Abbildung ausreichend, sie erfordert jedoch zusätzliche Anpassungen auf Abfrageebene. Ein Beispiel hierfür ist der Geburtstagskalender (``01_geburtstagskalender.py``). In SQL Server stehen typspezifische Funktionen wie ``MONTH()`` und ``DAY()`` unmittelbar zur Verfügung. In SQLite mussten Monat und Tag mittels ``substr()`` aus einem Textfeld extrahiert werden. Die fachliche Logik bleibt identisch, die technische Umsetzung wird jedoch umfangreicher. Die Unterschiede in der Typisierung stellen somit kein funktionales Problem dar, erhöhen jedoch die Komplexität der SQL-Statements.

## Unterschiede in der Geodatenverarbeitung

Bei der Betrachtung der Geodatenverarbeitung treten die festgestellten Unterschiede in ihrer Gesamtheit auf. Die Geodatentypen beider Systeme unterschieden sich stark. Der SQL Server stellt mit den Datentypen ``geometry`` und ``geography`` native räumliche Datentypen bereit, die integraler Bestandteil des Datenbanksystems sind. Sie sind semantische Objekte, statt nur ein reines Speicherformat und enthlten u.a. Koordinateninforamtionen (SIRD), Validierungslogik, Verarbeitungsmethoden und Berechnungslogik. Letztere sind sofort abrufbar und benötigen kein weiteres Setup für ihre Nutzung. Wird beispielsweise die Funktion ``STDistance()`` auf Objekte des Typs `geography` angewendet (siehe `04_abstand_shops_zur_htw.py`), wird bei der Verwendung geographischer Koordinanten (Länge, Breite)  das Ergebnis automatisch in Meter umgerechnet und zurückgegeben. Eine vorherige Projektion der Koordinaten ist daher nicht erforderlich.

In SQLite werden Geometrien intern als ``BLOB`` gespeichert. Für die Nutzung in Python mussten diese zunächst mittels ``ST_AsBinary()`` in das OGC-konforme WKB überführt und anschließend mit Shapely interpretiert werden. Die Verarbeitung räumlicher Daten verteilt sich damit auf mehrere Ebenen: Die Speicherung und grundlegende Analyse erfolgt in der Datenbank über SpatiaLite, die Interpretation der Geometrien über Shapely, die Verarbeitung über GeoPandas und die Visualisierung über Matplotlib. Anders als ``geometry`` und ``geography`` ist `BLOB` ein reines Speicherformat. Die gleiche Berechnung mittels `ST_Distance()` benötigt Vorverarbeitungsschritte. Bei der Verwendung geographischer Koordinaten, berechnet die Funktion die Distanz in den Einheiten des zugrundeliegenden Referenzsystems, geographischer Länge und Breite. Aus diesem Grund ist eine vorherige Transformation mittels `Transform()` in ein metrisches, kartesisches Koordinatenreferenzsystem (z. B. ETRS89 / UTM Zone 32N, EPSG:25832) erforderlich. Erst nach dieser Projektion kann eine Distanzberechnung durchgeführt werden, deren Ergebnis in Metern vorliegt..

Die fachliche Korrektheit ist in beiden Systemen gewährleistet, jedoch unterscheidet sich der Grad der Automatisierung und Integration deutlich. SQL Server stellt mit den Datentypen ``geography`` und `geometry` eine stärker integrierte Lösung bereit, während SQLite/SpatiaLite eine explizite Behandlung des Koordinatenreferenzsystems erfordert. 

## Systemintegration

Die zuvor dargestellten Unterschiede lassen sich im Kern auf den Grad der Systemintegration zurückführen. Microsoft SQL Server ist als vollintegriertes relationales Datenbankmanagementsystem konzipiert. Datenhaltung, Typisierung, Geodatenverarbeitung, Benutzer- und Rechteverwaltung sowie Optimierungsmechanismen sind fester Bestandteil eines geschlossenen Gesamtsystems. Der Betrieb erfolgt serverbasiert, mit explizitem Nutzerhandling, Transaktionsmanagement und einer klaren Trennung zwischen Datenbankinstanz und Clientanwendung. Die räumlichen Datentypen sind integraler Bestandteil des Systems und erfordern keine zusätzliche Installation oder Konfiguration.

SQLite hingegen verfolgt einen anderen architektonischen Ansatz. Es handelt sich um eine dateibasierte Datenbank ohne eigene Serverinstanz. Die Datenbank ist eine einzelne Datei, die direkt von Anwendungen angesprochen wird. Erweiterte Funktionalitäten – insbesondere im Bereich der Geodaten – werden nicht systemintern bereitgestellt, sondern über externe Module wie SpatiaLite ergänzt. Auch die Weiterverarbeitung und Visualisierung der Daten erfolgt außerhalb der Datenbank, in diesem Projekt über Python-Bibliotheken wie Shapely, GeoPandas und Matplotlib. Die Gesamtfunktionalität entsteht somit durch das Zusammenspiel mehrerer Komponenten.

Diese Architektur bietet Vorteile hinsichtlich Portabilität, Offenheit und Flexibilität, erfordert jedoch einen höheren Integrations- und Konfigurationsaufwand. Während der SQL Server eine stark integrierte, zentral verwaltete Umgebung bereitstellt, stellt die Kombination aus SQLite, SpatiaLite und Python eine modulare Lösung dar, bei der Verantwortung für Koordinatenreferenzsysteme, Erweiterungen und Systemkompatibilität stärker beim Anwender liegt.

# Fazit

Ziel des Projektstudiums war die Untersuchung der Einsatzmöglichkeiten von Python-Open-Source-Bibliotheken zur Visualisierung raumbezogener Sachdaten aus Datenbanken. Im Projektverlauf konkretisierte sich diese Fragestellung dahingehend, ob eine auf SQLite, SpatiaLite und Python basierende Open-Source-Lösung in der Lage ist, die im Rahmen der SQL-Übungen erarbeiteten fachlichen und räumlichen Aufgaben funktional gleichwertig zu reproduzieren.

Die Ergebnisse zeigen, dass die gewählte Zielumgebung die definierten Anforderungen vollständig erfüllen kann. Relationale Abfragen, Join-Operationen, Aggregationen, Views sowie räumliche Operationen wie Punkt-in-Polygon-Selektionen, Flächenberechnungen und Distanzermittlungen konnten fachlich korrekt umgesetzt werden. Die durchgeführten Testfälle belegen die funktionale Gleichwertigkeit der Ergebnisse im Vergleich zur Referenzumgebung Microsoft SQL Server.

Gleichzeitig wurde deutlich, dass die Umsetzung in der Open-Source-Umgebung mit einem erhöhten technischen Aufwand verbunden ist. Unterschiede in der Typisierung, Anpassungen im SQL-Dialekt sowie die explizite Behandlung von Geodaten und Koordinatenreferenzsystemen erfordern zusätzliche Implementierungsschritte. Während Microsoft SQL Server viele dieser Aspekte systemintern integriert bereitstellt, müssen sie in der SQLite/SpatiaLite-Umgebung bewusster und expliziter umgesetzt werden. Insbesondere der modulare Aufbau der Zielumgebung – bestehend aus SQLite, SpatiaLite und verschiedenen Python-Bibliotheken – führt zu einer stärkeren Eigenverantwortung hinsichtlich Konfiguration, Referenzsystembehandlung und Datenverarbeitung.

Die ursprünglich vorgesehene Anbindung über einen Object-Relational Mapper (SQLAlchemy) wurde im Projektverlauf zugunsten einer direkten Nutzung der sqlite3-Schnittstelle verworfen, da diese für den untersuchten Anwendungsfall ausreichend und technisch transparenter erschien. Ebenso wurde anstelle einer eigenständigen Datenbankimplementierung die Migration der bestehenden Übungsdatenbank gewählt, um eine direkte Vergleichbarkeit der Ergebnisse sicherzustellen. Der im Themenblatt angesprochene Aspekt der Performanzanalyse wurde nicht vertieft, da der Schwerpunkt der Arbeit auf der funktionalen Reproduzierbarkeit und der qualitativen Bewertung der Open-Source-Lösung lag.

In der Gesamteinordnung zeigt sich, dass SQLite in Kombination mit SpatiaLite und Python eine fachlich geeignete Alternativlösung zur Bearbeitung der untersuchten Aufgaben darstellt. Die Lösung ist vollständig Open-Source-basiert, portabel und flexibel einsetzbar. Sie stellt jedoch keinen unmittelbar gleichwertigen Ersatz für ein integriertes, serverbasiertes RDBMS dar, da sie höhere Anforderungen an Konfiguration, Systemverständnis und explizite Implementierung stellt.

Die Arbeit kommt somit zu dem Ergebnis, dass die untersuchten Python-Open-Source-Bibliotheken in Verbindung mit einer SQLite/SpatiaLite-Datenbank grundsätzlich geeignet sind, raumbezogene Sachdaten zu analysieren und zu visualisieren. Die Eignung ist fachlich gegeben, der Implementierungsaufwand und der Integrationsgrad unterscheiden sich jedoch deutlich von einer proprietären, vollständig integrierten Datenbanklösung wie Microsoft SQL Server.

# Notizen Termin vom 22.01.2026

- Verzeichnisstruktur überarbeiten
    - Struktur der Programme überarbeiten
    - Ordner für Doku (docs) mit allen dazugehörigen Dateien
- Doku überarbeiten
    - Kapitel als einzelne Dokumente
    - unteinander verlinken 
    - README als Einstieg mit: (ganz oben in Verzeichnisstruktur)
        - Inhaltsverzeichnis
        - kurzer Projektbeschreibung
        - Links zu Kapiteln und Codes
    - Ergebniskapitel
     - Software testen
        - Testfälle defninieren
        - MS SQL als Referenzdaten
        - Test durchführen u. dokumentieren
    - Fazit formulieren
- Abagbe per Git -> hochladen, damit Prof. Toll sich das einfach ziehen kann 
- keine formelle Präsentation -> Vorstellung der Projektarbeit im Kollegenkreis

## notizen 22.21.2026 16:38
 
- python-programme laufen nicht mehr -> module können nicht importiert werden -> fixen- rest steht oben -> GELÖST

## notizen 05.02.2026

 - FK enforcing als Test aufnehmen
 - bei Validierung der Geodaten, die Überprüfung der SRID mit aufnehmen und T11 streichen
 - T13 von chatti übernehmen und nochmal korrekturlesen

## notizen 06.02.2026

- das Kapitel Ergebnisauwertung ist nur ein KI-Prompt und viel zu allgemein
- es fehlen infos zu erkenntnissen, die über testergebnisse hinausgehen
    - unterschied der datentypen zwischen SSMS und SQLite, insbesondere Geodaten betreffend
    - allgemeine Dialektunterscheide zwischen beiden Systemen
    - notwendigkeit der installation von Spatialite, um Geodaten mit SQLite nutzen zu können und die damit verbundenen Hürden bei der installation und risiken von beim laden der erweiterung (DLL-Hell)
- tests waren nur funktionsnachweise
- weitere wichtige erkenntnisse der arbeit herausfinden 
- korrekturlesung
- aufteilung in verschiedene dokuemnte und verlinkungen
- text lesen, überabrieten, glätten, auf roten faden achten 
