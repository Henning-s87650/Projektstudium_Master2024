## Testfälle (revidiert)

Die folgenden Testfälle prüfen die migrierte SQLite-/SpatiaLite-Datenbank sowie die
Python-basierten Auswertungsskripte hinsichtlich der in der Anforderungsanalyse
definierten Anforderungen. Die Testfälle sind so gewählt, dass sie sowohl
Migration/Integrität (ND1–ND3) als auch die zentralen fachlichen Fähigkeiten
(FD1–FD5) und Python-Funktionalitäten (FP1–FP6) abdecken.

### Migration / Schema / Daten (Preconditions)

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T01 | Migration/Schema | Tabellen vorhanden | ND1 | Tabellenmenge identisch (Soll-Tabellen vorhanden) |
| T02 | Migration/Schema | Primärschlüsseldefinitionen korrekt | ND2 | PK-Attribute je Tabelle entsprechen der MS-SQL-Referenz |
| T03 | Migration/Daten | Inhaltliche Übereinstimmung (Aggregat-Signaturen) | ND3 | Kennzahlen (z. B. COUNT, COUNT(DISTINCT PK), MIN/MAX/SUM ausgewählter Attribute) identisch |

### Integrität (Constraints)

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T04 | Integrität | PK eindeutig (einfach) | ND2 | 0 Duplikate bezogen auf den PK |
| T05 | Integrität | PK eindeutig (zusammengesetzt) | ND2 | 0 Duplikate bezogen auf den zusammengesetzten PK |
| T06 | Integrität | FK-Konsistenz + FK-Enforcement | ND2 | 0 FK-Orphans **und** FK-Prüfung aktiv (`PRAGMA foreign_keys = 1`) |

### Sachdaten (repräsentative Referenzabfragen gegen MS SSMS)

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T07 | Sachdaten | Geburtstagskalender (Sortierung/Format) | FD4, FP3, FP5 | identische Zeilenanzahl **und** identische Datensätze in deterministischer Sortierung (ORDER BY inkl. Tie-Breaker) |
| T08 | Sachdaten | Join Mitarbeiter–Shop (Join + Filter) | FD4, FP3, FP4 | identische Ergebnismenge als **Tupel-Set** über definierte Attribute (z. B. Mitarbeiter, Wohnort, Arbeitsort); Reihenfolge kein Kriterium |
| T09 | Sachdaten | Aggregation / View (Gruppierung + SUM) | FD4, FP3 | identische Gruppierungsschlüssel **und** identische Aggregatwerte je Gruppe; Reihenfolge kein Kriterium |

### Räumliche Daten (Spatial Preconditions + räumliche Abfragen + Berechnungen)

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T11 | Räumlich | Geometrien vorhanden + SRID konsistent | FD1 | `NULL`-Geometrien = 0 **und** SRID einheitlich = 4326 (Sollwert aus MS-SQL-Referenz) |
| T12 | Räumlich | Shops in Bundesland (Punkt-in-Polygon) | FD2, FP3 | identische Shop-Liste (Set-Vergleich der Shop-IDs) |
| T13 | Räumlich | Nachbar-Bundesländer (Topologie) | FD2, FP3 | identische Ergebnisliste (Set-Vergleich der Bundesländer) |
| T14 | Räumlich | Flächenberechnung Bundesländer | FD3, FP3 | Ergebniswerte innerhalb definierter Toleranz (Toleranz im Testfall begründet) |
| T15 | Räumlich | Distanz Shop–HTW | FD3, FP3 | Ergebniswerte innerhalb definierter Toleranz (Toleranz im Testfall begründet) |

### Python (Smoke-/Integrationstests)

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T16 | Python | Datenbankverbindung + SpatiaLite laden | FP1, FP2 | keine Exception beim Verbindungsaufbau und beim Laden der Erweiterung |
| T17 | Python/Geo | WKB → Shapely → Plot | FP6 | Visualisierung läuft ohne Fehler (Plot wird erzeugt) |

### Optimierung (optional)

| Test-ID | Kategorie | Ziel / Prüfpunkt | Referenzierte Anforderungen | Vergleichskriterium |
|---|---|---|---|---|
| T18 | Optimierung | Indexnutzung in Queryplan sichtbar | FD5 | `EXPLAIN QUERY PLAN` zeigt Indexzugriff für eine geeignete Beispielabfrage (vorher/nachher oder dokumentierter Plan) |
