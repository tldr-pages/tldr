# pdftotext

> PDF-fájlok átalakítása egyszerű szöveges formátumba. További információ: <https://www.xpdfreader.com/pdftotext-man.html>.

- A `filename.pdf` egyszerű szöveggé konvertálása és kinyomtatása a standard kimenetre:

`pdftotext {{filename.pdf}} -`

- A `filename.pdf` átalakítása egyszerű szöveggé és mentése `filename.txt` néven:

`pdftotext {{filename.pdf}}`

- A `filename.pdf` egyszerű szöveggé konvertálása és az elrendezés megőrzése:

`pdftotext -layout {{filename.pdf}}`

- A `input.pdf` átalakítása egyszerű szöveggé és mentése `output.txt` néven:

`pdftotext {{input.pdf}} {{output.txt}}`

- A `input.pdf` 2., 3. és 4. oldalának átalakítása egyszerű szöveggé és mentése `output.txt` néven:

`pdftotext -f {{2}} -l {{4}} {{input.pdf}} {{output.txt}}`
