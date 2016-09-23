# fold

> Wraps each line in an input file to fit a specified width

- Wrap each line to default width (80)

`fold {{file}}`

- Wrap each line to width '30'

`fold -w30 {{file}}`

- Wrap each line to width '5' and break at spaces (If word length > 5, it is wrapped, else only one word is kept per line )

`fold -w5 -s {{file}}`
