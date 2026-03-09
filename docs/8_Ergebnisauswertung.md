[zurück zur Startseite](../README.md)

# Ergebnisauswertung

Die durchgeführten Testfälle zeigen, dass die Zielumgebung (SQLite in Kombination mit SpatiaLite und Python) die zuvor definierten funktionalen Anforderungen erfüllt. Die Tests bilden jedoch ausschließlich einen Funktionsnachweis.

Im Verlauf der Implementierung sind weitere Erkenntnisse entstanden, die nicht unmittelbar aus den Testfällen hervorgehen, jedoch für die Einordnung der Zielumgebung gegenüber der MS-SQL-Server-Umgebung relevant sind. Diese betreffen Unterschiede in der Typisierung der Datenbanksysteme, den Umgang mit Geodaten, Abweichungen im SQL-Dialekt sowie den zusätzlichen Installations- und Integrationsaufwand von SQLite.

## Dialektspezifische Unterschiede in SQL

Neben den Datentypen unterscheiden sich auch die SQL-Dialekte beider Systeme. Transact-SQL (MS SQL Server) bietet eine Vielzahl komfortabler Funktionen, die in SQLite nicht oder nur in angepasster Form existieren. Dies betrifft insbesondere Datumsfunktionen, Typkonvertierungen, bestimmte Stringoperationen sowie einzelne Aggregations- und Formatierungsfunktionen. In der Praxis bedeutete dies, dass jedes nicht-triviale SQL-Statement angepasst werden musste. Die Abfragen konnten fachlich äquivalent umgesetzt werden, jedoch nie unverändert übernommen werden. SQLite erweist sich dennoch in den untersuchten Bereichen als funktional gleichwertig.

## Unterschiede in der Typisierung

Ein grundlegender Unterschied zwischen Microsoft SQL Server und SQLite liegt im Typisierungskonzept. Der SQL Server arbeitet streng typisiert. Die Datenbank erzwingt die Einhaltung des Typs bei jedem ``INSERT`` oder ``UPDATE``. Datentypen wie ``date``, ``money`` oder ``geography`` besitzen daher klar definierte Eigenschaften und sind an die Typdefinition der jeweiligen Spalte gebunden. Bei einer Typinkompatibilität (bspw. dem Einfügen von Text in einer numerischen Spalte) wird eine Fehlermeldung ausgelöst und der Prozess abgebrochen. Dafür stehen umfangreiche datentypspezifische Funktionalitäten bereit, wie beispielsweise ``MONTH()`` und ``DAY()`` für die Verarbeitung des Datumformats.

SQLite verwendet ein dynamisches Typsystem und besitzt fünf grundlegende Type Affinities (``NULL``, `INTEGER`, ``REAL``, ``TEXT``, ``BLOB``). Deklarierte Typen wie ``VARCHAR`` oder ``DATETIME`` werden diesen zugeordnet. Im Rahmen der Migration führte dies zwangsläufig zu Vereinfachungen. Datumswerte wurden als ``TEXT`` gespeichert, Geldbeträge als ``REAL`` und Geodaten als ``BLOB``. Funktional ist diese Abbildung ausreichend, sie erfordert jedoch zusätzliche Anpassungen auf Abfrageebene. Ein Beispiel hierfür ist der Geburtstagskalender (``01_geburtstagskalender.py``). In SQL Server stehen typspezifische Funktionen wie ``MONTH()`` und ``DAY()`` unmittelbar zur Verfügung. In SQLite mussten Monat und Tag mittels ``substr()`` aus einem Textfeld extrahiert werden. Die fachliche Logik bleibt identisch, die technische Umsetzung wird jedoch umfangreicher. Die Unterschiede in der Typisierung stellen somit kein funktionales Problem dar, erhöhen jedoch die Komplexität der SQL-Statements.

## Unterschiede in der Geodatenverarbeitung

Bei der Betrachtung der Geodatenverarbeitung treten die festgestellten Unterschiede in ihrer Gesamtheit auf. Die Geodatentypen beider Systeme unterscheiden sich deutlich. Der SQL Server stellt mit den Datentypen ``geometry`` und ``geography`` native räumliche Datentypen bereit, die integraler Bestandteil des Datenbanksystems sind. Sie sind semantische Objekte, statt nur ein reines Speicherformat und enthalten u.a. Koordinateninformationen (SRID), Validierungslogik, Verarbeitungsmethoden und Berechnungslogik. Letztere sind sofort abrufbar und benötigen kein weiteres Setup für ihre Nutzung. Wird beispielsweise die Funktion ``STDistance()`` auf Objekte des Typs `geography` angewendet (siehe `04_abstand_shops_zur_htw.py`), liefert sie automatisch Distanzen automatisch in Metern. Eine vorherige Projektion der Koordinaten ist nicht erforderlich.

