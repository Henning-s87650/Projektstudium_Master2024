[zurück zur Startseite](../README.md)

# 2.4  Auswahl der Python-Bibliotheken

Für die Umsetzung der in der Anforderungsanalyse formulierten Anforderungen an die Python-Programme ist die Auswahl geeigneter Bibliotheken von zentraler Bedeutung.

Auf Grundlage der in Abschnitt 2.2 definierten Anforderungen sowie des in Abschnitt 2.3 beschriebenen Systementwurfs ist eine geeignete Python-Open-Source-Bibliothek zur Verarbeitung und Visualisierung raumbezogener Sachdaten auszuwählen. Ziel ist ein skriptbasiertes System, das Sach- und Geodaten aus der SQLite-/SpatiaLite-Datenbank ausliest, auswertet und darstellt. 

Die Bibliotheksauswahl orientiert sich dabei an den funktionalen Anforderungen **FP3 bis FP6** sowie der nicht-funktionalen Anforderung **NP1 und NP2**.  
Der Verbindungsaufbau zur Datenbank erfolgt über das Python-Modul `sqlite3` und das Laden der Spatialite-Erweiterung mithilfe des Moduls `os`. Damit sind die Anforderungen **FP1** (Datenbankanbindung) und **FP2** (Laden der SpatiaLite-Erweiterung) bereits erfüllt. Sie fließen daher nicht in die Formulierung der Auswahlkriterien ein.

## Kriterien

Auf Basis der Anforderungen werden folgende Kriterien für die Bewertung der Bibliotheken definiert:

| Kriterium | Abgeleitet aus | Beschreibung |
|------------|----------------|--------------|
| K1 | FP3 | Möglichkeit zur Übergabe und Verarbeitung relationaler sowie räumlicher SQL-Abfragen |
| K2 | FP4 | Überführung von SQL-Resultsets in weiterverarbeitbare Python-Datenstrukturen |
| K3 | FP5 | Strukturierte tabellarische Darstellung von Sachdaten |
| K4 | FP6 | Grafische Darstellung von Punkt-, Linien- und Flächengeometrien |
| K5 | FP6 | Unterstützung komplexer Geometrietypen (z. B. MultiPolygon, MultiLineString) |
| K6 | NP1 | Verfügbarkeit unter einer Open-Source-Lizenz |
| K7 | NP2 | Unterstützung eines modularen Programmaufbaus |

### 2.4.1 Kurzbeschreibung der betrachteten Python-Geodatenbibliotheken

Die betrachteten Bibliotheken wurden im Rahmen einer Recherche in Fachartikeln, Online-Foren und anhand von Downloadstatistiken ausgewählt und werden in den folgenden Absätzen kurz beschrieben.

#### GeoPandas

GeoPandas ist eine Open-Source-Bibliothek zur Verarbeitung vektorbasierter Geodaten in Python. Sie erweitert das Datenmodell der Bibliothek *pandas* - den DataFrame - um die Möglichkeit, geometrische Objekte wie Punkte, Linien oder Flächen zu verwalten und räumlich zu verarbeiten. Die Geometrieverarbeitung basiert auf der Bibliothek *Shapely*, während Ein- und Ausgabeoperationen typischerweise über GDAL-basierte Schnittstellen (bspw. pygrio oder Fiona) erfolgen. Die Visualisierung von Daten wird über Matplotlib realisiert.

GeoPandas Developers (2024): *GeoPandas Documentation*.  
https://geopandas.org/

#### Shapely

Shapely ist eine Python-Bibliothek zur Erstellung und Analyse planarer Geometrien. Sie stellt eine Python-Schnittstelle zur GEOS-Bibliothek (Geometry Engine – Open Source) bereit und ermöglicht Operationen wie Pufferbildung, Verschneidung oder Flächenberechnung. Shapely bildet die geometrische Grundlage zahlreicher Python-GIS-Bibliotheken, insbesondere von GeoPandas.

Toblerity/Shapely Developers (2024): *Shapely Documentation*.  
https://shapely.readthedocs.io/

#### Fiona

Fiona ist eine GDAL-basierte Python-Bibliothek zum Lesen und Schreiben vektorbasierter Geodatenformate wie Shapefile oder GeoPackage. Der Schwerpunkt liegt auf der Datenein- und -ausgabe, nicht auf der Analyse oder Visualisierung. Fiona wird häufig als Input-Output-Komponente (IO-Komponente) innerhalb größerer Geodaten-Workflows verwendet.

Fiona Developers (2024): *Fiona Documentation*.  
https://fiona.readthedocs.io/

#### pyogrio

