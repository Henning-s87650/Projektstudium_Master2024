[🏠 zurück zur Startseite](../README.md)

[◀ 4.2 Python-Programmierung](42_Pythonprogrammierung.md)

# 5 Nutzung der Software auf externem Desktop

Dieses Kapitel beschreibt die Voraussetzungen und notwendigen Schritte zur Nutzung
und Wartung der entwickelten Softwarelösung auf einem anderen Desktop-Rechner.
Ziel ist es, die Übertragbarkeit der Projekdateien sicherzustellen und eine
Weiterverwendung der Anwendungen unabhängig vom ursprünglichen Entwicklungsrechner
zu ermöglichen.

Die entwickelte Softwarelösung ist so aufgebaut, dass sie
auf anderen Windows-Arbeitsrechnern ausgeführt oder nachgebildet werden kann, sofern die im Kapitel
[*3 Systemvoraussetzungen und Softwareinstallation*](3_System_und_Installation.md) beschriebenen Voraussetzungen erfüllt sind.

Für die Nutzung auf einem anderen Rechner sind folgende Schritte
erforderlich:

1. **Übertragung der Projektdateien**  
   Das vollständige Projektverzeichnis, bestehend aus den angefertigten Python-Skripten und -Modulen sowie der SQLite-Datenbankdatei,
   wird auf den Zielrechner übertragen. Eine Installation im klassischen Sinne ist nicht erforderlich.

2. **Anpassung systemabhängiger Pfade**  
   In der Datei `dbparam.py` sind Pfade zur SQLite-Datenbank, zum
   SpatiaLite-Verzeichnis sowie zur SpatiaLite-Erweiterungsdatei hinterlegt. Diese Pfade müssen auf dem Zielrechner
   überprüft und an die dortige Verzeichnisstruktur angepasst
   werden.

3. **Überprüfung der Laufzeitumgebung**  
   Vor der Ausführung der Anwendungen ist sicherzustellen, dass Python,
   die benötigten Python-Bibliotheken sowie SQLite und SpatiaLite korrekt
   installiert sind. Die Funktionsfähigkeit kann durch das Ausführen eines Python-Skripts überprüft werden.
   
   Zur Überprüfung der Funktionsfähigkeit werden folgende Anwendungen empfohlen:
   
   - `01_geburtstagskalender.py` für das Überprüfen der Funktionsfähigkeit des übertragenen Gesamtsystems. Die Anwendung funktioniert auch ohne SpatiaLite-Erweiterung, da keine räumlichen Funktionen im SQL-Statement verwendet werden. Zudem ist sie im *3.2.3 Python-Anwendungen für die Sachdatenwiedergabe* detailliert erklärt, was einen möglichen Fehlerfindungsprozess unterstützt.

   - `04_abstand_shops_zur_HTW.py` für das Überprüfen der Funktionsfähigkeit der SpatiaLite-Erweiterung. Die dort referenzierte SQL-Anweisung mit dem Schlüssel `ABSTAND_SHOPS_ZUR_HTW` enthält mehrere räumliche Funktionen, welche durch SpatiaLite bereitgestellt werden. Sollte die Ausführung dieser Anwendung fehlschlagen, jedoch die von `01_geburtstagskalender.py` nicht, **kann** das Problem auf die SpatiaLite-Erweiterung eingegrenzt werden.

   **Anmerkung:** Es ist dennoch empfohlen für eine Lokalisierung auftretender Fehlers, die während der Laufzeit der Anwendungen auftretenden Fehlermeldungen heranzuziehen. Fehlende oder fehlerhaft installierte Python-Bibliotheken sind ebenfalls auf diesem Weg identifizierbar.

Nach Durchführung dieser Schritte können die Python-Anwendungen auf dem neuen
Rechner ausgeführt werden. Die Programme sollten sich
identisch zur hier gezeigten Entwicklungsumgebung verhalten, da alle datenbankseitigen Operationen vollständig innerhalb der SQLite-Datenbankdatei ausgeführt werden.

---
[6 Anpassung und Erweiterung der Software ▶](6_Anpassung_Erweiterung.md)