# tabula

> Extract tables from PDF files.

- Extract all tables from a PDF to a CSV file:

`tabula {{file.pdf}} -o {{file.csv}}`

- Extract tables from pages 1, 2, 3, and 6 of a PDF:

`tabula --pages {{1-3,6}} {{file.pdf}}`

- Extract tables from page 1 of a PDF, guessing which portion of the page to examine:

`tabula {{file.pdf}} --guess --pages {{1}}`

- Extract all tables from a PDF, using ruling lines to determine cell boundaries:

`tabula {{file.pdf}} --spreadsheet`

- Extract all tables from a PDF, using blank space to determine cell boundaries:

`tabula {{file.pdf}} --no-spreadsheet`