In SQLite werden Geometrien intern als ``BLOB`` gespeichert. Dabei handelt es sich um ein, durch einen Header erweitertes, WKB-Format. Für die Nutzung in Python mussten diese zunächst mittels ``ST_AsBinary()`` in das OGC-konforme WKB-Format überführt und anschließend mit Shapely interpretiert werden. Die Verarbeitung räumlicher Daten verteilt sich damit auf mehrere Ebenen: Die Speicherung und grundlegende Analyse erfolgt in der Datenbank über SpatiaLite, die Interpretation der Geometrien über Shapely, die Verarbeitung über GeoPandas und die Visualisierung über Matplotlib. Anders als ``geometry`` und ``geography`` ist `BLOB` ein reines Speicherformat. Die gleiche Berechnung mittels `ST_Distance()` benötigt zusätzliche Vorverarbeitungsschritte. Bei der Verwendung geographischer Koordinaten, berechnet die Funktion die Distanz in den Einheiten des zugrundeliegenden Referenzsystems, geographischer Länge und Breite. Aus diesem Grund ist eine vorherige Transformation mittels `Transform()` in ein metrisches, kartesisches Koordinatenreferenzsystem (z. B. ETRS89 / UTM Zone 32N, EPSG:25832) erforderlich. Erst nach dieser Projektion kann eine Distanzberechnung durchgeführt werden, deren Ergebnis in Metern vorliegt.

Die fachliche Korrektheit ist in beiden Systemen gewährleistet, jedoch unterscheidet sich der Grad der Automatisierung und Integration deutlich. SQL Server stellt mit den Datentypen ``geography`` und `geometry` eine stärker integrierte Lösung bereit, während SQLite/SpatiaLite eine explizite Behandlung des Koordinatenreferenzsystems erfordert. 

## Systemintegration

Die zuvor dargestellten Unterschiede lassen sich im Kern auf den Grad der Systemintegration zurückführen. Microsoft SQL Server ist als vollintegriertes relationales Datenbankmanagementsystem konzipiert. Datenhaltung, Typisierung, Geodatenverarbeitung, Benutzer- und Rechteverwaltung sowie Optimierungsmechanismen sind fester Bestandteil eines geschlossenen Gesamtsystems. Der Betrieb erfolgt serverbasiert, mit explizitem Nutzerhandling, Transaktionsmanagement und einer klaren Trennung zwischen Datenbankinstanz und Clientanwendung. Die räumlichen Datentypen sind integraler Bestandteil des Systems und erfordern keine zusätzliche Installation oder Konfiguration.

SQLite hingegen verfolgt einen anderen architektonischen Ansatz. Es handelt sich um eine dateibasierte Datenbank ohne eigene Serverinstanz. Die Datenbank ist eine einzelne Datei, die direkt von Anwendungen angesprochen wird. Erweiterte Funktionalitäten – insbesondere im Bereich der Geodaten – werden nicht systemintern bereitgestellt, sondern über externe Module wie SpatiaLite ergänzt. Auch die Weiterverarbeitung und Visualisierung der Daten erfolgt außerhalb der Datenbank, in diesem Projekt über Python-Bibliotheken wie Shapely, GeoPandas und Matplotlib. Die Gesamtfunktionalität entsteht somit durch das Zusammenspiel mehrerer Komponenten.

Diese Architektur bietet Vorteile hinsichtlich Portabilität, Offenheit und Flexibilität, erfordert jedoch einen höheren Integrations- und Konfigurationsaufwand. Während der SQL Server eine stark integrierte, zentral verwaltete Umgebung bereitstellt, stellt die Kombination aus SQLite, SpatiaLite und Python eine modulare Lösung dar, bei der Verantwortung für Koordinatenreferenzsysteme, Erweiterungen und Systemkompatibilität stärker beim Anwender liegt.

---
<div style="display: flex; justify-content: space-between;">
  <a href="73_Testergebnisse.md">◀ 7.3 Testergebnisse</a>
  <a href="9_Fazit.md">9 Fazit
 ▶</a>
</div>