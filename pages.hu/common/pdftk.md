# pdftk

> PDF-eszközkészlet. További információ: <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>.

- Vegye ki az 1-3., 5. és 6-10. oldalt egy PDF-fájlból, és mentse el egy másik PDF-fájlként:

`pdftk {{input.pdf}} cat {{1-3 5 6-10}} output {{output.pdf}}`

- PDF-fájlok listájának egyesítése (összekapcsolása) és az eredmény mentése egy másik PDF-fájlként:

`pdftk {{file1.pdf file2.pdf ...}} cat output {{output.pdf}}`

- Egy PDF-fájl minden egyes oldalának különálló fájlba történő szétválasztása, adott fájlnév kimeneti mintával:

`pdftk {{input.pdf}} burst output {{out_%d.pdf}}`

- Az összes oldal elforgatása 180 fokkal az óramutató járásával megegyező irányban:

`pdftk {{input.pdf}} cat {{1-endsouth}} output {{output.pdf}}`

- A harmadik oldal elforgatása 90 fokkal az óramutató járásával megegyező irányban, a többi változatlanul hagyása:

`pdftk {{input.pdf}} cat {{1-2 3east 4-end}} output {{output.pdf}}`
