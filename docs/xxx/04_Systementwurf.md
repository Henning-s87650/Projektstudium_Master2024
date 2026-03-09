# Systementwurf

Auf Basis der Anforderungsanalyse ergibt sich ein Systementwurf mit vier Komponenten. Das folgende Diagramm veranschaulicht diesen und zeigt die Interaktionen zwischen den verschiedenen Komponenten.

![UML-Diagramm des Systementwurfs](media/Schema_Systemkonzept.jpg)

Zusammenfassend lassen sich die einzelnen Kompenenten folgednermaßen beschreiben:

1. **Datenhaltung**  
   - SQLite-Datenbank mit SpatiaLite-Erweiterung  
   - Speicherung von Sach- und Geodaten  
   - möglichst exakte Abbildung der ursprünglichen MS-SQL-Server-Datenbank, um eine inhaltliche und funktionale Vergleichbarkeit sicherzustellen.

2. **Schnittstelle zur Datenhaltung**  
   - Python-basierte Verbindungslogik  
   - Öffnen der Datenbankinstanz  
   - Laden der SpatiaLite-Erweiterung  
   - Rückgabe eines Verbindungsobjekts, das in allen Auswertungsskripten wiederverwendet wird.

3. **Verwaltung der Verarbeitungsregeln**
   - enthält SQL-Satements für die Datenverarbeitung in Form eines Dictionary
   - jedes Statement besitzt ein "sprechendes" Schlüsselattribut
   - Nutzung der Schlüsselattribute zum Aufruf der SQL-Statements für die Datenverarbeitung

4. **Datenverarbeitung und Visualisierung**  
   - spezialisierte Python-Skripte für Analyse- und Visualisierungsaufgaben  
   - Auswahl passender SQL-Anweisung aus dem Dictionary
   - Übergabe des SQL-Statements und der Verbindungsparameter an die Datenbank  
   - Einlesen der gefilterten Datenlage in tabellarische Datenstrukturen
   - Ausgabe von Sachdaten im Terminal und zusätzliche Visualisierung von Geodaten.