[🏠 zurück zur Startseite](../README.md)

[◀ 2.4 Systementwurf](24_Systementwurf.md)

# 3 Systemvoraussetzungen und Softwareinstallation

Die entwickelte Lösung ist für den Einsatz auf einem lokalen Arbeitsplatzrechner konzipiert und wurde unter einem Windows-Betriebssystem implementiert sowie getestet. Die eingesetzten Softwarekomponenten sind grundsätzlich plattformunabhängig und nicht spezifisch an Windows gebunden.

Die Installation und Einbindung der SpatiaLite-Erweiterung erfolgt jedoch betriebssystemabhängig. Unter Windows wird SpatiaLite als dynamische Programmbibliothek (DLL) eingebunden und über die entsprechenden betriebssystemspezifischen Suchpfade geladen. In der vorliegenden Implementierung werden daher Windows-typische Dateipfade verwendet. Das Einbetten der erforderlichen DLL-Pfade erfolgt mithilfe der Python-Standardbibliothek.

Es ist hervorzuheben, dass SpatiaLite selbst ebenfalls plattformunabhängig ist. Die Wahl des Betriebssystems beeinflusst lediglich die konkrete Form der Installation.

Die Ausführung der Python-Skripte erfolgt lokal und ohne Server- oder Webkomponenten. Sämtliche Anwendungen werden im Benutzerkontext gestartet und greifen auf eine dateibasierte SQLite-Datenbank zu. Eine Mehrbenutzerfähigkeit oder der Betrieb in einer verteilten Systemumgebung ist nicht vorgesehen.

Im folgenden Kapitel ist die Installation und Konfiguration der benötigten Komponenten dargestellt, um die Grundlage für die anschließende Implementierung zu schaffen.

## Unterkapitel

- [3.1 Installation der benötigten Softwarekomponenten](31_Installation.md)

- [3.2 Setup der Projektumgebung](32_Setup.md)

---
[3.1 Installation der benötigten Softwarekomponenten ▶](31_Installation.md)