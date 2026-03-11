[🏠 zurück zur Startseite](../README.md)

[◀ 8 Ergebnisauswertung](8_Ergebnisauswertung.md)

# 9 Fazit

Ziel des Projektstudiums war die Untersuchung der Einsatzmöglichkeiten von Python-Open-Source-Bibliotheken zur Visualisierung raumbezogener Sachdaten aus Datenbanken. Im Projektverlauf konkretisierte sich diese Fragestellung dahingehend, ob eine auf SQLite, SpatiaLite und Python basierende Open-Source-Lösung in der Lage ist, die im Rahmen der SQL-Übungen erarbeiteten fachlichen und räumlichen Aufgaben funktional gleichwertig zu reproduzieren.

Die Ergebnisse zeigen, dass die gewählte Zielumgebung die definierten Anforderungen vollständig erfüllen kann. Relationale Abfragen, Join-Operationen, Aggregationen, Views sowie räumliche Operationen wie Punkt-in-Polygon-Selektionen, Flächenberechnungen und Distanzermittlungen konnten fachlich korrekt umgesetzt werden. Die durchgeführten Testfälle belegen die funktionale Gleichwertigkeit der Ergebnisse im Vergleich zur Referenzumgebung Microsoft SQL Server.

Gleichzeitig wurde deutlich, dass die Umsetzung in der Open-Source-Umgebung mit einem erhöhten technischen Aufwand verbunden ist. Unterschiede in der Typisierung, Anpassungen an den jeweiligen SQL-Dialekt sowie die explizite Behandlung von Geodaten und Koordinatenreferenzsystemen erfordern zusätzliche Implementierungsschritte. Während Microsoft SQL Server viele dieser Aspekte systemintern integriert bereitstellt, müssen sie in der SQLite/SpatiaLite-Umgebung bewusster und expliziter umgesetzt werden. Insbesondere der modulare Aufbau der Zielumgebung – bestehend aus SQLite, SpatiaLite und verschiedenen Python-Bibliotheken – führt zu einer stärkeren Eigenverantwortung hinsichtlich Konfiguration, Referenzsystembehandlung und Datenverarbeitung.

Die ursprünglich vorgesehene Anbindung über einen Object-Relational Mapper (SQLAlchemy) wurde im Projektverlauf zugunsten einer direkten Nutzung der ``sqlite3``-Schnittstelle verworfen, da diese für den untersuchten Anwendungsfall ausreichend und technisch transparenter erschien. Ebenso wurde anstelle einer eigenständigen Datenbankimplementierung die Migration der bestehenden Übungsdatenbank gewählt, um eine direkte Vergleichbarkeit der Ergebnisse sicherzustellen.

In der Gesamteinordnung zeigt sich, dass SQLite in Kombination mit SpatiaLite und Python eine fachlich geeignete Alternativlösung zur Bearbeitung der untersuchten Aufgaben darstellt. Die Lösung ist vollständig Open-Source-basiert, portabel und flexibel einsetzbar. Sie stellt jedoch keinen unmittelbar gleichwertigen Ersatz für ein integriertes, serverbasiertes relationales Datenbankmanagementsystem dar, da sie höhere Anforderungen an Konfiguration, Systemverständnis und explizite Implementierung stellt.

Die Arbeit kommt somit zu dem Ergebnis, dass die untersuchten Python-Open-Source-Bibliotheken in Verbindung mit einer SQLite/SpatiaLite-Datenbank grundsätzlich geeignet sind, raumbezogene Sachdaten zu analysieren und zu visualisieren. Die Eignung ist fachlich gegeben, der Implementierungsaufwand und der Integrationsgrad unterscheiden sich jedoch deutlich von einer proprietären, vollständig integrierten Datenbanklösung wie Microsoft SQL Server.