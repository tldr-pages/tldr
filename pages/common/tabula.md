# tabula

> Extract tables from PDF files.
> More information: <https://github.com/tabulapdf/tabula-java#commandline-usage-examples>.

- Extract all tables from a PDF to a CSV file:

`tabula {{[-o|--outfile]}} {{file.csv}} {{file.pdf}}`

- Extract all tables from a PDF to a JSON file:

`tabula {{[-f|--format]}} JSON {{[-o|--outfile]}} {{file.json}} {{file.pdf}}`

- Extract tables from pages 1, 2, 3, and 6 of a PDF:

`tabula {{[-p|--pages]}} 1-3,6 {{file.pdf}}`

- Extract tables from page 1 of a PDF, guessing which portion of the page to examine:

`tabula {{[-g|--guess]}} {{[-p|--pages]}} 1 {{file.pdf}}`

- Extract all tables from a PDF, using ruling lines to determine cell boundaries:

`tabula {{[-r|--spreadsheet]}} {{file.pdf}}`

- Extract all tables from a PDF, using blank space to determine cell boundaries:

`tabula {{[-n|--no-spreadsheet]}} {{file.pdf}}`
