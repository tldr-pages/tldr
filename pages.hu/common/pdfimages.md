# pdfimages

> Segédprogram képek kivonására PDF-ekből. További információ: <https://manned.org/pdfimages>.

- Kivonja az összes képet egy PDF-fájlból, és PNG-ként menti őket:

`pdfimages -png {{path/to/file.pdf}} {{filename_prefix}}`

- Képek kivonása a 3-5. oldalról:

`pdfimages -f {{3}} -l {{5}} {{path/to/file.pdf}} {{filename_prefix}}`

- Képek kivonása PDF-fájlból, és az oldalszám feltüntetése a kimeneti fájlnevekben:

`pdfimages -p {{path/to/file.pdf}} {{filename_prefix}}`

- A PDF-fájlban lévő összes képre vonatkozó információk listázása:

`pdfimages -list {{path/to/file.pdf}}`
