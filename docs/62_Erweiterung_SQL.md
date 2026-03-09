[zurück zur Startseite](../README.md)

## 6.1 Erweiterung der SQL-Verwaltung

Neue SQL-Anweisungen können durch Ergänzung des Dictionaries ``SQL_QUERIES`` im Modul ``queries.py`` integriert werden. Jede Abfrage wird dabei unter einem eindeutigen, sprechenden Schlüssel abgelegt. Dieser kann anschließend von bestehenden oder neuen Python-Skripten referenziert werden.

Zur Demonstration wird eine einfache SELECT-Abfrage ergänzt:

```python
"ALLES_SELEKTIEREN": """
        SELECT * 
        FROM Mitarbeiter;
    """
```
Wie bereits im Kapitel *3.2.3 Python-Anwendungen für die Sachdatenwiedergabe* beschrieben, wird diese Abfrage im jeweiligen Auswertungsskript über ihren Schlüssel referenziert. Das folgende Beispiel zeigt ein demonstratives Skript namens `00_beispiel.py`:

```python
# Beispiel zur Demonstration des Einbindens zusätzlicher SQL-Statements

# Import der notwendigen Bibliotheken
import pandas as pd
from dbparam import connection
from queries import SQL_QUERIES

# Auswahl des SQL-Statements
query = SQL_QUERIES['ALLES_SELEKTIEREN']

# Einlesen der Tabelle unter Verwendung des Kontextmanagers
with connection() as conn:
    df = pd.read_sql(query, conn)

# Ausgabe der Daten
print("\n Die gesamte Tabelle Mitarbeiter: \n")
print(df)
```
Die neue SQL-Anweisung wird dabei an folgender Stelle referenziert:

```python
query = SQL_QUERIES['ALLES_SELEKTIEREN']
```

Alternativ ist es möglich, ein vollständig neues Dictionary für SQL-Anweisungen zu verwenden. Dazu wird eine neue Python-Datei angelegt, in der das Dictionary definiert ist, beispielsweise:

```python
NEW_SQL_QUERIES = {
    "ALLES_SELEKTIEREN": """
        SELECT * FROM Mitarbeiter;
    """
}
```
Dieses Dictionary wird in einer Datei `new_queries.py` gespeichert und kann anschließend in einem Auswertungsskript importiert werden:

```python
from new_queries import NEW_SQL_QUERIES
```

Das Auswertungsskript 00_beispiel.py muss dann entsprechend angepasst werden:

```python
# Beispiel zur Demonstration des Einbindens zusätzlicher SQL-Statements

import pandas as pd
from dbparam import connection
from new_queries import NEW_SQL_QUERIES

query = NEW_SQL_QUERIES['ALLES_SELEKTIEREN']

with connection() as conn:
    df = pd.read_sql(query, conn)

print("\n Die gesamte Tabelle Mitarbeiter:\n")
print(df)
```

In beiden Varianten ist ersichtlich, dass nur minimale Änderungen erforderlich sind, um neue SQL-Abfragen in das bestehende System zu integrieren.

---
<div style="display: flex; justify-content: space-between;">
  <a href="6_Anpassung_Erweiterung.md">◀ 6 Anpassung und Erweiterung der Software</a>
  <a href="63_Erweiterung_Datenverarbeitung.md">6.2 Erweiterung der Datenverarbeitung
 ▶</a>
</div>