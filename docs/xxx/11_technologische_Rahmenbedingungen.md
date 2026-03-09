## Technologische Rahmenbedingungen / Systemvoraussetzungen (evtl. ausarbeiten)

Die entwickelte Lösung ist für den Betrieb auf einem lokalen Arbeitsplatzrechner ausgelegt und wurde unter einem Windows-Betriebssystem implementiert und getestet. Die verwendeten Komponenten sind generell plattformunabhängig und nicht an Windows gebunden.

Plattformabhängig wiederum ist die Installation und das Laden der SpatiaLite-Erweiterung. Diese wird unter Windows als dynamsiche Programmbibliothek (DLL) eingebunden und über betriebssystemspezifische Suchpfade aufgerufen. Entsprechend werden in der Implementierung Windows-typische Dateipfade verwendet. Das Hinzufügen von DLL-Pfaden wird mithilfe der Python-Standardbibliothek vorgenommen. Bei Verwendung eines anderen Betriebssystem weicht die Installation von SpatiaLite hiervon ab.

**Anmerkung:** SpatiaLite ist ebenfalls nicht Windows-gebunden. Die Wahl von Windows als Betriebssystem bedingt jedoch diese Art von Installation.

Die Ausführung der Python-Skripte erfolgt lokal und ohne Server- oder Webkomponenten. Alle Anwendungen werden direkt im Benutzerkontext gestartet und greifen auf eine dateibasierte SQLite-Datenbank zu. Eine Mehrbenutzerfähigkeit oder der Betrieb in einer verteilten Umgebung ist nicht vorgesehen.

Geodaten werden in der Datenbank als SpatiaLite-Geometrien gespeichert und für die Verarbeitung in
Python in das binäre WKB-Format überführt. Die anschließende Interpretation und Visualisierung
erfolgt vollständig im Arbeitsspeicher.

Das System dient der fachlichen Reproduktion und Analyse der im Modul *Datenbanktechnologien*
behandelten Inhalte in einer alternativen technischen Umgebung und ist nicht als produktives
Informationssystem ausgelegt.