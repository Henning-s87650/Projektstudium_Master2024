## 4.3 Auswahl der Python-Bibliotheken

Für die Umsetzung der in der Anforderungsanalyse formulierten Anforderungen an die Python-Programme ist die Auswahl geeigneter Bibliotheken von zentraler Bedeutung. Ziel ist ein skriptbasiertes System, das Sach- und Geodaten aus der SQLite-/SpatiaLite-Datenbank ausliest, auswertet und darstellt.

Die Bibliotheksauswahl orientiert sich dabei an den funktionalen Anforderungen **FP3 bis FP6** sowie der nicht-funktionalen Anforderung **NP1**.  
Der Verbindungsaufbau zur Datenbank erfolgt über das Python-Modul `sqlite3` und das Laden der Spatialite-Erweiterung mithilfe des Moduls `os`. Damit sind die Anforderungen **FP1** (Datenbankanbindung) und **FP2** (Laden der SpatiaLite-Erweiterung) bereits erfüllt. Diese beiden Anforderungen fließen daher nicht in die Formulierung der Auswahlkriterien ein.

---

### 4.3.1 Kriterien

Auf Basis der funktionalen Anforderungen werden folgende Kriterien für die Bewertung der Bibliotheken definiert:

| Kriterium | Beschreibung                                                                                 | Bezug |
|----------|-----------------------------------------------------------------------------------------------|-------|
| K1       | Verarbeitung von SQL – die Bibliothek muss SQL-Anweisungen an die Datenbank übergeben können | FP3   |
| K2       | Interpretation von Tabellenstrukturen – tabellarisch geordnete Daten interpretieren          | FP4   |
| K3       | Tabellarische Wiedergabe – tabellarische Daten wiedergeben                                   | FP5   |
| K4       | Grundlegende Interpretation von Geometrieformaten                                            | FP5   |
| K5       | Erweiterte Interpretation von Geometrieformaten – z. B. mehrteilige Geometrien               | FP5   |
| K6       | Visualisierung von Geometriedaten – Geometriedaten ad hoc darstellen                        | FP6   |

Die nicht-funktionale Anforderung **NP1 (Open-Source)** wird nicht als eigenes Kriterium aufgeführt, da bei der Recherche von vornherein ausschließlich Bibliotheken mit Open-Source-Lizenz betrachtet werden.

Auf Grundlage dessen wird eine Bewertungsmatrix erstellt, in der eine Auswahl relevanter Bibliotheken gegenübergestellt wird. Die betrachteten Bibliotheken wurden im Rahmen einer Recherche in Fachartikeln, Online-Foren und anhand von Downloadstatistiken ausgewählt.

---

### 4.3.2 Bewertungsmatrix

| Bibliothek | K1 | K2 | K3 | K4 | K5 | K6 |
|-----------|----|----|----|----|----|----|
| Shapely   | ✗  | ✗  | ✗  | ✓  | ✓  | ✗  |
| GeoPandas | ✗  | ✓  | ✓  | ✓  | ✓  | ✓  |
| Cartopy   | ✗  | ✗  | ✗  | ✓  | ✓  | ✓  |
| Folium    | ✗  | ✗  | ✗  | ✓  | ✗  | ✓  |
| ipyleaflet| ✗  | ✗  | ✗  | ✓  | ✗  | ✓  |
| leafmap   | ✗  | ✗  | ✗  | ✓  | ✓  | ✓  |

---

### 4.3.3 Bewertung der Bibliotheken

**GeoPandas**  
Die Matrix verdeutlicht, dass GeoPandas nahezu alle Kriterien erfüllt:

- Interpretation tabellarischer Datenstrukturen (K2),
- tabellarische Wiedergabe (K3),
- Verarbeitung grundlegender und mehrteiliger Geometrietypen (K4, K5),
- direkte Visualisierung von Geometriedaten (K6).

Damit deckt GeoPandas einen Großteil der Anforderungen **FP3 bis FP6** ab.

**Shapely**  
Shapely, auf dem GeoPandas technisch basiert, erfüllt die geometriebezogenen Kriterien (K4, K5), bietet jedoch:

- keine tabellarischen Datenstrukturen (K2, K3),
- keine eigenen Visualisierungsmöglichkeiten (K6).

