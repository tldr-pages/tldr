# nl

> Number lines from a file or from `stdin`.
> More information: <https://manned.org/nl>.

- Number non-blank lines in a file:

`nl {{path/to/file}}`

- Read from `stdin`:

`{{command}} | nl`

- Number [a]ll body lines including blank lines or do [n]ot number body lines:

`nl {{[-b|--body-numbering]}} {{a|n}} {{path/to/file}}`

- Number only the body lines that match a basic regular expression (BRE) [p]attern:

`nl {{[-b|--body-numbering]}} p'FooBar[0-9]' {{path/to/file}}`

- Use a specific increment for line numbering:

`nl {{[-i|--line-increment]}} {{increment}} {{path/to/file}}`

- Specify the line numbering format to [r]ight or [l]eft justified, keeping leading [z]eros or [n]ot:

`nl {{[-n|--number-format]}} {{rz|ln|rn}}`

- Specify the line numbering's width (6 by default):

`nl {{[-w|--number-width]}} {{col_width}} {{path/to/file}}`

- Use a specific string to separate the line numbers from the lines (TAB by default):

`nl {{[-s|--number-separator]}} {{separator}} {{path/to/file}}`
