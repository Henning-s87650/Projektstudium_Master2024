[zurück zur Startseite](../README.md)

## Referenzdaten

Als Referenz dienen die Ergebnisse der im Modul *Datenbanktechnologien* durchgeführten Übungen in
Microsoft SQL Server (MS SSMS). Für jeden Testfall wird eine fachlich äquivalente Abfrage in der
neuen Umgebung (SQLite/SpatiaLite + Python) ausgeführt und mit dem Resultat aus MS SSMS verglichen.

Der Vergleich erfolgt abhängig vom Testtyp über:
- **exakte Übereinstimmung** (z. B. Zeilenzahlen, Join-Ergebnisse, Aggregationen),
- **stichprobenbasierte Übereinstimmung** bei großen Tabellen (z. B. Zufallsstichproben),
- **toleranzbasierte Übereinstimmung** bei räumlichen Berechnungen (z. B. Fläche/Distanz),
  sofern unterschiedliche Rechenmodelle/Einheiten zwischen den Systemen auftreten können.

---
<div style="display: flex; justify-content: space-between;">
  <a href="7_Testen_der_Software.md">◀ 7 Testen der Software</a>
  <a href="72_Testfälle.md">7.2 Testfälle
 ▶</a>
</div>