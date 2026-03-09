[zurück zur Startseite](../README.md)

# Testen der Software

Dieses Kapitel beschreibt die Überprüfung der entwickelten Softwarelösung hinsichtlich ihrer
fachlichen Korrektheit und Vergleichbarkeit mit der Referenzumgebung aus den MS-SQL-Server-Übungen
(MS SSMS). Ziel ist es, nachvollziehbar zu dokumentieren, ob die Migration der Datenbank nach SQLite/SpatiaLite vollständig und konsistent erfolgt ist. Zudem wird überprüft, ob die implementierten SQL-Abfragen und Python-Auswertungen Ergebnisse liefern, die den Resultaten der MS-SQL-Umgebung entsprechen.

Die Tests sind so gewählt, dass sie die zuvor definierten Anforderungen abdecken:
- Datenbankbezogen: **Tabellenstruktur, Relationen, inhaltliche Übereinstimmung** (ND1–ND3),
  sowie funktionale Anforderungen wie **Aggregation/Views, räumliche Abfragen, Berechnungen und Indizes**
  (FD1–FD5).
- Python-bezogen: **Datenbankverbindung inkl. SpatiaLite, Ausführung von SQL, tabellarische Ausgabe
  sowie Visualisierung von Geodaten** (FP1–FP6).

## Unterkapitel

- [7.1 Referenzdaten](71_Referenzdaten.md)

- [7.2 Testfälle](72_Testfälle.md)

- [7.3 Testergebnisse](73_Testergebnisse.md)

---
<div style="display: flex; justify-content: space-between;">
  <a href="63_Erweiterung_Datenverarbeitung.md">◀ 6.3 Erweiterung der Datenverarbeitung</a>
  <a href="71_Referenzdaten.md">7.1 Referenzdaten
 ▶</a>
</div>