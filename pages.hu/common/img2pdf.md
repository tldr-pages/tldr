# img2pdf

> Raszteres képek parancssori veszteségmentes konvertálása PDF-be. További információ: <https://gitlab.mister-muffin.de/josch/img2pdf>.

- Több képet egyetlen PDF-be konvertálhat úgy, hogy minden kép külön oldalon van:

`img2pdf {{path/to/image1.jpg}} {{path/to/image2.jpg}} --output {{path/to/file.pdf}}`

- Egy több képkockás képnek csak az első képkockáját konvertálja PDF-be:

`img2pdf {{path/to/file.gif}} --first-frame-only --output {{path/to/file.pdf}}`

- Automatikusan tájolja a képet, A4-es oldalméretet használjon fekvő módban, és vízszintesen 2 cm-es, függőlegesen pedig 5,1 cm-es keretet állítson be:

`img2pdf {{path/to/file.jpg}} --auto-orient --pagesize {{A4^T}} --border {{2cm}}:{{5.1cm}} --output {{path/to/file.pdf}}`

- Csak a nagyobb képeket zsugorítja 10 cm x 15 cm-es téglalapra egy 30x20 cm-es oldalon belül:

`img2pdf {{path/to/file.tiff}} --pagesize {{30cm}}x{{20cm}} --imgsize {{10cm}}x{{15cm}} --fit {{shrink}} --output {{path/to/file.pdf}}`

- Egy kép átalakítása PDF-be, és a metaadatok megadása az eredményül kapott fájlhoz:

`img2pdf {{path/to/file.png}} --title {{title}} --author {{author}} --creationdate {{1970-01-31}} --keywords {{keyword1 keyword2}} --subject {{subject}} --output {{path/to/file.pdf}}`
