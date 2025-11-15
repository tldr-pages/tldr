# inkscape

> Een SVG (Scalable Vector Graphics) bewerkingsprogramma.
> Voor Inkscape versies tot en met 0.92.x, gebruik -e in plaats van -o.
> Meer informatie: <https://inkscape.org>.

- Open een SVG-bestand in de Inkscape GUI:

`inkscape {{pad/naar/bestand.svg}}`

- Exporteer een SVG-bestand in een bitmap met het standaardformaat (PNG) en de standaardresolutie (96 DPI):

`inkscape {{pad/naar/bestand.svg}} {{[-o|--export-filename]}} {{pad/naar/bestandsnaam.png}}`

- Exporteer een SVG-bestand in een bitmap van 600x400 pixels (vervorming van de aspectverhouding mogelijk):

`inkscape {{pad/naar/bestand.svg}} {{[-o|--export-filename]}} {{pad/naar/bestandsnaam.png}} {{[-w|--export-width]}} 600 {{[-h|--export-height]}} 400`

- Exporteer de tekening (selectiekader van alle objecten) van een SVG-bestand in een bitmap:

`inkscape {{pad/naar/bestand.svg}} {{[-o|--export-filename]}} {{pad/naar/bestandsnaam.png}} {{[-D|--export-area-drawing]}}`

- Exporteer een enkel object, gezien zijn ID, in een bitmap:

`inkscape {{pad/naar/bestand.svg}} {{[-i|--export-id]}} {{id}} {{[-o|--export-filename]}} {{object.png}}`

- Exporteer een SVG-document naar PDF, converteer alle teksten naar paden:

`inkscape {{pad/naar/bestand.svg}} {{[-o|--export-filename]}} {{bestandsnaam.pdf}} {{[-T|--export-text-to-path]}}`

- Dupliceer het object met id="path123", roteer het duplicaat 90 graden, sla het bestand op, en sluit Inkscape af:

`inkscape {{pad/naar/bestand.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
