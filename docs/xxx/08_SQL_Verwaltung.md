## 5.2.2 Verwaltung der SQL-Anweisungen (`queries.py`)

Das Modul `queries.py` dient der zentralen Verwaltung sämtlicher im Projekt verwendeter
SQL-Anweisungen. Alle Abfragen werden in einem Dictionary namens `SQL_QUERIES` hinterlegt, das die
SQL-Statements eindeutig identifizierbar und modular nutzbar macht.

### Struktur des Moduls

`SQL_QUERIES` ist wie folgt aufgebaut:

- **Schlüssel**  
  - kompakt, sprechend und eindeutig  
  - vollständig in **Großschreibung**  
  - Worttrennung über **Unterstriche**  

- **Werte**  
  - mehrzeilige SQL-Statements  
  - jeweils vollständig formulierte Abfragen  
  - werden unverändert in den Auswertungsskripten ausgeführt

Zur Veranschaulichung zeigt das folgende Codebeispiel einen Ausschnitt aus dem Anfang des Dictionary mit den SQL-Satements `GEBURTSTAGSKALENDER` und `MITARBEITER_WOHNORT`:

```python
SQL_QUERIES = {
    "GEBURTSTAGSKALENDER": """
        SELECT Name, Gebdat
        FROM Mitarbeiter
        ORDER BY
        CAST(substr(Gebdat, 5, 2) AS INTEGER),
        CAST(substr(Gebdat, 7, 2) AS INTEGER);
    """,

    "MITARBEITER_WOHNORT": """
        SELECT 
            M.Name AS Mitarbeiter, 
            M.Ort AS Wohnort, 
            S.Ort AS Arbeitsort
        FROM Mitarbeiter M
        JOIN Shop S ON M.Shop_ID = S.Shop_ID
        WHERE M.Ort != S.Ort;
    """,

    [...]
```

Die Auswertungsskripte importieren das Dictionary und greifen ausschließlich über den passenden
Schlüssel auf die benötigte Abfrage zu. Dadurch entfällt die Notwendigkeit, SQL-Strings in jedem
Skript separat zu pflegen und sie können bei Bedarf in weiteren Skripten wiederverwendet werden.

### Anpassung der SQL-Statements für SQLite

Die SQL-Anweisungen entsprechen nicht in allen Fällen ihren ursprünglichen Varianten aus der
MS-SQL-Server-Umgebung. Grund hierfür sind Unterschiede in den SQL-Dialekten von MS SQL-Server (Transact-SQL) und SQLite. Zum Ausdruck kommt dies im Projektkontext durch abweichende Datenypen und fehlende oder anders benannte SQL-Funkitonen. 

Ein exemplarisches Beispiel ist das Statement `GEBURTSTAGSKALENDER`. Das ursprüngliche Transact-SQL-Statement sieht folgendermaßen aus:

```sql
SELECT Name, gebdat
FROM Mitarbeiter
ORDER BY MONTH(gebdat), DAY(gebdat);
```

Dies musste angepasst werden. Zum einen besitzt das Attribut `gebdat` den Datentyp `date`, welcher in SQLite nicht vorhanden ist. Zum anderen werden für das Erstellen des Geburtstagskalenders der Mitarbeiter die Funktionen `MONTH()` und `DAY()` genutzt, welche in SQLite ebenfalls nicht zur Verfüfung stehen. Wie bereits im Kapitel *Datenbankmigration* beschrieben, wird `gebdat` in SQLite als `TEXT` im Format `YYYYMMDD` abgebildet. Da es zudem keine Funktionen wie `DAY()` oder `MONTH()` gibt, müssen Monat und Tag aus dem Text extrahiert werden:

```sql
CAST(substr(GebDat, 5, 2) AS INTEGER) AS Monat,
CAST(substr(GebDat, 7, 2) AS INTEGER) AS Tag
```

Diese Anpassung ermöglicht es, die fachliche Logik der MS SQL-Server-Aufgabe trotz genannter Abweichungen beizubehalten. Das vollständige SQL-Statement in SQLite sieht folgendermaßen aus:

```sql
SELECT Name, Gebdat
        FROM Mitarbeiter
        ORDER BY
        CAST(substr(Gebdat, 5, 2) AS INTEGER),
        CAST(substr(Gebdat, 7, 2) AS INTEGER);
```