Da Shapely vollständig in GeoPandas integriert ist, entsteht durch eine eigenständige Nutzung kein zusätzlicher Mehrwert.

**Cartopy**  
Cartopy unterstützt eine Vielzahl von Geometrietypen (K4, K5) und verfügt über umfangreiche Visualisierungsfunktionen (K6). Es bietet jedoch:

- keine tabellarische Datenverarbeitung (K2, K3),
- keine Schnittstellen zur SQL- oder Datenbankkommunikation (K1).

Abgesehen von einer breiten Palette kartographischer Projektions- und Darstellungsmöglichkeiten bietet Cartopy damit keine entscheidenden Vorteile für die Projektziele. Es eignet sich eher als Ergänzung, nicht jedoch als zentrale Bibliothek.

**Folium**  
Folium basiert auf dem JavaScript-Framework Leaflet und erzeugt interaktive Karten als HTML-Dokumente. Die Übergabe von Daten erfolgt über das GeoJSON-Format, wodurch Geometrien zuvor konvertiert werden müssen. Einschränkungen:

- keine Unterstützung für WKB oder WKT – eine direkte Nutzung der in SpatiaLite gespeicherten Geometriemodelle ist nicht möglich,
- keine Verarbeitung von SQL-Anweisungen (K1),
- keine Interpretation oder Ausgabe tabellarischer Datenstrukturen (K2, K3),
- nur grundlegende Geometrieformate (K4), keine mehrteiligen Geometrien (K5),
- Visualisierung (K6) ist browserbasiert und an das Generieren von HTML-Artefakten gebunden.

Aufgrund dieser Einschränkungen ist Folium für das Erreichen des Projektziels nicht geeignet.

**ipyleaflet**  
ipyleaflet ist eine an Jupyter-Notebooks angepasste Variante des Leaflet-Frameworks und verfolgt einen ähnlichen Ansatz wie Folium. Die Bibliothek ist vollständig auf interaktive Notebook-Umgebungen ausgerichtet. Wie bei Folium fehlen:

- Funktionen zur Interpretation tabellarischer Datenstrukturen (K2, K3),
- jede Art von SQL-Integration (K1).

Die Verarbeitung von Geometrien (K4) erfolgt über GeoJSON oder Koordinatenlisten. Die im Projekt benötigten WKB-Formate können nicht direkt eingelesen werden; komplexere Geometrien (K5) erfordern zusätzliche Vorverarbeitungsschritte. ipyleaflet bietet zwar umfangreiche interaktive Visualisierungsmöglichkeiten (K6), jedoch ausschließlich in Jupyter-Umgebungen. Insgesamt erfüllt die Bibliothek damit zu wenige der geforderten Kriterien und wird nicht weiter berücksichtigt.

**leafmap**  
leafmap ist noch stärker auf Notebook-Umgebungen spezialisiert und fungiert als Metawerkzeug, das verschiedene Visualisierungsframeworks zusammenführt.
Das Modul weißt folgende Defizite auf:

- keine Integration tabellarischer Strukturen oder SQL-Schnittstellen (K1, K2, K3),
- Interpretation geometrischer Datenformate erfolgt ausschließlich durch eingebundene Bibliotheken wie GeoPandas (K4, K5),
- Darstellung erfolgt über Notebook-Widgets, die außerhalb interaktiver Umgebungen nicht funktionsfähig sind (K6).

leafmap ist damit gut für interaktive Kartenerstellung in Jupyter-Umgebungen geeignet, verfolgt jedoch einen anderen Schwerpunkt als das Projektziel und wird daher ebenfalls nicht weiter betrachtet.

---

### 4.3.4 Ergebnis der Auswahl

Die systematische Bewertung zeigt, dass **GeoPandas** die einzige Bibliothek ist, die eine Mehrheit der geforderten Kriterien vollständig erfüllt. In Kombination mit:

- `pandas`,
- `Shapely`,
- `Matplotlib`

entsteht eine integrierte Umgebung, mit der sowohl Sachdaten als auch Geometrien verarbeitet und visualisiert werden können. GeoPandas bildet somit den zentralen Baustein der Python-Implementierung.