[🏠 zurück zur Startseite](../README.md)

[◀ 1 Einleitung](1_Einleitung.md)

# 2 technische Grundlagen

Dieses Kapitel definiert den fachlichen und technischen Referenzrahmen der Arbeit. Ziel ist es, die Ausgangssituation zu beschreiben, die Anforderungen an das Zielsystem systematisch abzuleiten und die konzeptionelle Grundlage für die spätere Implementierung und Validierung zu schaffen.

Als Referenz dient die im Modul Datenbanktechnologien entwickelte MS SQL Server-Datenbank. Ihre Tabellenstruktur, Datentypen, Relationen sowie die im Rahmen der Übungen realisierten Sach- und Geodatenabfragen definieren den funktionalen Leistungsumfang, den die Open-Source-Zielumgebung reproduzieren soll.

Aus dieser Referenz werden funktionale und nicht-funktionale Anforderungen abgeleitet. Diese Anforderungen konkretisieren, welche Eigenschaften die SQLite-Datenbank sowie die Python-basierte Auswertungsumgebung erfüllen müssen, um eine fachliche Gleichwertigkeit zur Referenzumgebung zu erreichen. Sie bilden damit die Bewertungsgrundlage für die spätere Testkonzeption und Ergebniseinordnung.

Auf Basis der Anforderungsanalyse erfolgt die Auswahl geeigneter Python-Bibliotheken. Die Bewertung orientiert sich an der Fähigkeit der Bibliotheken, relationale und räumliche Daten aus SQLite auszulesen, zu verarbeiten und zu visualisieren.

Abschließend wird ein Systementwurf vorgestellt, der die Architektur der Zielumgebung beschreibt. Er definiert die Interaktion zwischen Datenhaltung, Verbindungslogik, SQL-Verwaltung und Auswertungsskripten und stellt die konzeptionelle Grundlage für die in Kapitel 4 beschriebene Implementierung dar.

## Unterkapitel

- [2.1 Datengrundlage](21_Datengrundlage.md)

- [2.2 Anforderungsanalyse](22_Anforderungsanalyse.md)

- [2.3 Auswahl der Python-Bibliotheken](23_Auswahl_Python_Bibliotheken.md)

- [2.4 Systementwurf](24_Systementwurf.md)

---

[2.1 Datengrundlage
 ▶](21_Datengrundlage.md)