# nl

> A utility for numbering lines, either from a file, or from standard input.

- Number lines in a file:

`nl {{file}}`

- Number only the lines with printable text:

`nl -t {{file}}`

- Number only the body lines that match a basic regular expression (BRE) pattern:

`nl -b p'FooBar[0-9]' {{file}}`
