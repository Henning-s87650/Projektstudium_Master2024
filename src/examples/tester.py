# t11_null_geometrien.py
# Prüft NULL-Geometrien (und optional ST_IsEmpty) in definierten Tabellen/Spalten.
# Voraussetzung: connection() aus dbparam.py stellt sicher, dass SpatiaLite geladen ist.

import pandas as pd
from src.core.dbparam import connection

# ----------------------------
# Konfiguration: Hier anpassen
# ----------------------------
GEOM_CHECKS = [
    # ("Tabelle", "GeomSpalte")
    ("Geografie", "Flaeche"),
    # Beispiele (falls vorhanden):
    # ("Shop", "Geom"),
    # ("Bundesland", "Geom"),
]

# Optional: Zusätzlich prüfen, ob Geometrien "leer" sind (ST_IsEmpty = 1)
# Achtung: benötigt SpatiaLite-Funktion ST_IsEmpty
CHECK_EMPTY_GEOMS = True


def count_null_geoms(conn, table: str, geom_col: str) -> int:
    sql = f"SELECT COUNT(*) FROM {table} WHERE {geom_col} IS NULL;"
    return int(conn.execute(sql).fetchone()[0])


def count_empty_geoms(conn, table: str, geom_col: str) -> int:
    # ST_IsEmpty(geom) = 1 bedeutet leere Geometrie
    sql = f"""
        SELECT COUNT(*)
        FROM {table}
        WHERE {geom_col} IS NOT NULL
          AND ST_IsEmpty({geom_col}) = 1;
    """
    return int(conn.execute(sql).fetchone()[0])


def main() -> None:
    results = []

    with connection() as conn:
        for table, geom_col in GEOM_CHECKS:
            null_cnt = count_null_geoms(conn, table, geom_col)

            empty_cnt = None
            empty_err = None
            if CHECK_EMPTY_GEOMS:
                try:
                    empty_cnt = count_empty_geoms(conn, table, geom_col)
                except Exception as e:
                    # Falls ST_IsEmpty nicht verfügbar ist, brechen wir nicht ab,
                    # sondern dokumentieren es in der Ausgabe.
                    empty_err = str(e)

            results.append({
                "Tabelle": table,
                "Geometriespalte": geom_col,
                "NULL_Geometrien": null_cnt,
                "LEERE_Geometrien": empty_cnt if empty_cnt is not None else "n/a",
                "Hinweis": empty_err if empty_err else ""
            })

    df = pd.DataFrame(results)

    print("\nT11 – NULL-Geometrien Check\n")
    print(df.to_string(index=False))

    # Einfaches OK/FAIL-Kriterium:
    # FAIL wenn irgendwo NULL_Geometrien > 0 oder (wenn geprüft) LEERE_Geometrien > 0
    failed = False
    for row in results:
        if isinstance(row["NULL_Geometrien"], int) and row["NULL_Geometrien"] > 0:
            failed = True
        if CHECK_EMPTY_GEOMS and isinstance(row["LEERE_Geometrien"], int) and row["LEERE_Geometrien"] > 0:
            failed = True

    print("\nErgebnis:", "FAIL (Geometrien fehlen/leer)" if failed else "OK (keine NULL/leer Geometrien gefunden)")


if __name__ == "__main__":
    main()
