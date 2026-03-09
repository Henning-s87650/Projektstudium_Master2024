[zurück zur Startseite](../README.md)

# 2.2 Anforderungsanalyse

Ziel der Anforderungsanalyse ist die Definition des Leistungsumfangs, den die Zielumgebung aus SQLite, SpatiaLite und Python erfüllen muss, um als fachlich gleichwertig zur Referenzdatenbank in Microsoft SQL Server zu gelten. Die Anforderungen werden aus den im Modul *Datenbanktechnologien* bearbeiteten Übungsaufgaben abgeleitet. Diese Aufgaben definieren die funktionalen Eigenschaften der ursprünglichen MS-SQL-Server-Datenbank und bilden damit den Maßstab für die Reproduktion im Open-Source-System.

Zur systematischen Strukturierung werden die Anforderungen in:

- **funktionale Anforderungen** und  
- **nicht-funktionale Anforderungen**

unterteilt.

Zusätzlich erfolgt eine Differenzierung zwischen Anforderungen an:

- die **Datenbankebene** (SQLite/SpatiaLite) und  
- die **Anwendungsebene** (Python-Programme).

Die hier definierten Anforderungen dienen nicht ausschließlich der konzeptionellen Beschreibung des Systems, sondern stellen zugleich die Bewertungsgrundlage für die in [Kapitel 7](72_Testfälle.md) dargestellten Testfälle dar.

## Anforderungen an die Datenbank

Die Anforderungen an die Datenbank definieren die strukturelle und funktionale Reproduzierbarkeit der Referenzumgebung auf Schema- und SQL-Ebene. Sie legen fest, welche Eigenschaften die SQLite-/SpatiaLite-Datenbank aufweisen muss, um die fachlichen Aufgaben der MS-SQL-Server-Datenbank gleichwertig abbilden zu können.

### Funktionale Anforderungen an die Datenbank

Die funktionalen Anforderungen beschreiben die operativen Fähigkeiten der Datenbank.

#### FD1 – Räumliche Datenhaltung

Die Zielumgebung muss in der Lage sein, Punkt- und Flächengeometrien dauerhaft zu speichern. Die Speicherung muss in einem räumlichen Format erfolgen, das die Durchführung arithmetischer und topologischer Operationen ermöglicht.

#### FD2 – Räumliche Abfragen

Die Datenbank muss räumliche Prädikate interpretieren und ausführen können. Dazu zählen insbesondere:

- Punkt-in-Polygon-Abfragen,
- Nachbarschaftsbeziehungen,
- räumliche Filteroperationen.

Die Ergebnisse müssen fachlich identisch oder qualitativ vergleichbar zur Referenzumgebung sein.

#### FD3 – Geometrische Berechnungen

Die Zielumgebung muss metrische Berechnungen auf Geometrien unterstützen. Dazu gehören:

- Flächenberechnungen von Polygonen,
- Distanzberechnungen zwischen Punktgeometrien.

Aufgrund möglicher Unterschiede in Rechenmodellen (z. B. geodätisch vs. projiziert) ist eine toleranzbasierte Bewertung zulässig.

#### FD4 – Aggregation und Views

Die Datenbank muss Aggregatfunktionen und Gruppierungen unterstützen. Dazu zählen:

- Summenbildungen,
- Gruppierungen nach Attributen,
- Erstellung von Views oder funktional äquivalenten Abfragen.

Die Ergebnisse müssen reproduzierbar und fachlich korrekt sein.

### Übersicht funktionale Anforderungen an die Datenbank

| Nummer | Anforderung | Beschreibung |
|--------|------------|--------------|
| FD1 | Räumliche Datenhaltung | Speicherung und Verwaltung von Punkt- und Flächengeometrien |
| FD2 | Räumliche Abfragen | Durchführung topologischer und räumlicher Filteroperationen |
| FD3 | Geometrische Berechnungen | Berechnung von Flächen und Distanzen |
| FD4 | Aggregation und Views | Unterstützung von Aggregatfunktionen und Gruppierungen |


### Nicht-funktionale Anforderungen an die Datenbank

Die nicht-funktionalen Anforderungen betreffen die strukturelle und inhaltliche Integrität der migrierten Datenbank. Sie definieren die Voraussetzungen für eine Vergleichbarkeit der Daten zwischen Referenz- und Zielsystem.

#### ND1 – Tabellenstruktur

Die Tabellenstruktur der Referenzdatenbank muss vollständig reproduziert werden. Alle relevanten Tabellen müssen im Zielsystem vorhanden sein.

#### ND2 – Relationen und Schlüssel

Primär- und Fremdschlüsselbeziehungen müssen korrekt implementiert werden. Die referenzielle Integrität muss gewährleistet sein.

#### ND3 – Inhaltliche Übereinstimmung

