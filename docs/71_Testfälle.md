[zurück zur Startseite](../README.md)

## 7.1 Testfälle

Die folgenden Tabellen listen die definierten Testfälle auf. Jeder Testfall ist einer Kategorie zugeordnet und referenziert die entsprechenden Anforderungen aus der Anforderungsanalyse.

### Testfälle zur Überprüfung der Datenbankmigration

Die folgenden Testfälle prüfen, ob die Migration der ursprünglichen MS-SQL-Server-Datenbank nach SQLite/SpatiaLite strukturell und datenbezogen korrekt durchgeführt wurde. Dabei wird überprüft, ob alle Tabellen vorhanden sind, die Primärschlüsselstrukturen korrekt übernommen wurden und die Anzahl der Datensätze mit der Referenzdatenbank übereinstimmt.

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T01 | Migration/Schema | Tabellen vorhanden | ND1 | identische Tabellen |
| T02 | Migration/Schema | PKs korrekt | ND2 | PK wie MS |
| T03 | Migration/Daten | Zeilenzahlen je Tabelle | ND3 | Zeilenzahlen identisch |

### Testfälle zur Überprüfung der Datenbankintegrität

Die folgenden Testfälle überprüfen die Integrität der übertragenen Daten. Im Fokus steht dabei die Konsistenz der Primär- und Fremdschlüsselbeziehungen. Ziel ist es sicherzustellen, dass durch die Migration keine Duplikate, fehlende Referenzen oder inkonsistente Datensätze entstanden sind.

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T04 | Integrität | PK eindeutig (einfach) | ND2 | 0 Duplikate |
| T05 | Integrität | PK eindeutig (zus.) | ND2 | 0 Duplikate |
| T06 | Integrität | FK-Orphans | ND2 | 0 Orphans |

### Testfälle zur Überprüfung der Daten

Diese Testfälle prüfen die fachliche Korrektheit der Datenabfragen sowie der räumlichen Berechnungen. Dazu werden ausgewählte SQL-Abfragen und räumliche Analysen ausgeführt und mit den Ergebnissen der Referenzumgebung verglichen. Je nach Testfall erfolgt der Vergleich über identische Ergebnismengen oder über toleranzbasierte Übereinstimmungen bei räumlichen Berechnungen.

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

Die folgenden Testfälle überprüfen die korrekte Integration der Python-Anwendungen mit der SQLite/SpatiaLite-Datenbank. Dabei wird insbesondere geprüft, ob die SpatiaLite-Erweiterung geladen werden kann, räumliche Geometrien korrekt verarbeitet werden und Visualisierungen der Geodaten fehlerfrei erzeugt werden.

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T16 | Python | SpatiaLite geladen | FP1, FP2 | keine Exception |
| T17 | Python/Geo | WKB → Shapely → Plot | FP6 | Plot ohne Fehler |

Die beschriebenen Testfälle bilden damit die Grundlage für die anschließende Durchführung der Tests und die Auswertung der Ergebnisse im folgenden Kapitel.

---

<div style="display: flex; justify-content: space-between;">
  <a href="7_Testen_der_Software.md">◀ 7 Testen der Software</a>
  <a href="72_Testergebnisse.md">7.2 Testergebnisse
 ▶</a>
</div>