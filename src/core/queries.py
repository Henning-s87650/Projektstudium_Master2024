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

    "WARENWERT_GESAMTBESTAND": """
        SELECT 
            G.Bundesland, 
            SUM(B.Menge * A.Preis) AS Gesamtwert_Warenbestand
        FROM Bestand B
        JOIN Shop S ON B.Shop_ID = S.Shop_ID
        JOIN Artikel A ON B.Artnr = A.Artnr
        JOIN Geografie G ON S.Land_ID = G.Land_ID
        GROUP BY G.Bundesland;
    """,

    "ABSTAND_SHOPS_ZUR_HTW_ALT" : """
        SELECT 
            S.Shop_ID, 
            S.Name AS Shop_Name, 
            ST_Distance(S.Coordinate, MakePoint(13.73490, 51.03767, 4326)) AS Distanz
        FROM Shop S
        ORDER BY Distanz ASC;
    """,

        "ABSTAND_SHOPS_ZUR_HTW" : """
       SELECT
            S.Shop_ID,
            S.Name AS Shop_Name,
            ST_Distance(
                Transform(S.Coordinate, 25832),
                Transform(MakePoint(13.73490, 51.03767, 4326), 25832)
            ) AS Distanz_m
        FROM Shop S
        WHERE S.Coordinate IS NOT NULL
        ORDER BY Distanz_m ASC;


    """,

    "BESTAND_RAEUCHERTOFU" : """
        SELECT 
            s.Shop_ID,
            s.Name,
            s.Ort,
            s.PLZ,
            s.Strasse,
            s.Land_ID,
            ST_Distance(S.Coordinate, MakePoint(13.73490, 51.03767, 25832)) AS Distanz_von_HTW,
            COALESCE(b.Menge, 0) AS RaeuchertofuBestand
        FROM Shop s
        LEFT JOIN Bestand b
            ON s.Shop_ID = b.Shop_ID
        LEFT JOIN Artikel a
            ON a.Artnr = b.Artnr
            AND a.Bezeichnung = 'Räuchertofu'
        ORDER BY Distanz_von_HTW;
    """,

    "ABSTAENDE_SHOPS_ALT": """
        SELECT 
            S1.Shop_ID AS Von_Shop_ID, 
            S2.Shop_ID AS Zu_Shop_ID, 
            ST_Distance(S1.Coordinate, S2.Coordinate) AS Distanz
        FROM Shop S1, Shop S2
        WHERE S1.Shop_ID < S2.Shop_ID
        ORDER BY Distanz ASC;
    """,

    "INHALT_GEOGRAFIE" : """
        SELECT
            Land_ID,
            Bundesland,
            Region,
            Staat,
            ST_AsBinary(Flaeche) AS Flaeche_WKB
        FROM Geografie;
    """,

    "SELECT_SACHSEN" : """
        SELECT
            Land_ID,
            Bundesland,
            Region,
            Staat,
            ST_AsBinary(Flaeche) AS Flaeche_WKB
        FROM Geografie
        WHERE Bundesland = 'Sachsen';
    """,

    "FLAECHE_BUNDESLAENDER2": """
        SELECT 
            Bundesland, 
            CAST(ST_Area(Transform(Flaeche, 25832)) / 1000000.0, 2) AS Flaeche_km2
        FROM Geografie
        WHERE Staat = 'Deutschland'
        ORDER BY Flaeche_km2 DESC;
    """
    ,

    "FLAECHE_BUNDESLAENDER": """
        SELECT 
            Bundesland, 
            ST_Area(Transform(Flaeche, 25832)) / 1000000 AS Flaeche_km2
        FROM Geografie
        WHERE Staat = 'Deutschland'
        AND ST_IsEmpty(Flaeche) = 0
        AND ST_SRID(Flaeche) = 4326
        ORDER BY Flaeche_km2 DESC;
    """,

    "SHOPS_BUNDESLAENDER" : """
        SELECT 
            g.Bundesland AS Name,
            'Bundesland' AS Typ,
        ST_AsBinary(g.Flaeche) AS Flaeche_WKB
        FROM Geografie g
        UNION ALL
        SELECT
            s.Name AS Name,
            'Shop' AS Typ,
        ST_AsBinary(s.Coordinate) AS wkb
        FROM Shop s
        WHERE s.Coordinate IS NOT NULL;
    """,

    "NACHBAR_HESSEN": """
        SELECT 
            G1.Bundesland AS Bundesland, 
            G2.Bundesland AS Nachbar_Bundesland
        FROM Geografie G1
        JOIN Geografie G2 ON ST_Touches(G1.Flaeche, G2.Flaeche)
        WHERE G1.Bundesland = 'Hessen' AND G2.Flaeche IS NOT NULL;
    """,

    "VIEW_BESTANDSWERT_BL" : """
        CREATE VIEW IF NOT EXISTS vw_Bestandswert AS
        SELECT 
            s.Shop_ID, 
            g.Bundesland, 
            SUM(b.Menge * a.Preis) AS Bestandswert
        FROM Shop s
        JOIN Bestand b ON s.Shop_ID = b.Shop_ID
        JOIN Artikel a ON b.Artnr = a.Artnr
        JOIN Geografie g ON g.Land_ID = s.Land_ID
        GROUP BY s.Shop_ID, g.Bundesland;
    """,

    "BESTANSWERT_PRO_KM2" : """
        SELECT
            g.Bundesland,
            g.Region,
            ST_Area(Transform(g.Flaeche, 25832)) / 1000000 AS Flaeche_km2,
            SUM(vw.Bestandswert) / (ST_Area(Transform(g.Flaeche, 25832)) / 1000000) AS Bestandswert_pro_km2
        FROM vw_Bestandswert AS vw
        JOIN Geografie AS g ON g.Bundesland = vw.Bundesland
        WHERE g.Flaeche IS NOT NULL AND ST_IsEmpty(g.Flaeche) = 0 AND ST_SRID(g.Flaeche) = 4326
        GROUP BY g.Bundesland, g.Region
        ORDER BY Bestandswert_pro_km2 DESC;
    """,

    "EXKLUSIVE_ARTIKEL": """
        WITH Artikel_Bundeslaender AS (
            SELECT A.Artnr, A.Bezeichnung, G.Bundesland
            FROM Bestand B
            JOIN Artikel A ON B.Artnr = A.Artnr
            JOIN Shop S ON B.Shop_ID = S.Shop_ID
            JOIN Geografie G ON S.Land_ID = G.Land_ID
        )
        SELECT AB1.Artnr, AB1.Bezeichnung, AB1.Bundesland
        FROM Artikel_Bundeslaender AB1
        WHERE NOT EXISTS (
            SELECT 1 FROM Artikel_Bundeslaender AB2
            WHERE AB1.Artnr = AB2.Artnr AND AB1.Bundesland != AB2.Bundesland
        )
        ORDER BY AB1.Bezeichnung;
    """,
    
    "EXKLUSIVES_EINZUGSGEBIET": """
        SELECT 
            S1.Shop_ID, 
            S1.Name AS Shop_Name, 
            G.Bundesland,
            COUNT(S2.Shop_ID) - 1 AS Anzahl_Konkurrenz_Shops, 
            ST_AsText(Transform(ST_Buffer(Transform(S1.Coordinate, 25832), 5000), 4326)) AS Pufferzone
        FROM Shop S1
        JOIN Geografie G ON S1.Land_ID = G.Land_ID
        JOIN Shop S2 ON ST_Distance(Transform(S1.Coordinate, 25832), Transform(S2.Coordinate, 25832)) <= 5000
        GROUP BY S1.Shop_ID, S1.Name, G.Bundesland
        ORDER BY Anzahl_Konkurrenz_Shops ASC;
    """,

    "ALLES_SELEKTIEREN": """
        SELECT * FROM Mitarbeiter;
    """

}