Die Tabellendaten der SQLite-Datenbank müssen inhaltlich mit der Referenzdatenbank übereinstimmen. Abweichungen auf Zeilen- oder Attributebene würden die Vergleichbarkeit der Systeme beeinträchtigen.

### Übersicht nicht-funktionale Anforderungen an die Datenbank

| Nummer | Anforderung | Beschreibung |
|--------|------------|--------------|
| ND1 | Tabellenstruktur | Vollständige Reproduktion des Schemas |
| ND2 | Relationen | Korrekte Abbildung von PK- und FK-Beziehungen |
| ND3 | Inhaltliche Übereinstimmung | Identische Datenbestände im Zielsystem |

## Anforderungen an die Python-Programme

Die Python-Anwendungen bilden die Schnittstelle zwischen Datenbank und Nutzer. Ziel ist es, die in der Referenzumgebung ausgeführten SQL-Abfragen über Python reproduzierbar auszuführen und die Ergebnisse fachlich korrekt darzustellen.

Die Verarbeitung der Daten erfolgt primär über SQL. Python übernimmt dabei:

- die Verbindungslogik,
- die Übergabe der SQL-Anweisungen,
- die Weiterverarbeitung der Resultsets,
- die tabellarische Ausgabe sowie
- die Visualisierung räumlicher Daten.

###   Funktionale Anforderungen an die Python-Programme

Die funktionalen Anforderungen an das Python-Programm leiten sich aus dem Projektziel, sowie aus den durchgeführten Aufgaben der MS-SQL-Praktika ab. Sie beschreiben die Fähigkeiten, die das Python-System besitzen muss, um die Daten aus der migrierten SQLite-/SpatiaLite-Datenbank auszugeben und die Ergebnisse analog zur ursprünglichen SQL-Server-Umgebung darzustellen.

#### FP1 – Datenbankverbindung

Das Python-System muss eine Verbindung zur SQLite-Datenbank herstellen können.

#### FP2 – Laden der SpatiaLite-Erweiterung

Die SpatiaLite-Erweiterung muss korrekt eingebunden werden, sodass räumliche Funktionen verfügbar sind.

#### FP3 – Ausführung von SQL-Anweisungen

SQL-Statements müssen aus Python heraus ausgeführt werden können. Dies umfasst sowohl Sachdatenabfragen als auch räumliche Abfragen.

#### FP4 – Einlesen gefilterter Datenlagen

Gefilterte Resultsets müssen in geeignete Datenstrukturen (z. B. DataFrames) überführt werden können.

#### FP5 – Tabellarische Darstellung von Sachdaten

Die Ergebnisse nicht-räumlicher Abfragen müssen strukturiert und nachvollziehbar ausgegeben werden.

#### FP6 – Visualisierung räumlicher Daten

Geometrien müssen aus dem Datenbanksystem ausgelesen, interpretiert und grafisch dargestellt werden können.

### Übersicht funktionale Anforderungen an die Python-Programme

| Nummer | Anforderung | Beschreibung |
|--------|------------|--------------|
| FP1 | Datenbankverbindung | Aufbau einer Verbindung zu SQLite |
| FP2 | SpatiaLite laden | Aktivierung räumlicher Funktionen |
| FP3 | SQL-Ausführung | Ausführen relationaler und räumlicher Abfragen |
| FP4 | Datenübernahme | Überführung der Resultsets in Datenstrukturen |
| FP5 | Tabellarische Ausgabe | Strukturierte Darstellung von Sachdaten |
| FP6 | Visualisierung | Grafische Darstellung von Geometrien |

### Nicht-funktionale Anforderungen an die Python-Programme

Die nicht-funktionalen Anforderungen betreffen Eigenschaften der Python-Lösung, die über die reine Funktionserfüllung hinausgehen.

#### NP1 – Open-Source-Basis

Es sollen ausschließlich Open-Source-Komponenten eingesetzt werden. Dadurch bleibt die Lösung lizenzfrei, transparent und reproduzierbar.

#### NP2 – Wartbarkeit und Modularität

Der Code soll modular strukturiert sein. Verbindungslogik, Abfrageverwaltung und Datenverarbeitung werden getrennt, um:

- einzelne Komponenten unabhängig testen und erweitern zu können  
- die Wartbarkeit und Wiederverwendbarkeit zu erhöhen  

### Übersicht nicht-funktionale Anforderungen an die Python-Programme

| Nummer | Anforderung | Beschreibung |
|--------|------------|--------------|
| NP1 | Open-Source | Einsatz ausschließlich Open-Source-basierter Komponenten |
| NP2 | Wartbarkeit | Modularer Aufbau des Programmcodes |
| NP3 | Transparenz | nachvollziehbare Struktur des Programmcodes |

---
<div style="display: flex; justify-content: space-between;">
  <a href="21_Datengrundlage.md">◀ 2.1 Datengrundlage</a>
  <a href="23_Auswahl_Python_Bibliotheken.md">2.3 Auswahl der Python-Bibliotheken ▶</a>
</div>