[zurück zur Startseite](../README.md)

# 4 Implementierung

Dieses Kapitel beschreibt die technische Umsetzung der zuvor konzipierten Systemarchitektur. Ziel der Implementierung ist es, die bestehende MS-SQL-Server-Datenbankstruktur in eine auf SQLite und SpatiaLite basierende Open-Source-Umgebung zu überführen und eine Python-basierte Umgebung zur Auswertung und Visualisierung der Daten bereitzustellen.

Im ersten Schritt wird die Migration der Datenbankstruktur durchgeführt. Dabei werden Tabellen, Relationen und Geometrien aus der ursprünglichen MS-SQL-Server-Datenbank in eine funktional vergleichbare SQLite-/SpatiaLite-Struktur überführt. Ziel ist es, die fachliche Struktur der Ausgangsdatenbank möglichst unverändert abzubilden, um eine spätere Vergleichbarkeit der Systeme sicherzustellen.

Im zweiten Schritt erfolgt die Implementierung der Python-basierten Auswertungsumgebung. Hier werden Skripte entwickelt, die den Zugriff auf die SQLite-Datenbank ermöglichen, SQL-Abfragen ausführen und die resultierenden Daten für Analyse und Visualisierung aufbereiten.

Die folgenden Abschnitte dokumentieren die beiden Umsetzungsschritte und zeigen, wie aus der konzeptionellen Planung eine funktionsfähige Arbeitsumgebung entsteht. Diese bildet die Grundlage für die anschließende Überprüfung, ob mit SQLite und Python fachlich vergleichbare Ergebnisse zur ursprünglichen SQL-Server-Umgebung erzeugt werden können.

## Unterkapitel

- [4.1 Datenbankmigration](41_Migration.md)

- [4.2 Python-Programmierung](42_Pythonprogrammierung.md)

---
<div style="display: flex; justify-content: space-between;">
  <a href="32_Setup.md">◀ 3.2 Setup der Projektumgebung</a>
  <a href="41_Migration.md">4.1 Datenbankmigration ▶</a>
</div>  