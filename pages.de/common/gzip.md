# gzip

> Komprimiere/Dekomprimiere Dateien mit `gzip`-Komprimierung (LZ77).
> Weitere Informationen: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Komprimiere eine Datei und ersetze sie durch ein `gzip`-Archiv:

`gzip {{pfad/zu/datei}}`

- Dekomprimiere eine Datei und ersetze sie durch die unkomprimierte Originalversion:

`gzip {{[-d|--decompress]}} {{pfad/zu/datei.gz}}`

- Zeige den Namen und den Reduktionsprozentsatz für jede komprimierte Datei:

`gzip {{[-v|--verbose]}} {{pfad/zu/datei.gz}}`

- Komprimiere eine Datei und behalte die Originaldatei:

`gzip {{[-k|--keep]}} {{pfad/zu/datei}}`

- Komprimiere eine Datei und spezifiziere den Ausgabedateinamen:

`gzip {{[-c|--stdout]}} {{pfad/zu/datei}} > {{pfad/zu/komprimierte_datei.gz}}`

- Dekomprimiere ein `gzip`-Archiv und spezifiziere den Ausgabedateinamen:

`gzip {{[-cd|--stdout --decompress]}} {{pfad/zu/datei.gz}} > {{pfad/zu/dekomprimierte_datei}}`

- Spezifiziere die Komprimierungsstufe. 1 ist am schnellsten (niedrige Kompression), 9 ist am langsamsten (hohe Kompression), 6 ist der Standard:

`gzip -{{1..9}} {{[-c|--stdout]}} {{pfad/zu/datei}} > {{pfad/zu/komprimierte_datei.gz}}`

- Liste den Inhalt einer komprimierten Datei:

`gzip {{[-l|--list]}} {{pfad/zu/datei.txt.gz}}`
