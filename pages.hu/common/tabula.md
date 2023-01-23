# tabula

> Táblázatok kivonása PDF-fájlokból. További információ: <https://tabula.technology>.

- Az összes táblázat kivonása egy PDF-ből egy CSV-fájlba:

`tabula -o {{file.csv}} {{file.pdf}}`

- Az összes táblázat kivonása egy PDF-ből egy JSON-fájlba:

`tabula --format JSON -o {{file.json}} {{file.pdf}}`

- Táblázatok kivonása a PDF 1., 2., 3. és 6. oldaláról:

`tabula --pages {{1-3,6}} {{file.pdf}}`

- Táblázatok kivonása egy PDF 1. oldaláról, kitalálva, hogy az oldal mely részét vizsgálja:

`tabula --guess --pages {{1}} {{file.pdf}}`

- Az összes táblázat kivonása egy PDF-ből, a cellahatárok meghatározásához uralkodó vonalak segítségével:

`tabula --spreadsheet {{file.pdf}}`

- Az összes táblázat kivonása egy PDF-ből, a cellahatárok meghatározásához üres területet használva:

`tabula --no-spreadsheet {{file.pdf}}`
