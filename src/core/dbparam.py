# Import der notwendigen Bibliotheken
import os
import sqlite3
from pathlib import Path
from contextlib import contextmanager

# Pfad zu DB-Datei, dem SpatiaLite-Verzeichnis und der SpatiaLite-Erweiterungsdatei
DB_PATH = r"D:\Studium\Studienunterlagen\Master\03_Fachsemester\01_Projektstudium\Projektstudium_Master2024\data\gm23s87650.db"
SPATIALITE_DIR = r"C:\Program Files\Spatialite\mod_spatialite-5.1.0-win-amd64"
SPATIALITE_DLL = r"C:\Program Files\Spatialite\mod_spatialite-5.1.0-win-amd64\mod_spatialite.dll"

os.add_dll_directory(SPATIALITE_DIR)

@contextmanager
def connection():

    # Verbindung öffnen
    con = sqlite3.connect(DB_PATH)

    # SpatiaLite-Erweiterung laden
    con.enable_load_extension(True)
    con.load_extension(SPATIALITE_DLL)

    try:
        # Verbindung an den Aufrufer „übergeben“
        yield con
    finally:
        # Verbindung immer schließen – auch bei Fehlern im with-Block
        con.close()