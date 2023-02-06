# mutool

> PDF-fájlok konvertálása, információk lekérdezése és adatok kinyerése. További információ: <https://mupdf.com/docs>.

- Az 1-10. oldal átalakítása 10 PNG-be:

`mutool convert -o {{image%d.png}} {{file.pdf}} {{1-10}}`

- Egy PDF 2., 3. és 5. oldalának konvertálása szöveggé a standard kimeneten:

`mutool draw -F {{txt}} {{file.pdf}} {{2,3,5}}`

- Két PDF fájl összekapcsolása:

`mutool merge -o {{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- Információk lekérdezése a PDF-be ágyazott összes tartalomról:

`mutool info {{input.pdf}}`

- A PDF-be ágyazott összes kép, betűtípus és erőforrás kivonása az aktuális könyvtárba:

`mutool extract {{input.pdf}}`

- Egy PDF vázlatának (tartalomjegyzékének) kinyomtatása:

`mutool show {{input.pdf}} outline`
