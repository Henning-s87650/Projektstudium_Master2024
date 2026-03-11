/* 1 -> Geografie */

CREATE TABLE TempGeografie AS SELECT * FROM Geografie;
DROP TABLE Geografie;
CREATE TABLE Geografie (
    Land_ID TEXT PRIMARY KEY,
    Bundesland TEXT,
    Region TEXT,
    Staat TEXT,
    Flaeche MULTIPOLYGON
);
INSERT INTO Geografie SELECT * FROM TempGeografie;
DROP TABLE TempGeografie;

/* 2 -> Shop */

CREATE TABLE TempShop AS SELECT * FROM Shop;
DROP TABLE Shop;
CREATE TABLE Shop (
    Shop_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Ort TEXT,
    PLZ TEXT,
    Strasse TEXT,
    Land_ID TEXT,
    geom POINT,
    FOREIGN KEY (Land_ID) REFERENCES Geografie(Land_ID)
);
INSERT INTO Shop SELECT * FROM TempShop;
DROP TABLE TempShop;
ALTER TABLE Shop RENAME COLUMN geom TO Coordinate;

/* 3 -> Artikel: */

CREATE TABLE TempArtikel AS SELECT * FROM Artikel;
DROP TABLE Artikel;
CREATE TABLE Artikel (
    Artnr INTEGER PRIMARY KEY,
    Marke TEXT,
    Bezeichnung TEXT,
    Preis REAL,
    Artgruppe TEXT
);
INSERT INTO Artikel SELECT * FROM TempArtikel;
DROP TABLE TempArtikel;

/* 4 -> Mitarbeiter */

CREATE TABLE TempMitarbeiter AS SELECT * FROM Mitarbeiter;
DROP TABLE Mitarbeiter;
CREATE TABLE Mitarbeiter (
    Mitnr INTEGER PRIMARY KEY,
    Name TEXT,
    Vorname TEXT,
    Ort TEXT,
    Gebdat TEXT,
    Gehalt INTEGER,
    Shop_ID INTEGER,
    FOREIGN KEY (Shop_ID) REFERENCES Shop(Shop_ID)
);
INSERT INTO Mitarbeiter SELECT * FROM TempMitarbeiter;
DROP TABLE TempMitarbeiter;

/* 5 -> Bestand */

CREATE TABLE TempBestand AS SELECT * FROM Bestand;
DROP TABLE Bestand;
CREATE TABLE Bestand (
    Artnr INTEGER NOT NULL,
    Shop_ID INTEGER NOT NULL,
    Menge INTEGER,
    PRIMARY KEY (Artnr, Shop_ID),
    FOREIGN KEY (Artnr) REFERENCES Artikel(Artnr),
    FOREIGN KEY (Shop_ID) REFERENCES Shop(Shop_ID)
);
INSERT INTO Bestand SELECT * FROM TempBestand;
DROP TABLE TempBestand;

/* 6 -> Verkauf */

CREATE TABLE TempVerkauf AS SELECT * FROM Verkauf;
DROP TABLE Verkauf;
CREATE TABLE Verkauf (
    Artnr INTEGER NOT NULL,
    Shop_ID INTEGER NOT NULL,
    Datum TEXT NOT NULL,
    Menge INTEGER,
    Verkaufspreis REAL,
    PRIMARY KEY (Artnr, Shop_ID, Datum),
    FOREIGN KEY (Shop_ID) REFERENCES Shop(Shop_ID)
);
INSERT INTO Verkauf SELECT * FROM TempVerkauf;
DROP TABLE TempVerkauf;