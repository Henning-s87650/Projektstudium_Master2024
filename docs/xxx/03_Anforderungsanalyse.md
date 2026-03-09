# Methodik

Das Vorgehen gliedert sich in:

1. **Anforderungsanalyse**  
   Erhebung funktionaler und nicht-funktionaler Anforderungen an Datenbank und Python-Programme.

2. **Systementwurf**  
   Konzeption der grundlegenden Systemarchitektur und Festlegung der technischen Rahmenbedingungen des Zielsystems (SQLite/SpatiaLite + Python).

3. **Implementierung**  
   Umsetzung der definierten Funktionalitäten in SQLite/SpatiaLite sowie  Python-Skripten.

4. **Test und Validierung**  
   Überprüfung der implementierten Lösung anhand der zuvor erhobenen Anforderungen und Vergleich der Ergebnisse mit den MS-SQL-Server-Praktikumsaufgaben des Moduls „Datenbanktechnologien“. 
---

## Anforderungsanalyse

Die Anforderungen sind in **funktionale** und **nicht-funktionale** Anforderungen unterteilt. Zusätzlich wird zwischen Anforderungen an die **Datenbank** und an die **Python-Programme** unterschieden.

### Funktionale Anforderungen an die Datenbank

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

#### Übersicht funktionale Anforderungen Datenbank

| Nummer | Anforderung              | Beschreibung                                                              |
|--------|--------------------------|---------------------------------------------------------------------------|
| FD1    | Räumliche Datenhaltung   | Geodaten (Punkte, Flächen) müssen gespeichert und ausgewertet werden.    |
| FD2    | Räumliche Abfragen       | Abfragen nach räumlichen Beziehungen müssen ausführbar sein.             |
| FD3    | Berechnungen             | Abstände und Flächeninhalte müssen berechnet werden können.              |
| FD4    | Aggregation und Views    | Aggregationen und Views müssen erstellt und ausgegeben werden können.    |
| FD5    | Abfrageoptimierung       | Indizes sollen zur Abfrageoptimierung angelegt und genutzt werden.       |

---

### Nicht-funktionale Anforderungen an die Datenbank

Die nicht-funktionalen Anforderungen betreffen die strukturelle und inhaltliche Übereinstimmung der migrierten SQLite-/SpatiaLite-Datenbank mit der ursprünglichen MS-SQL-Server-Datenbank.

**Tabellenstruktur (ND1)**  
In „MS SQL 1“ wird ein relationales Schema mit den Tabellen `Shop`, `Geografie`, `Mitarbeiter`, `Artikel` und `Bestand` definiert. Die neue Datenbank soll diese Tabellenstruktur vollständig abbilden, um alle Praktikumsaufgaben und Abfragen auf gleicher Basis durchführen zu können.

**Relationen (ND2)**  
Primär- und Fremdschlüsselbeziehungen sind für die Aufgaben essenziell (z. B. Verknüpfung von Shops mit Geometrien oder von Artikeln mit Beständen). Die migrierte Datenbank soll diese Beziehungen korrekt übernehmen.

**Inhaltliche Übereinstimmung (ND3)**  
Die Inhalte der Tabellen in SQLite sollen den Daten der MS-SQL-Datenbank entsprechen, damit sich Abfragen, Distanzberechnungen und Aggregationen sinnvoll vergleichen lassen.

#### Übersicht nicht-funktionale Anforderungen Datenbank

| Nummer | Anforderung               | Beschreibung                                                                 |
|--------|---------------------------|------------------------------------------------------------------------------|
| ND1    | Tabellenstruktur          | Die Tabellen `Shop`, `Geografie`, `Mitarbeiter`, `Artikel`, `Bestand` müssen vorhanden sein. |
| ND2    | Relationen                | Primär- und Fremdschlüssel sollen der ursprünglichen Datenbank entsprechen. |
| ND3    | Inhaltliche Übereinstimmung | Die Tabellendaten der SQLite-Datenbank sollen der MS-SQL-Datenbank gleichen. |

---

### Funktionale Anforderungen an die Python-Programme

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

#### Übersicht funktionale Anforderungen Python

| Nummer | Anforderung                       | Beschreibung                                                                 |
|--------|-----------------------------------|------------------------------------------------------------------------------|
| FP1    | Datenbankverbindung aufbauen      | Öffnen einer Datenbankinstanz aus Python.                                   |
| FP2    | SpatiaLite-Erweiterung laden      | Laden der SQLite-Erweiterung SpatiaLite.                                    |
| FP3    | SQL-Anweisungen                   | Ausführen von SQL-Anweisungen zur Datenanalyse.                             |
| FP4    | Einlesen gefilterter Datenlage    | Einlesen gefilterter Datenlagen über SQL.                                   |
| FP5    | Darstellung von Sachdaten         | Tabellarische Darstellung der gefilterten Sachdaten.                        |
| FP6    | Visualisierung von Geodaten       | Darstellung der Geodatenlage in Kartenform.                                 |

---

### Nicht-funktionale Anforderungen an die Python-Programme (NP)

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

---

## Systementwurf

Auf Basis der Anforderungsanalyse ergibt sich ein Systementwurf mit drei Kernaufgaben:

1. **Datenhaltung**  
   - SQLite-Datenbank mit SpatiaLite-Erweiterung  
   - Speicherung von Sach- und Geodaten  
   - möglichst exakte Abbildung der ursprünglichen MS-SQL-Server-Datenbank, um eine inhaltliche und funktionale Vergleichbarkeit sicherzustellen.

2. **Schnittstelle zur Datenhaltung**  
   - Python-basierte Verbindungslogik  
   - Öffnen der Datenbankinstanz  
   - Laden der SpatiaLite-Erweiterung  
   - Rückgabe eines Verbindungsobjekts, das in allen Auswertungsskripten wiederverwendet wird.

3. **Datenverarbeitung und Visualisierung**  
   - spezialisierte Python-Skripte für Analyse- und Visualisierungsaufgaben  
   - Auswahl passender SQL-Anweisungen aus einem zentralen Modul  
   - Einlesen der gefilterten Datenlage in tabellarische Datenstrukturen
   - Ausgabe von Sachdaten im Terminal und zusätzliche Visualisierung von Geodaten.

Das folgende Diagramm veranschaulicht den Systementwurf und zeigt die Interaktionen zwischen den verschiedenen Komponenten.

![UML-Diagramm des Systementwurfs](Schema_Systemkonzept.jpg)