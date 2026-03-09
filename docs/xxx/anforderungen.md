## Übersicht funktionale Anforderungen Datenbank

| Nummer | Anforderung              | Beschreibung |
|--------|--------------------------|--------------|
| FD1    | Räumliche Datenhaltung   | Geodaten (Punkte, Flächen) müssen gespeichert, ausgelesen und fachlich ausgewertet werden können. |
| FD2    | Räumliche Abfragen       | Abfragen nach räumlichen Beziehungen (z. B. Punkt-in-Polygon) müssen ausführbar sein. |
| FD3    | Berechnungen             | Abstände und Flächeninhalte müssen berechnet werden können. |
| FD4    | Aggregation und Views    | Aggregationen sowie darauf basierende Views müssen erstellt und ausgegeben werden können. |
| FD5    | Abfrageoptimierung       | Indizes sollen zur Abfrageoptimierung angelegt und von der Datenbankengine genutzt werden. |

## Übersicht nicht-funktionale Anforderungen Datenbank

| Nummer | Anforderung                 | Beschreibung |
|--------|-----------------------------|--------------|
| ND1    | Tabellenstruktur            | Die Tabellen `Shop`, `Geografie`, `Mitarbeiter`, `Artikel`, `Bestand` müssen vorhanden sein. |
| ND2    | Relationen                  | Primär- und Fremdschlüssel sollen der ursprünglichen Datenbank entsprechen. |
| ND3    | Inhaltliche Übereinstimmung | Die Tabellendaten der SQLite-Datenbank sollen inhaltlich der MS-SQL-Datenbank entsprechen. |

## Übersicht funktionale Anforderungen Python

| Nummer | Anforderung                    | Beschreibung |
|--------|--------------------------------|--------------|
| FP1    | Datenbankverbindung aufbauen   | Öffnen einer SQLite-Datenbankinstanz aus Python muss möglich sein. |
| FP2    | SpatiaLite-Erweiterung laden   | Die SQLite-Erweiterung SpatiaLite muss aus Python geladen werden können. |
| FP3    | SQL-Anweisungen                | SQL-Anweisungen zur Datenanalyse müssen ausgeführt werden können, einschließlich JOINs, Filterbedingungen, Sortierungen (`ORDER BY`) und Aggregationen. |
| FP4    | Einlesen gefilterter Datenlage | Gefilterte Datenlagen müssen über SQL-Abfragen aus der Datenbank eingelesen werden können. |
| FP5    | Darstellung von Sachdaten      | Gefilterte Sachdaten müssen tabellarisch ausgegeben werden können, einschließlich reproduzierbarer Sortierreihenfolgen bei definierter Abfrage. |
| FP6    | Visualisierung von Geodaten    | Geodaten müssen aus der Datenbank gelesen, in geeignete Geometrieobjekte überführt und in Kartenform visualisiert werden können. |

## Übersicht nicht-funktionale Anforderungen Python

| Nummer | Anforderung   | Beschreibung |
|--------|---------------|--------------|
| NP1    | Open-Source   | Alle verwendeten Softwarekomponenten sollen Open-Source-basiert sein. |
| NP2    | Wartbarkeit   | Der Programmcode soll modular aufgebaut, nachvollziehbar strukturiert und kommentiert sein. |
