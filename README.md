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
│   └──  media
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
```

# Quellenverzeichnis

- Sharma, N. (2023, 5. Juli). *70 Geospatial Python Libraries*. Medium. Abgerufen am 13. Dezember 2024, von https://medium.com/data-science-collective/70-geospatial-python-libraries-54604d815a7b

- Abdishakur. (2020, 28. Juli). *Best Libraries for Geospatial data Visualisation in Python* Towards Data Science. Abgerufen am 13. Dezember 2024, von https://towardsdatascience.com/best-libraries-for-geospatial-data-visualisation-in-python-d23834173b35/

- Rieke, C. (2018, 25. März). *Essential Geospatial Python libraries* Medium. Abgerufen am 13. Dezember 2024, von https://towardsdatascience.com/best-libraries-for-geospatial-data-visualisation-in-python-d23834173b35/

- Mitford, L. (2018, 22. Oktober). *Geo-spatial analysis with Python* Medium. Abgerufen am 13. Dezember 2024, von https://medium.com/@lisa.mitford/geo-spatial-analysis-with-python-fdddd69eebea

- Kumaraswamy, A. (2018, 22. Mai). *Top 7 libraries for geospatial analysis* Packtpub. Abgerufen am 13. Dezember 2024, von https://www.packtpub.com/en-us/learning/tech-guides/libraries-for-geospatial-analysis?srsltid=AfmBOoonpF7DqIJriJbKPFhPDgLRUiKlA7qUehsnBGyQSe5ytWm69ZaD

- *SpatialPython* (2016, 14. September). GitHub. Abgerufen am 26. März 2025, von https://github.com/SpatialPython/spatial_python?tab=readme-ov-file

- *Awesome-Geospatial* (2016, 6. Mai). GitHub. Abgerufen am 26. März 2025, von https://github.com/sacridini/Awesome-Geospatial

- GeoPandas developers. (2025, 22. Dezember). *GeoPandas Documentation*, Version 1.1.2. Abgerufen am 2. Februar 2026, von https://geopandas.org/en/stable/

- Sean Gillies and Shapely contributors. (2025, 24. September). *Shapely documentation*, Version 2.1.2. Abgerufen am 2. Februar 2026, von https://shapely.readthedocs.io/en/stable/

- Gillies, S. (2024, 16. September). *Fiona: access to simple geospatial feature data*, Version 1.10.1. Abgerufen am 2. Februar 2026, von https://fiona.readthedocs.io/en/stable/

- Brendan C. Ward and pyogrio contributors. (2025, 28. November). *pyogrio - bulk-oriented spatial vector file I/O using GDAL/OGR*, Version 0.12.1. Abgerufen am 2. Februar 2026, von https://pyogrio.readthedocs.io/en/latest/

- Story, R. (2025, 16. Juni). *Folium 0.20.0 documentation*, Version 0.20.0. Abgerufen am 2. Februar 2026, von https://python-visualization.github.io/folium/

- Jupyter Development Team. (2025, 13. Juni). *ipyleaflet documentation*, Version 0.20.0. Abgerufen am 2. Februar 2026, von https://ipyleaflet.readthedocs.io/

- Wu, Q., (2021). *Leafmap: A Python package for interactive mapping and geospatial analysis with minimal coding in a Jupyter environment*. Journal of Open Source Software, 6(63), 3414, https://doi.org/10.21105/joss.03414

- Cartopy contributors. (2025, 8. August). *Cartopy documentation*, Version 0.20. Abgerufen am 2. Februar 2026, von https://scitools.org.uk/cartopy/

- The Matplotlib development team. (2024, 13. Dezember). *Matplotlib documentation*, Version 3.10.8. Abgerufen am 2. Februar 2026, von https://cartopy.readthedocs.io/stable/
---