pyogrio ist eine moderne, performante Alternative zu Fiona und ermöglicht den Zugriff auf GDAL/OGR-Funktionalitäten aus Python. Die Bibliothek ist insbesondere auf effizientes Einlesen großer Vektordatensätze ausgerichtet und wird zunehmend im GeoPandas-Umfeld eingesetzt.

pyogrio Developers (2024): *pyogrio Documentation*.  
https://pyogrio.readthedocs.io/

#### PyQGIS

PyQGIS ist die Python-API des Desktop-GIS-Systems QGIS. Sie erlaubt den Zugriff auf die vollständige GIS-Funktionalität von QGIS, einschließlich Datenmanagement, Geoverarbeitung, Projektionen und Visualisierung. PyQGIS setzt eine installierte QGIS-Laufzeitumgebung voraus und wird häufig zur Automatisierung von GIS-Workflows eingesetzt.

QGIS Development Team (2024): *PyQGIS Developer Cookbook*.  
https://docs.qgis.org/

#### GRASS GIS Python API

GRASS GIS ist ein Open-Source-Geoinformationssystem mit umfangreichen Analysefunktionen. Über die Python-API (`grass.script`, `pygrass`) können Geoverarbeitungsprozesse automatisiert gesteuert werden. GRASS wird insbesondere im wissenschaftlichen Umfeld für räumliche Analysen eingesetzt.

GRASS Development Team (2024): *GRASS GIS Documentation*.  
https://grass.osgeo.org/documentation/

#### Folium

Folium ist eine Python-Bibliothek zur Erstellung interaktiver Webkarten. Sie basiert auf dem JavaScript-Framework Leaflet und erzeugt HTML-basierte Kartenanwendungen. Die Datenübergabe erfolgt typischerweise über GeoJSON-Strukturen. Folium eignet sich vor allem für die Erstellung interaktiver Visualisierungen im Webkontext.

Folium Developers (2024): *Folium Documentation*.  
https://python-visualization.github.io/folium/

#### ipyleaflet

ipyleaflet ist eine Jupyter-Notebook-Erweiterung zur Erstellung interaktiver Karten auf Basis von Leaflet. Die Bibliothek ist eng in das Jupyter-Ökosystem integriert und ermöglicht widgetbasierte Interaktionen innerhalb von Notebook-Umgebungen.

ipyleaflet Developers (2024): *ipyleaflet Documentation*.  
https://ipyleaflet.readthedocs.io/

#### leafmap

leafmap ist eine Python-Bibliothek zur interaktiven Kartenerstellung, die auf ipyleaflet aufbaut und zusätzliche Funktionen für Geodaten-Workflows bereitstellt. Sie wird häufig im Earth-Observation- und Remote-Sensing-Umfeld eingesetzt.

leafmap Developers (2024): *leafmap Documentation*.  
https://leafmap.org/

#### Cartopy

Cartopy ist eine Python-Bibliothek zur kartographischen Darstellung geographischer Daten. Sie erweitert Matplotlib um Projektionen und geographische Referenzsysteme und wird häufig für wissenschaftliche Karten verwendet.

Cartopy Developers (2024): *Cartopy Documentation*.  
https://scitools.org.uk/cartopy/

#### Matplotlib

Matplotlib ist eine allgemeine Python-Bibliothek zur Erstellung von Diagrammen und Grafiken. Sie stellt die grundlegende Visualisierungsinfrastruktur für viele wissenschaftliche Python-Bibliotheken bereit und dient häufig als Rendering-Backend für Geodatenbibliotheken wie GeoPandas oder Cartopy.

Matplotlib Developers (2024): *Matplotlib Documentation*.  
https://matplotlib.org/

## 2.4.2 Bewertung der betrachteten Python-Bibliotheken

Die Bibliotheken werden den Kriterien in einer Matrix gegenübergestellt. Das Erfüllen des jeweiligen Kriteriums ist in drei Kategorien eingeteilt:

- ✓ &nbsp;&nbsp;&nbsp;  Kriterium erfüllt
- (✓) &nbsp;  Kriterium teilweise erfüllt
- ✗ &nbsp;&nbsp;&nbsp;  Kriterium nicht erfüllt

