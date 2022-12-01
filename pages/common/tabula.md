# tabula

> Extract tables from PDF files.
> More information: <https://tabula.technology>.

- Extract all tables from a PDF to a CSV file:

`tabula -o {{path/to/file.csv}} {{path/to/file.pdf}}`

- Extract all tables from a PDF to a JSON file:

`tabula --format JSON -o {{path/to/file.json}} {{path/to/file.pdf}}`

- Extract tables from pages 1, 2, 3, and 6 of a PDF:

`tabula --pages {{1-3,6}} {{path/to/file.pdf}}`

- Extract tables from page 1 of a PDF, guessing which portion of the page to examine:

`tabula --guess --pages {{1}} {{path/to/file.pdf}}`

- Extract all tables from a PDF, using ruling lines to determine cell boundaries:

`tabula --spreadsheet {{path/to/file.pdf}}`

- Extract all tables from a PDF, using blank space to determine cell boundaries:

`tabula --no-spreadsheet {{path/to/file.pdf}}`
