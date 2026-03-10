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

```text
Projektstudium_Master2024
├── README.md
├── data
│   └── gm23s87650.db
├── docs
│   ├── 1_Einleintung.md
│   ├── 21_Datengrundlage.md
│   ├── 22_Anforderungsanalyse.md
│   ├── 23_Auswahl_Python_Bibliotheken.md
│   ├── 24_Systementwurf.md
│   ├── 2_technische_Grundlagen.md
│   ├── 31_Installation.md
│   ├── 32_Setup.md
│   ├── 3_System_und_Installation.md
│   ├── 41_Migration.md
│   ├── 42_Pythonprogrammierung.md
│   ├── 4_Implementierung.md
│   ├── 5_Setup_anderer_Desktop.md
│   ├── 61_Erweiterung_SQL.md
│   ├── 62_Erweiterung_Datenverarbeitung.md
│   ├── 6_Anpassung_Erweiterung.md
│   ├── 71_Testfälle.md
│   ├── 72_Testergebnisse.md
│   ├── 7_Testen_der_Software.md
│   ├── 8_Ergebnisauswertung.md
│   ├── 9_Fazit.md
│   ├── media
│   │   ├── Add_DBC_QGIS.png
│   │   ├── Add_Layer_QGIS.png
│   │   ├── Artikel_Vali_SQLite.png
│   │   ├── Artikel_Vali_SSMS.png
│   │   ├── ER_Diagramm_Beziehung.png
│   │   ├── ER_Diagramm_MS_SSMS.png
│   │   ├── ER_Diagramm_SQL_Server_DB.png
│   │   ├── ER_Diagramm_SQLite_DB.png
│   │   ├── FME_DB_Verbindung.png
│   │   ├── FME_Prozess_ausfuehren.png
│   │   ├── Gebkalender_Py.png
│   │   ├── Gebkalender_SSMS.png
│   │   ├── Install_Py1.png
│   │   ├── Install_Py2.png
│   │   ├── Map_QGIS.png
│   │   ├── Mitarbeiter_Vali_SSMS.png
│   │   ├── Plots_Geodaten.png
│   │   ├── SQLServer_Reader_hinzufuegen.png
│   │   ├── Schema_Systemkonzept.jpg
│   │   ├── Shops_Bundeslaender.png
│   │   ├── Shops_QGIS.png
│   │   ├── SpatiaLite_Writer_hinzufuegen.png
│   │   ├── Test_Vollstaendigkeit_Mitarbeiter_SQLite.png
│   │   ├── Test_Vollstaendigkeit_Mitarbeiter_SSMS.png
│   │   ├── Test_Vollstaendigkeit_SQLServer.png
│   │   ├── Test_Vollstaendigkeit_SQLite.png
│   │   ├── Validierung_SQLite.png
│   │   ├── Validierung_SQLite2.png
│   │   ├── Verbundene_Reader_Writer.png
│   │   ├── agg_view_T09_SQLite.png
│   │   ├── agg_view_T09_SSMS.png
│   │   ├── bunte_Bundeslaender.png
│   │   ├── count_SQLite.png
│   │   ├── count_SSMS.png
│   │   ├── flaeche_SQLite.png
│   │   ├── flaeche_SSMS.png
│   │   ├── htw_distanz_SQLite.png
│   │   ├── htw_distanz_SSMS.png
│   │   ├── install_spatialite.png
│   │   ├── join_vali_t08_SQLite.png
│   │   └── join_vali_t08_SSMS.png
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-314.pyc
│   ├── core
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   ├── dbparam.cpython-314.pyc
│   │   │   └── queries.cpython-314.pyc
│   │   ├── dbparam.py
│   │   └── queries.py
│   ├── examples
│   │   ├── 00_beispiel.py
│   │   ├── new_queries.py
│   │   └── tester.py
│   └── script
│       ├── 01_geburtstagskalender.py
│       ├── 02_mitarbieter_wohnort.py
│       ├── 03_warenwert_gesamtbestand.py
│       ├── 04_abstand_shops_zur_htw.py
│       ├── 05_bestand_raeuchertofu.py
│       ├── 06_abstaende_shops.py
│       ├── 07_geometrie_darstellen.py
│       ├── 08_flaeche_bundeslaender.py
│       ├── 09_shops_und_bundeslaender.py
│       ├── 11_nachbarn_hessen.py
│       ├── 12_bestandswert_shops_je_bundesland.py
│       ├── 13_exklusives_einzugsgebiet.py
│       ├── __init__.py
│       └── __pycache__
│           └── 01_geburtstagskalender.cpython-314.pyc
```

## Technische Grundlage

Die Umsetzung basiert vollständig auf Open-Source-Technologien:

- SQLite (dateibasiertes relationales Datenbanksystem)
- SpatiaLite (räumliche Erweiterung für SQLite)
- Python 3
- pandas
- GeoPandas
- Shapely
- Matplotlib

## Reproduzierbarkeit

Zur Reproduktion der Ergebnisse ist erforderlich:

1. Installation von Python 3
2. Installation der genannten Bibliotheken
3. Bereitstellung der SQLite-/SpatiaLite-Datenbankdatei
4. Ausführung der jeweiligen Skripte im Ordner `src/script/`

Details zur Einrichtung sind in Kapitel 5 der Dokumentation beschrieben.

## Dokumentation

- ### [1 Einleitung](docs/1_Einleintung.md)
- ### [2 Technische Grundlagen](docs/2_technische_Grundlagen.md)
    - [2.1 Datengrundlage](docs/21_Datengrundlage.md)
    - [2.2 Anforderungsanalyse](docs/22_Anforderungsanalyse.md)
    - [2.3 Auswahl der Python-Bibliotheken](docs/23_Auswahl_Python_Bibliotheken.md)
    - [2.4 Systementwurf](docs/24_Systementwurf.md)

- ### [3 Systemvoraussetzungen und Softwareinstallation](docs/3_System_und_Installation.md)
    - [3.1 Installation](docs/31_Installation.md)
    - [3.2 Setup der Projektumgebung](docs/32_Setup.md)

- ### [4 Migration](docs/4_Implementierung.md)
    - [4.1 Datenbankmigration](docs/41_Migration.md)
    - [4.2 Python-Programmierung](docs/42_Pythonprogrammierung.md)

- ### [5 Nutzung der Software auf anderem Desktop](docs/5_Setup_anderer_Desktop.md)

- ### [6 Anpassung und Erweiterung der Software](docs/6_Anpassung_Erweiterung.md)

    - [6.1 Anpassung und Erweiterung der Software](docs/61_Erweiterung_SQL.md)
    - [6.2 Erweiterung der Datenverarbeitung](docs/62_Erweiterung_Datenverarbeitung.md)

- ### [7 Testen der Software](docs/7_Testen_der_Software.md)

    - [7.1 Testfälle](docs/71_Testfälle.md)
    - [7.2 Testergebnisse](docs/72_Testergebnisse.md)

- ### [8 Ergebnisauswertung](docs/8_Ergebnisauswertung.md)

- ### [9 Fazit](docs/9_Fazit.md)




---