| Bibliothek | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|------------|----|----|----|----|----|----|----|
| GeoPandas  | ✓  | ✓  | ✓  | ✓  | ✓  | ✓  | ✓  |
| Shapely    | ✗  | ✗  | ✗  | ✗  | ✓  | ✓  | ✓  |
| Fiona      | ✗  | (✓) | ✗ | ✗ | (✓) | ✓ | ✓ |
| pyogrio    | ✗  | (✓) | ✗ | ✗ | (✓) | ✓ | ✓ |
| PyQGIS     | ✓  | ✓  | (✓) | ✓ | ✓ | ✓ | (✓) |
| GRASS API  | ✓  | ✓  | (✓) | ✓ | ✓ | ✓ | (✓) |
| Folium     | ✗  | ✗  | ✗  | ✓  | (✓) | ✓  | ✓  |
| ipyleaflet | ✗  | ✗  | ✗  | ✓  | (✓) | ✓  | ✓  |
| leafmap    | ✗  | ✗  | ✗  | ✓  | (✓) | ✓  | ✓  |
| Cartopy    | ✗  | ✗  | ✗  | ✓  | ✓  | ✓  | ✓  |
| Matplotlib | ✗  | ✗  | ✗  | ✓* | ✗  | ✓  | ✓  |

Die Bewertungsmatrix verdeutlicht, dass die betrachteten Bibliotheken hinsichtlich ihres Funktionsumfangs unterschiedliche Schwerpunkte aufweisen. In den folgenden Abschnitten wird dieser jeweils entsprechend des Projektziels bewertet.

### GeoPandas

GeoPandas erfüllt als einzige der untersuchten Bibliotheken sämtliche funktionalen (K1–K5) sowie nicht-funktionalen Kriterien (K6–K8) vollständig. SQL-Resultsets lassen sich über die Integration mit pandas in weiterverarbeitbare Datenstrukturen überführen (K1, K2), wodurch sowohl die strukturierte tabellarische Ausgabe von Sachdaten (K3) als auch deren Weiterverarbeitung möglich ist. Die Bibliothek unterstützt die native Verarbeitung unterschiedlicher Geometrietypen, einschließlich komplexer Strukturen wie MultiPolygon oder MultiLineString (K5). Die Visualisierung erfolgt direkt innerhalb der Python-Umgebung, typischerweise über Matplotlib (K4).

Darüber hinaus ist GeoPandas vollständig Open Source (K6) und fügt sich modular in eine Python-basierte Systemarchitektur ein (K7). Der Datenfluss bleibt durch die transparente DataFrame-Struktur nachvollziehbar (K8). In der Gesamtbetrachtung stellt GeoPandas damit eine integrierte Lösung dar, die alle definierten Anforderungen abdeckt.

## Shapely

Shapely erfüllt ausschließlich das Kriterium der geometrischen Verarbeitung (K5). Die Bibliothek stellt eine leistungsfähige Geometrie-Engine bereit, unterstützt jedoch weder die Integration und Verarbeitung von SQL-Abfragen (K1) noch die Überführung relationaler Resultsets in tabellarische Strukturen (K2, K3). Eine eigene Visualisierungskomponente ist nicht vorhanden (K4).

Shapely ist zwar Open Source (K6) und modular einsetzbar (K7, K8), deckt jedoch nur einen Teilbereich der Anforderungen ab. In der Bewertungsmatrix wird Shapely daher zutreffend als reine Geometrie-Engine eingeordnet.

## Fiona und pyogrio

Fiona und pyogrio fungieren primär als IO-Schnittstellen für Vektordaten. Beide ermöglichen das Lesen und Schreiben geographischer Dateiformate, bieten jedoch keine eigenständige SQL-Verarbeitung (K1) und keine strukturierte tabellarische Darstellung (K3). Eine Weiterverarbeitung der eingelesenen Daten ist nur indirekt möglich (K2 (✓)), da zusätzliche Bibliotheken erforderlich sind.

Visualisierungsfunktionen sind nicht Bestandteil dieser Bibliotheken (K4). Die Unterstützung komplexer Geometrien erfolgt über die zugrunde liegenden GDAL-Strukturen, jedoch ohne eigene Analyse- oder Darstellungslogik (K5 (✓)).

Beide Projekte sind Open Source (K6) und modular nutzbar (K7, K8), stellen jedoch keine vollständige Lösung dar, sondern sind als Datenzugriffs-Bausteine innerhalb eines größeren Workflows zu verstehen.

## PyQGIS und GRASS GIS Python API

PyQGIS und die GRASS GIS Python API erfüllen die funktionalen Anforderungen weitgehend vollständig. Beide ermöglichen die Ausführung relationaler und räumlicher SQL-Abfragen (K1) und verfügen über eigene interne Datenmodelle zur Weiterverarbeitung (K2). Die tabellarische Ausgabe ist möglich, jedoch nicht in Form generischer Python-Datenstrukturen wie bei GeoPandas, weshalb K3 als teilweise erfüllt ((✓)) bewertet wird.

Beide Systeme unterstützen sämtliche relevanten Geometrietypen (K5) sowie deren Visualisierung (K4). Sie sind vollständig Open Source (K6).

