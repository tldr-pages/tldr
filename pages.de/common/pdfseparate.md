# pdfseparate

> Extrahiere die Seiten einer Portable Document Format (PDF) Datei.
> Weitere Informationen: <https://manpages.debian.org/latest/poppler-utils/pdfseparate.1.en.html>.

- Extrahiere die Seiten einer PDF Datei und speichere jede Seite als neue PDF Datei ab:

`pdfseparate {{pfad/zu/quelldatei.pdf}} {{pfad/zu/zieldatei-%d.pdf}}`

- Gib die erste Seite zum Extrahieren an:

`pdfseparate -f {{3}} {{pfad/zu/quelldatei.pdf}} {{pfad/zu/zieldatei-%d.pdf}}`

- Gib die letzte Seite zum Extrahieren an:

`pdfseparate -l {{10}} {{pfad/zu/quelldatei.pdf}} {{pfad/zu/zieldatei-%d.pdf}}`
