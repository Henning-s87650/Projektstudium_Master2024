## 2.4 Auswahl geeigneter Python-Open-Source-Bibliotheken

Auf Grundlage der in Abschnitt 2.2 definierten Anforderungen sowie des in Abschnitt 2.3 beschriebenen Systementwurfs ist eine geeignete Python-Open-Source-Bibliothek zur Verarbeitung und Visualisierung raumbezogener Sachdaten auszuwählen.

Gemäß Themenblatt besteht die Aufgabe darin, geeignete Bibliotheken zu recherchieren, deren Fähigkeiten zu analysieren und gegenüberzustellen sowie auf Basis dieser Analyse eine begründete Auswahl zu treffen :contentReference[oaicite:2]{index=2}. Ziel dieses Kapitels ist daher nicht die experimentelle Performanzmessung mehrerer Implementierungen, sondern eine systematische und argumentativ nachvollziehbare Entscheidungsfindung.

Die Auswahl erfolgt in zwei Schritten:

1. Funktionale Eignungsprüfung  
2. Argumentative Abwägung geeigneter Kandidaten  

---

### 2.4.1 Marktüberblick gängiger Python-Geodatenbibliotheken

Im Python-Ökosystem haben sich verschiedene Bibliotheken für die Verarbeitung und Visualisierung von Geodaten etabliert. Diese lassen sich funktional in mehrere Gruppen einteilen:

**Vektorbasierte Geodatenbibliotheken**
- GeoPandas  
- Shapely  
- Fiona  
- pyogrio  

**Rasterbasierte Bibliotheken**
- Rasterio  
- rioxarray  

**GIS-Engines mit Python-API**
- PyQGIS  
- GRASS GIS Python API  

**Visualisierungsbibliotheken**
- Matplotlib  
- Cartopy  
- Folium  

Rasterorientierte Bibliotheken werden im Folgenden nicht weiter betrachtet, da das Projekt ausschließlich auf der Verarbeitung von Vektor-Geodaten basiert (Punkt, Linie, Fläche).

Komponentenbibliotheken wie Shapely, Fiona oder pyogrio decken jeweils Teilaspekte (Geometrieverarbeitung bzw. Datenzugriff) ab, stellen jedoch keine vollständige Lösung zur integrierten Verarbeitung und Visualisierung dar. Sie sind als Bausteine relevant, jedoch keine eigenständigen Gesamtlösungen.

Damit verbleiben als realistische Kandidaten für eine integrierte Umsetzung:

- GeoPandas  
- PyQGIS  
- GRASS GIS Python API  

---

### 2.4.2 Stufe 1 – Funktionale Eignungsprüfung

In einem ersten Schritt wird geprüft, ob die betrachteten Bibliotheken die funktionalen Mindestanforderungen erfüllen.

| Kriterium | Beschreibung |
|-----------|-------------|
| F1 | Integration von SQL-basierten Daten |
| F2 | Verarbeitung tabellarischer Sachdaten |
| F3 | Unterstützung von Punkt-, Linien- und Flächengeometrien |
| F4 | Unterstützung komplexer Geometrien |
| F5 | Visualisierung räumlicher Daten |
| F6 | Darstellung qualitativer und quantitativer Attribute |
| F7 | Open-Source-Lizenz |

**GeoPandas** erfüllt alle Kriterien. SQL-Resultsets können in DataFrames eingelesen, geometrische Objekte verarbeitet und visualisiert werden.

**PyQGIS** erfüllt ebenfalls alle funktionalen Anforderungen. Die Bibliothek bietet umfassende Geoverarbeitung, Visualisierung und Datenbankanbindung.

**GRASS GIS** stellt ebenfalls eine vollständige Geoverarbeitungsumgebung bereit und erfüllt die funktionalen Anforderungen.

Die funktionale Eignungsprüfung führt somit zu keinem eindeutigen Ergebnis. Alle drei Kandidaten sind grundsätzlich geeignet.

---

### 2.4.3 Stufe 2 – Argumentative Abwägung im Kontext des Systementwurfs

Da mehrere Bibliotheken funktional geeignet sind, erfolgt eine zweite Bewertungsebene. Diese berücksichtigt die im Systementwurf definierten Architekturprinzipien :contentReference[oaicite:3]{index=3}:

- klare Trennung von Datenhaltung, Schnittstelle und Verarbeitungslogik  
- modulare Erweiterbarkeit  
- reproduzierbare Open-Source-Umgebung  

Folgende Kriterien werden herangezogen:

| Kriterium | Beschreibung |
|-----------|-------------|
| A1 | Integrationsfähigkeit in ein eigenständiges Python-Skript |
| A2 | Komplexität der Systemabhängigkeiten |
| A3 | Modularität und klare Trennung der Komponenten |
| A4 | Nachvollziehbarkeit des Datenflusses |
| A5 | Etablierung im Python-Geodaten-Ökosystem |

#### PyQGIS

PyQGIS ist eng an die QGIS-Laufzeitumgebung gebunden. Die Python-API fungiert als Schnittstelle zu einem vollständigen GIS-System. Dadurch entstehen zusätzliche Abhängigkeiten sowie eine stärkere Kopplung an eine externe Softwareumgebung. Der Funktionsumfang geht deutlich über die Anforderungen des Projektes hinaus.

#### GRASS GIS

GRASS verfolgt ein ähnliches Paradigma. Auch hier steht eine eigenständige GIS-Engine im Mittelpunkt. Die Integration in ein schlankes, skriptbasiertes System erfordert zusätzliche Konfigurations- und Laufzeitumgebungen.

#### GeoPandas

GeoPandas integriert sich direkt in die Python-Laufzeitumgebung. Die Verarbeitung erfolgt innerhalb eines klar nachvollziehbaren Skripts, das die in Abschnitt 2.3 beschriebene Trennung zwischen Datenbankzugriff, SQL-Logik und Visualisierung unterstützt :contentReference[oaicite:4]{index=4}. Die Abhängigkeiten beschränken sich auf etablierte Python-Bibliotheken (pandas, Shapely, Matplotlib).

Die Bibliothek ist im Python-Geodaten-Ökosystem weit verbreitet und stellt einen de-facto-Standard für vektorbasierte Geodatenverarbeitung dar.

---

### 2.4.4 Auswahlentscheidung

Die funktionale Analyse zeigt, dass mehrere Bibliotheken grundsätzlich geeignet sind. Erst die argumentative Abwägung im Kontext der definierten Architekturprinzipien führt zu einer Differenzierung.

GeoPandas erfüllt die funktionalen Anforderungen vollständig und ermöglicht gleichzeitig eine konsistente Umsetzung des im Systementwurf beschriebenen modularen Konzepts. Die Integration erfolgt direkt innerhalb einer Python-Umgebung ohne zusätzliche externe GIS-Laufzeit.

Auf dieser Grundlage wird GeoPandas als zentrale Bibliothek für die weitere Implementierung ausgewählt.

Die Entscheidung basiert somit nicht auf einer isolierten Betrachtung einzelner Funktionen, sondern auf einer systematischen Analyse unter Berücksichtigung der Projektanforderungen und des konzipierten Systemmodells.