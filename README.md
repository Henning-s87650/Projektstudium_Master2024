# Untersuchung der Einsatzmöglichkeiten von Python-Open-Source-Bibliotheken zur Visualisierung raumbezogener Sachdaten aus Datenbanken

Projektstudium (Modul G396)  
Studiengang Geoinformatik/Management  
Hochschule für Technik und Wirtschaft Dresden  

---

Dieses Projekt untersucht die Einsatzmöglichkeiten von Python-Open-Source-Bibliotheken zur Verarbeitung und Visualisierung raumbezogener Sachdaten aus relationalen Datenbanken.
Im Fokus stehen die Migration einer MS-SQL-Server-Datenbank in eine SQLite-/SpatiaLite-Umgebung sowie die funktionale Reproduktion der im Modul *Datenbanktechnologien* entwickelten Aufgaben.



## Abstract

Ziel des Projektstudiums ist die Untersuchung, ob und in welcher Qualität Python-basierte Open-Source-Bibliotheken geeignet sind, raumbezogene Sachdaten aus relationalen Datenbanken auszulesen, zu verarbeiten und zu visualisieren.

Als Referenz dient eine im Modul *Datenbanktechnologien* entwickelte MS-SQL-Server-Datenbank. Diese wird in eine SQLite-/SpatiaLite-Umgebung überführt und funktional reproduziert. Auf dieser Grundlage wird ein modular aufgebautes Python-System implementiert, das relationale und räumliche Abfragen ausführt sowie Ergebnisse tabellarisch und kartographisch darstellt.

Die Untersuchung umfasst insbesondere:

- die Migration einer relationalen MS-SQL-Server-Datenbank nach SQLite,
- die Integration räumlicher Funktionalitäten mittels SpatiaLite,
- die Implementierung modularer Python-Programme zur Datenverarbeitung,
- die Visualisierung verschiedener Geometrietypen,
- sowie die Validierung und Bewertung der erzeugten Ergebnisse.

## Repository-Struktur

 **Ordnerstruktur erstellen und hier einfügen**

## Technische Grundlage

Die Umsetzung basiert vollständig auf Open-Source-Technologien:

- SQLite (dateibasiertes relationales Datenbanksystem)
- SpatiaLite (räumliche Erweiterung für SQLite)
- Python 3.x
- pandas
- GeoPandas
- Shapely
- Matplotlib

## Reproduzierbarkeit

Zur Reproduktion der Ergebnisse ist erforderlich:

1. Installation von Python 3.x
2. Installation der genannten Bibliotheken
3. Bereitstellung der SQLite-/SpatiaLite-Datenbankdatei
4. Ausführung der jeweiligen Skripte im Ordner `src/script/`

Details zur Einrichtung sind in Kapitel 3 der Dokumentation beschrieben.

## Dokumentation

- ### [1 Einleitung](docs/1_Einleintung.md)
- ### [2 Technische Grundlagen](docs/2_technische_Grundlagen.md)
    - [2.1 Datengrundlage](docs/21_Datengrundlage.md)
    - [2.2 Anforderungsanalyse](docs/22_Anforderungsanalyse.md)
    - [2.3 Systementwurf](docs/23_Systementwurf.md)
    - [2.4 Auswahl der Python-Bibliotheken](docs/24_Auswahl_Python_Bibliotheken.md)

- ### [3 Systemvoraussetzungen und Softwareinstallation](docs/3_System_und_Installation.md)
    - [3.1 Installation](docs/31_Installation.md)
    - [3.2 Setup der Projektumgebung](docs/32_Setup.md)

- ### [4 Migration](docs/4_Implementierung.md)
    - [4.1 Datenbankmigration](docs/41_Migration.md)
    - [4.2 Python-Programmierung](docs/42_Pythonprogrammierung.md)

- ### [5 Nutzung der Software auf anderem Desktop](docs/5_Setup_anderer_Desktop.md)

- ### [6 Anpassung und Erweiterung der Software](docs/6_Anapassung_Erweiterung.md)

    - [6.1 Anpassung und Erweiterung der Software](docs/61_neue_Systemumgebung.md)
    - [6.3 Erweiterung der Datenverarbeitung](docs/63_Erweiterung_Datenverarbeitung.md)

- ### [7 Testen der Software](docs/7_Testen_der_Software.md)

    - [7.1 Referenzdaten](docs/71_Referenzdaten.md)
    - [7.2 Testfälle](docs/72_Testfälle.md)
    - [7.3 Testergebnisse](docs/73_Testergebnisse.md)

- ### [8 Ergebnisauswertung](docs/8_Ergebnisauswertung.md)

- ### [9 Fazit](docs/9_Fazit.md)




---