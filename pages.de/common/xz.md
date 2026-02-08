# xz

> Komprimiere oder dekomprimiere XZ- und LZMA-Dateien.
> Weitere Informationen: <https://manned.org/xz>.

- Komprimiere eine Datei mit xz:

`xz {{pfad/zu/datei}}`

- Dekomprimiere eine XZ-Datei:

`xz {{[-d|--decompress]}} {{pfad/zu/datei.xz}}`

- Komprimiere eine Datei mit lzma:

`xz {{[-F|--format]}} lzma {{pfad/zu/datei}}`

- Dekomprimiere eine LZMA-Datei:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{pfad/zu/datei.lzma}}`

- Dekomprimiere eine Datei und schreibe nach `stdout` (impliziert `--keep`):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{pfad/zu/datei.xz}}`

- Komprimiere eine Datei, aber lösche die Originaldatei nicht:

`xz {{[-k|--keep]}} {{pfad/zu/datei}}`

- Komprimiere eine Datei mit der schnellsten Kompression:

`xz -0 {{pfad/zu/datei}}`

- Komprimiere eine Datei mit der besten Kompression:

`xz -9 {{pfad/zu/datei}}`