Die Modularität (K7) ist jedoch durch die Bindung an eine vollständige GIS-Engine eingeschränkt und somit stark an das jeweilige System gekoppelt, wodurch eine isolierte Nutzung einzelner Komponenten weniger möglich ist. In der Matrix wird dies durch eine teilweise Erfüllung ((✓)) des Kriteriums K7 abgebildet.

## Folium, ipyleaflet und leafmap

Diese Bibliotheken sind auf die interaktive Visualisierung von Geodaten ausgerichtet. Sie ermöglichen die grafische Darstellung räumlicher Informationen (K4), häufig auf Basis von GeoJSON-Strukturen. Eine direkte SQL-Integration (K1) sowie die strukturierte Verarbeitung tabellarischer Sachdaten (K2, K3) sind jedoch nicht vorgesehen.

Komplexe Geometrien können dargestellt werden, sofern sie zuvor in geeignete Austauschformate überführt wurden (K5 (✓)).

Obwohl die Bibliotheken Open Source sind (K6) und modular eingesetzt werden können (K7, K8), erfüllen sie nur die Visualisierungsebene der Anforderungen und stellen keine integrierte Geodatenverarbeitungslösung dar.

## Cartopy

Cartopy dient der kartographischen Darstellung geographischer Daten und erweitert Matplotlib um Projektionen und geographische Referenzsysteme. Die Bibliothek erfüllt damit das Visualisierungskriterium (K4) und unterstützt die Darstellung verschiedener Geometrietypen (K5).

Eine SQL-Integration (K1) oder tabellarische Datenverarbeitung (K2, K3) ist nicht Bestandteil des Funktionsumfangs. Cartopy ist Open Source (K6) und modular nutzbar (K7, K8), adressiert jedoch ausschließlich die kartographische Darstellungsebene.

## Matplotlib

Matplotlib ist eine allgemeine Visualisierungsbibliothek ohne spezifische Geodatenlogik. Die grafische Darstellung von Geometrien ist möglich (K4), erfordert jedoch eine vorherige Aufbereitung der Daten. Eine native Unterstützung komplexer Geometriestrukturen (K5) ist nicht gegeben.

Die Bibliothek bietet weder SQL-Integration (K1) noch tabellarische Geodatenverarbeitung (K2, K3). Matplotlib ist vollständig Open Source (K6) und modular einsetzbar (K7, K8), stellt jedoch lediglich eine Visualisierungskomponente dar.

### 2.4.3 Ergebnis der Auswahl

Die Auswertung der Bewertungsmatrix zeigt, dass lediglich drei Bibliotheken – GeoPandas, PyQGIS und die GRASS GIS Python API – die funktionalen Kernanforderungen (K1–K5) grundsätzlich erfüllen. Während Shapely, Fiona und pyogrio jeweils zentrale Teilfunktionen bereitstellen, adressieren sie nur einzelne Aspekte der Verarbeitungskette und scheiden daher als eigenständige Gesamtlösungen aus. Die reinen Visualisierungsbibliotheken (Folium, ipyleaflet, leafmap, Cartopy, Matplotlib) decken ausschließlich die Darstellungsebene ab und erfüllen die Anforderungen an SQL-Verarbeitung und tabellarische Datenintegration nicht.

Während PyQGIS und GRASS GIS einen sehr hohen Funktionsumfang bieten, sind sie an GIS-Laufzeitumgebungen gebunden. Dies führt zu einer starken Systemkopplung, die über den im Systementwurf definierten Rahmen hinausgeht.

GeoPandas bietet demgegenüber eine integrierte, aber zugleich schlanke Lösung innerhalb der Python-Laufzeitumgebung. Die Bibliothek erlaubt eine konsistente Umsetzung des in Kapitel 2.3 beschriebenen Systemmodells und stellt bietet im Vergleich zu den untersuchten Komponentenbibliotheken eine deutlich höhere Funktionalität. Gegenüber GIS-Engines wie PyQGIS oder GRASS erfüllt GeoPandas die projektbezogenen Anforderungen vollständig, ohne an eine externe Laufzeitumgebung gebunden zu sein. Dadurch bleibt die Integrationsfähigkeit in eine reine Python-Anwendung gegeben und die Systemabhängigkeit entfällt.

Für die Umsetzung des in dieser Arbeit entwickelten Systemkonzepts wird daher GeoPandas als zentrale Bibliothek eingesetzt und bildet die Grundlage für die nachfolgende Implementierung.

---
<div style="display: flex; justify-content: space-between;">
  <a href="23_Systementwurf.md">◀ 2.3 Systementwurf</a>
  <a href="3_System_und_Installation.md">3 Systemvoraussetzungen und Softwareinstallation ▶</a>
</div>