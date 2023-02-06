# pdftocairo

> PDF-fájlokat konvertál PNG/JPEG/TIFF/PDF/PS/EPS/SVG-be a cairo segítségével. További információ: <https://poppler.freedesktop.org>.

- PDF fájl átalakítása JPEG-be:

`pdftocairo {{path/to/file.pdf}} -jpeg`

- Konvertálja PDF-be a kimenetet a papír kitöltésére kibővítve:

`pdftocairo {{path/to/file.pdf}} {{output.pdf}} -pdf -expand`

- Konvertálás SVG-be az első/utolsó konvertálandó oldal megadásával:

`pdftocairo {{path/to/file.pdf}} {{output.svg}} -svg -f {{first_page}} -l {{last_page}}`

- Konvertálás PNG-be 200ppi felbontással:

`pdftocairo {{path/to/file.pdf}} {{output.png}} -png -r 200`

- Konvertálás szürkeárnyalatos TIFF-be A3-as papírméret beállítása:

`pdftocairo {{path/to/file.pdf}} -tiff -gray -paper A3`

- Konvertálás PNG-be: A bal felső saroktól x és y képpontok levágása:

`pdftocairo {{path/to/file.pdf}} -png -x {{x_pixels}} -y {{y_pixels}}`
