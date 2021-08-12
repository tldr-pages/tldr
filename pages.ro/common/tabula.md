# tabula

> Extragerea tabelelor din fișiere PDF.
> Mai multe informaţii: <https://tabula.technology>

- Extrageţi toate tabelele dintr-un PDF într-un fişier CSV:

`tabula -o {{file.csv}} {{file.pdf}}`

- Extrageţi toate tabelele dintr-un PDF într-un fişier JSON:

`tabula --format JSON -o {{file.json}} {{file.pdf}}`

- Extragerea tabelelor din paginile 1, 2, 3 şi 6 ale unui PDF:

`tabula --pages {{1-3,6}} {{file.pdf}}`

- Extrageţi tabele din pagina 1 a unui PDF, ghicind ce porţiune a paginii să examinaţi:

`tabula --guess --pages {{1}} {{file.pdf}}`

- Extrageţi toate tabelele dintr-un PDF, utilizând linii de guvernare pentru a determina limitele celulei:

`tabula --spreadsheet {{file.pdf}}`

- Extrageţi toate tabelele dintr-un PDF, utilizând spaţiul necompletat pentru a determina limitele celulei:

`tabula --no-spreadsheet {{file.pdf}}`
