[🏠 zurück zur Startseite](../README.md)

[◀ 3.1 Installation der benötigten Softwarekomponenten](31_Installation.md)

# 3.2 Setup der Projektumgebung

Dieses Kapitel beschreibt die projektspezifischen Einrichtungsschritte, die nach der Installation
der benötigten Softwarekomponenten erforderlich sind. Ziel des Setups ist es, die Projektdateien
so zu konfigurieren, dass die Python-Anwendungen ohne weitere Anpassungen ausgeführt werden können.

## Ablage der Projektdateien

Die Projektdateien werden lokal auf dem Rechner abgelegt. Dabei ist sicherzustellen, dass die
vorgesehene Projekt- und Verzeichnisstruktur entweder unverändert erhalten bleibt oder eine neue koherente Struktur angelegt wird, die der in dieser Dokumentation beschriebenen Struktur nachempfunden ist. Bei letzterem ist zu beachten, dass die Speicherorte von ``dbparam.py``, ``queries.py``, der Datenbankdatei, der SQLite- und SpatiaLite-Installation bekannt sind oder sich im gleichen Ordner befinden, wie die Auswertungsskripte. Der Speicherort kann frei gewählt werden, muss jedoch im weiteren Verlauf des
Setup explizit konfiguriert werden.

## Konfiguration der Datenbankschnittstelle

Die zentrale Konfiguration der Datenbankverbindung erfolgt in `dbparam.py`. In dieser
Datei sind die systemabhängigen Pfade hinterlegt, die für den Zugriff auf die Datenbank und das
Laden der SpatiaLite-Erweiterung erforderlich sind.

Folgende Parameter müssen an die jeweilige Systemumgebung angepasst werden:

- der Pfad zur SQLite-Datenbankdatei (`DB_PATH`),
- der Pfad zum Verzeichnis der SpatiaLite-Bibliotheken (`SPATIALITE_DIR`),
- der Pfad zur SpatiaLite-Erweiterungsdatei (`SPATIALITE_DLL`).

Diese Pfade sind abhängig vom Speicherort der Projektdateien sowie von der lokalen Installation
von SpatiaLite. Ohne eine korrekte Anpassung dieser Parameter ist kein erfolgreicher Aufbau der
Datenbankverbindung möglich.

Die Konfiguration erfolgt einmalig vor der ersten Ausführung der Anwendungen.

## Voraussetzungen für die Ausführung

Vor dem Start der Python-Skripte muss sichergestellt sein, dass:

- die im Kapitel *3.1 Installation der benötigten Softwarekomponenten* beschriebenen Programme
  installiert sind,
- die Projektdateien vollständig vorliegen,
- die Pfade in `dbparam.py` korrekt gesetzt sind,

Sind diese Voraussetzungen erfüllt, ist keine weitere Initialisierung oder Vorbereitung
erforderlich.

---
[4 Implementierung ▶](4_Implementierung.md)