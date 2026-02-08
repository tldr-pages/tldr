# bzip2

> Ein Block-Sortier-Dateikompressor.
> Siehe auch: `bzcat`, `bunzip2`, `bzip2recover`.
> Weitere Informationen: <https://manned.org/bzip2>.

- Komprimiere eine Datei:

`bzip2 {{pfad/zu/zu_komprimierende_datei}}`

- Dekomprimiere eine Datei:

`bzip2 {{[-d|--decompress]}} {{pfad/zu/komprimierte_datei.bz2}}`

- Dekomprimiere eine Datei nach `stdout`:

`bzip2 {{[-dc|--decompress --stdout]}} {{pfad/zu/komprimierte_datei.bz2}}`

- Tests die Integrität jeder Datei innerhalb der Archivdatei:

`bzip2 {{[-t|--test]}} {{pfad/zu/komprimierte_datei.bz2}}`

- Zeige das Komprimierungsverhältnis für jede verarbeitete Datei mit detaillierten Informationen:

`bzip2 {{[-v|--verbose]}} {{pfad/zu/komprimierte_dateien.bz2}}`

- Dekomprimiere eine Datei und überschreibe existierende Dateien:

`bzip2 {{[-f|--force]}} {{pfad/zu/komprimierte_datei.bz2}}`

- Zeige Hilfe:

`bzip2 {{[-h|--help]}}`
