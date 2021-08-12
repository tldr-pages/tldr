# pdftocairo

> Efectuează conversia fișierelor PDF în PNG/JPEG/TIFF/PDF/PS/EPS/SVG utilizând Cairo.
> Mai multe informaţii: <https://poppler.freedesktop.org>

- Conversia unui fișier PDF în JPEG:

`pdftocairo {{path/to/file.pdf}} -jpeg`

- Conversia în PDF extinderea ieșirii pentru a umple hârtia:

`pdftocairo {{path/to/file.pdf}} {{output.pdf}} -pdf -expand`

- Conversia la SVG specificând prima/ultima pagină pentru a converti:

`pdftocairo {{path/to/file.pdf}} {{output.svg}} -svg -f {{first_page}} -l {{last_page}}`

- Conversia la PNG cu rezoluție 200ppi:

`pdftocairo {{path/to/file.pdf}} {{output.png}} -png -r 200`

- Conversia în tonuri de gri setarea dimensiunii hârtiei la A3:

`pdftocairo {{path/to/file.pdf}} -tiff -gray -paper A3`

- Conversia la PNG decuparea x și y pixeli din colțul din stânga sus:

`pdftocairo {{path/to/file.pdf}} -png -x {{x_pixels}} -y {{y_pixels}}`
