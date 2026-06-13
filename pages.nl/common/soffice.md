# soffice

> CLI voor de krachtige en gratis LibreOffice-suite.
> Meer informatie: <https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html>.

- Open één of meer bestanden in leesmodus:

`soffice --view {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon de inhoud van één of meer bestanden:

`soffice --cat {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Print bestanden met een specifieke printer:

`soffice --pt {{printer_naam}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Converteer alle `.doc` bestanden in de huidige map naar PDF:

`soffice --convert-to pdf *.doc`
