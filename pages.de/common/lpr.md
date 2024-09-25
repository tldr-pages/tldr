# lpr

> CUPS-Programm zum Drucken von Dateien.
> Siehe auch: `lpstat` und `lpadmin`.
> Weitere Informationen: <https://openprinting.github.io/cups/doc/man-lpr.html>.

- Drucke eine Datei mit dem Standarddrucker:

`lpr {{pfad/zu/datei}}`

- Drucke 2 Kopien einer Datei:

`lpr -# {{2}} {{pfad/zu/datei}}`

- Drucke eine Datei mit einem bestimmten Drucker:

`lpr -P {{druckername}} {{pfad/zu/datei}}`

- Drucke entweder eine einzelne Seite (z. B. 2) oder mehrere Seiten (z. B. 2-16):

`lpr -o page-ranges={{2|2-16}} {{pfad/zu/datei}}`

- Drucke doppelseitig entweder gespiegelt an der langen oder an der kurzen Seite:

`lpr -o sides={{two-sided-long-edge|two-sided-short-edge}} {{pfad/zu/datei}}`

- Drucke mit festgelegter Papiergröße (je nach Drucker-Konfiguration gibt es mehr Optionen):

`lpr -o media={{a4|letter|legal}} {{pfad/zu/datei}}`

- Drucke mehrere Seiten pro Blatt:

`lpr -o number-up={{2|4|6|9|16}} {{pfad/zu/datei}}`
