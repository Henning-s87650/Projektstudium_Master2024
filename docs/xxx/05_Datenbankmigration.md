# 5.1 Datenbankmigration

Die Migration der bestehenden MS-SQL-Server-Datenbank nach SQLite/SpatiaLite erfolgt mit zwei Werkzeugen:

- **DB Browser for SQLite (DBBrowser)** für die Erstellung des Schemas und der Datenbankdatei
- **Feature Manipulation Engine (FME)** für die Übertragung der Tabelleninhalte

Da beide Systeme unterschiedliche SQL-Dialekte verwenden, ist ein direkter Import des Datenbankschemas (bspw. via SQL-Datei) in SQLite nicht möglich. Obwohl es Erweiterungen für MS SSMS gibt, die eine Datenmigration nach SQLite ermöglichen, wurde der Migrationsprozess stattdessen mit der Software Feature Manipulation Engine (FME) durchgeführt. Ausschlaggebend hierfür war die Verfügbarkeit der Software in den Laboreinrichtungen der GI-Fakultät sowie vorhandene Vorkenntnisse im Umgang mit FME.

## 5.1.1 Erstellen des Datenbankschemas mit DB Browser for SQLite

Im DBBrowser for SQLite wird eine neue Datenbank erstellt und das Datenbankschema durch das Anlegen von Tabellen mit Schlüsselattributen und Constraints definiert. Die Datenbank heißt, entsprechend ihrem Gegenstück in MS SSMS, „gm23s87650.db“. Im Fenster „SQL ausführen“ werden dazu die nötigen SQL-Befehle ausgeführt. Das folgende Beispiel zeigt das SQL-Statement zum Erstellen der Tabelle *Bestand*.

```sql
CREATE TABLE Bestand (
    Artnr INTEGER NOT NULL,
    Shop_ID INTEGER NOT NULL,
    Menge INTEGER,
    CONSTRAINT PK_Bestand PRIMARY KEY(Shop_ID, Artnr),
    CONSTRAINT FK_Artnr FOREIGN KEY (Artnr) REFERENCES Artikel(Artnr),
    CONSTRAINT FK_Shop_id FOREIGN KEY (Shop_ID) REFERENCES Shop(Shop_ID)
);
```

Damit liegt eine leere, aber strukturell vorbereitete SQLite-Datenbank vor, die anschließend durch FME mit Inhalten befüllt wird.

### Unterschiede der Datentypen

Es ist zu beachten, dass sich die Datentypen der SQLite-Datenbank von denen der ursprünglichen MS-SQL-Server-Datenbank unterscheiden. SQLite besitzt lediglich fünf Datentypen:

- **NULL**
- **INTEGER**
- **REAL**
- **TEXT**
- **BLOB**

Dadurch kann die Bandbreite an Datentypen, welche SQL-Server/ Transact-SQL unterstützt nicht widergespiegelt werden. Beim Erstellen des Schemas werden daher die ursprünglichen Datentypen wie folgt in SQLite abgebildet:

- **int** wird zu **INTEGER**
- **money** wird zu **REAL**
- **date** wird zu **TEXT**
- **varchar** wird zu **TEXT**
- **geography** wird zu **BLOB**


## 5.1.2 Übertragung der Tabelleninhalte mit FME

Die eigentliche Migration der Datensätze erfolgt mithilfe von FME.  
Dazu wird ein Reader für die Originaldatenbank angelegt und anschließend ein Writer für die Zieldatenbank konfiguriert.

### Schritt 1: Reader konfigurieren (detaillierter ausarbeiten mit mehr Abbildungen)

- In FME wird ein neuer **Reader** hinzugefügt.
- Als Format wird **„Microsoft SQL Server Spatial“** gewählt.
- Im sich öffnenden Verbindungsfenster werden die gleichen Parameter eingetragen wie in MS SSMS (Servername, Datenbankname, Authentifizierung).
- Unter *Parameters → Constraints → Tables* werden die Tabellen ausgewählt, die übertragen werden sollen.
- Weitere Einstellungen sind nicht erforderlich.

Nach Bestätigung mit **OK** erzeugt FME für jede gewählte Tabelle ein Reader-Objekt im Canvas.

### Schritt 2: Writer konfigurieren (detaillierter ausarbeiten mit mehr Abbildungen)

- Für jeden Reader wird ein **Writer** hinzugefügt.
- Als Format wird **„SpatiaLite“** gewählt.
- Unter *Dataset* wird der Pfad zur zuvor erstellten Datei `gm23s87650.db` angegeben.
- Nach Bestätigung mit **OK** erscheint für jede Tabelle ein Writer-Objekt im Canvas.

### Schritt 3: Reader und Writer verbinden

- Jede Reader-Komponente wird mit ihrem zugehörigen Writer verbunden.
- Dies wird für alle Tabellen wiederholt.

![Abbildung mit verbundenen Readern und Writern]()

### Schritt 4: Prozess ausführen

- Der gesamte Prozess wird mit **Run** gestartet.
- FME liest die Daten aus MS SQL Server ein und schreibt sie in die SQLite/SpatiaLite-Datenbank.

![Abbildung des FME-Fensters mit markierten RUN-Button]()

