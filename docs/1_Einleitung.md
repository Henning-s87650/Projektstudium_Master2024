[🏠 zurück zur Startseite](../README.md)

# 1 Einleitung

Die Analyse und Visualisierung raumbezogener Daten ist ein zentraler Bestandteil geoinformatischer Anwendungen. Relationale Datenbanksysteme übernehmen dabei die strukturierte Speicherung und Verwaltung sowohl von Sachdaten als auch von Geometrien. Während etablierte Systeme wie Microsoft SQL Server (MS SQL Server) integrierte Lösungen für relationale und räumliche Daten bereitstellen, gewinnen Open-Source-Technologien zunehmend an Bedeutung.

Vor diesem Hintergrund untersucht die vorliegende Arbeit, ob eine auf SQLite und Python basierende Open-Source-Umgebung in der Lage ist, die räumlichen Funktionen einer bestehenden Microsoft-SQL-Server-Datenbank reproduzierbar umzusetzen. Ausgangspunkt des Projekts ist eine im Rahmen des Moduls Datenbanktechnologien entwickelte MS-SQL-Server-Datenbank. Diese dient als fachliches Referenzsystem. Ziel ist es, diese Referenzdatenbank in eine SQLite-Datenbank zu überführen und darauf aufbauend eine Python-basierte Auswertungs- und Visualisierungsumgebung zu implementieren.

Die zentrale Fragestellung lautet:

Kann eine Open-Source-Architektur aus SQLite und Python die funktionalen und räumlichen Aufgaben der Referenzumgebung fachlich identisch oder qualitativ vergleichbar reproduzieren?

Zur Beantwortung dieser Frage wird zunächst eine Anforderungsanalyse durchgeführt. Darauf aufbauend erfolgt der Entwurf einer Systemarchitektur. Anschließend werden geeignete Python-Bibliotheken recherchiert, bewertet und in die Zielumgebung integriert. Die bestehende Datenbank wird migriert und die erforderlichen Python-Anwendungen zur Abfrage, Verarbeitung und Visualisierung der Daten implementiert.

Die entwickelte Lösung wird abschließend anhand definierter Testfälle validiert. Dabei werden strukturelle Integrität, inhaltliche Konsistenz sowie die fachliche Korrektheit relationaler und räumlicher Operationen überprüft. Die Arbeit ist zugleich als technische Dokumentation konzipiert und soll die Architektur, Implementierung und Validierung des Systems nachvollziehbar darstellen.

Die Arbeit gliedert sich wie folgt: Kapitel 2 beschreibt die technischen Grundlagen sowie die Anforderungsanalyse und den Systementwurf. Kapitel 3 und 4 dokumentieren Installation, Migration und Implementierung der Zielumgebung. Kapitel 7 stellt die Testkonzeption und Validierung dar. Kapitel 8 diskutiert die Ergebnisse im Vergleich zur Referenzumgebung. Das Fazit fasst die zentralen Erkenntnisse zusammen und ordnet den Ansatz hinsichtlich seiner Einsatzmöglichkeiten ein.

---
[2 technische Grundlagen ▶](2_technische_Grundlagen.md)