Damit sind alle Tabelleninhalte in die SQLite-Datenbank übertragen worden.

## 5.1.4 Ergebnis des Migrationsprozesses

### Prüfung des Datenbankschemas

Nach der Übertragung folgt die Prüfung, ob der Migrationprozess in das neue System vollständig und korrekt durchgeführt wurde. Für diesen Schritt wird ein ER-Diagramm der neuen Datenbank erstellt. Da SQLite selbst keine Funktion zur Generierung eines ER-Diagramms bereitstellt, wird hierfür eine Drittsoftware genutzt.  

Zum Einsatz kommt die **DBeaver Community Edition**, ein Open-Source-Client zur Verwaltung verschiedener Datenbanksysteme (einschließlich SQLite). Dafür kann auch jede andere Software genutzt werden, welche im Stande ist, ER-Diagramme anhand einer Datenbankverbindung zu generieren, beispielsweise *DBVisualizer*. Die nachfolgende Abbildung zeigt das mithilfe von DBeaver erzeugte ER-Diagramm in der Martin-Notation.

![ER_Diagramm des Datenbankschemas](media/ER_Diagramm_SQLite_DB.png)

In DBeaver lassen sich zusätzlich die zugehörigen Constraints einsehen. Durch Auswahl der jeweiligen Beziehung im ER-Diagramm werden die betroffenen Attribute angezeigt.  

![ER_Diagram mit gewählter Beziehung](media/ER_Diagramm_Beziehung.png)

Das ER-Digramm zeigt, dass das Schema der SQLite-Datenbank, mit Ausnhame der Datentypen, identisch zur Originaldatenbank in SQL-Server ist.

### Prüfung der Tabelleninhalte

Das Überprüfen der Tabelleninhalte wird stichprobenartig und anhand quantitativer Kennwerte
vorgenommen. Ziel ist es, zu verifizieren, dass die Datenübertragung vollständig erfolgt ist und
die Inhalte der Tabellen in SQLite mit jenen der ursprünglichen MS-SQL-Server-Datenbank
übereinstimmen. Da einzelne Tabellen (z. B. `Verkauf`) zu groß für eine rein visuelle Kontrolle
sind, werden SQL-Anweisungen genutzt.

1. den Vergleich der Zeilenzahl (Vollständigkeit)
4. den Vergleich einfacher Aggregat-Signaturen (Plausibilitätsnachweis)
5. Deterministische Stichproben (reproduzierbare Sichtprüfung)

Die folgenden Unterabschnitte dokumentieren diese Prüfungen für die einzelnen Tabellen.

**Zeilenzahl**

Für den Vergleich der Zeilenanzahlen wird in beiden Systemen folgende SQL-Anweisung ausgeführt:

```sql
SELECT COUNT(*) AS count FROM Artikel;
```

| Tabellenname | Zeilenanzahl MS SSMS    | Zeilenanzahl SQLite |
|--------|-----------------------------------|------------------------------------------------------------------------------|
| Artikel    |200|200|
| Bestand    |3800|3800|
| Geografie    |47|47|
| Mitarbeiter    |53|53|
| Shop    |21|21|
| Verkauf    |310547|310547|

Da die Zeilenanzahlen der Tabellen beider Datenbanken identisch sind, ist davon auszugehen, dass die Datensätze vollständig übernommen wurden. Um zu Überprüfen, ob das tatsächlich zutrifft, werden Stichproben von zehn zufälligen Datensätzen aus der SQLite-Datenbank entnommen und im Anschluss in MS SSMS genau diese Datensätze ermittelt. Sind die Datensätze in der Referenzdatenbank vorhanden wird davon ausgegangen, dass die jeweiligen Tabellen in beiden Systemen übereinstimmen. Anahnd der Tabelle *Artikel* wird dieser Vorgang demonstriert. Mithilfe dieses SQL-Statements erfolgt zunächst die Entnahme 10 zufälliger Datensätze:

```sql
SELECT *
FROM (
    SELECT *
    FROM Artikel
    ORDER BY RANDOM()
    LIMIT 10
)
ORDER BY Artnr ASC
```

Die Unterabfrage gibt 10 zufällige Datensätze aus der Tabelle aus. Die übergeordnete Abfrage sortiert diese nach aufsteigender Artnr, um die Ausgaben visuell besser vergleichen zu können.

![Ergebnis der SQL-Abfrage in SQLite](media/Validierung_SQLite.png)

In MS SSMS wird folgende Abfrage genutzt, um die Datensätze in der Referenzdatenbank abzufragen:

```sql
SELECT * FROM Artikel
WHERE Artnr in (1102,1109,1512,1708,2001,2109,2112,2208,2306,2311)
ORDER BY Artnr ASC;
```

Die Ausgabe ist identisch zu ihrem Gegenstück in SQLite.

![Ergebnis der Überprüfung der Datensätze in MS SSMS](media/Validierung_SQLite2.png)

Somit ist davon auszugehen, dass beide Tabellen identisch sind. Die Ergebnisse dieser Analyse für die restlichen Tabellen zeigt, dass diese ebenfalls übereinstimmen. Somit ist bestätigt, dass die Datenbank für das Auslesen mithilfe von Python geeigent ist.