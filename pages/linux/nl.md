# nl

> Number lines from a file or from `stdin`.
> More information: <https://manned.org/nl.1p>.

- Number non-blank lines in a file:

`nl {{path/to/file}}`

- Read from `stdin`:

`{{command}} | nl -`

- Number [a]ll [b]ody lines including blank lines or do not [n]umber [b]ody lines:

`nl --body-numbering {{a|n}} {{path/to/file}}`

- Number only the [b]ody lines that match a basic regular expression (BRE) [p]attern:

`nl --body-numbering p'FooBar[0-9]' {{path/to/file}}`

- Use a specific [i]ncrement for line numbering:

`nl --line-increment {{increment}} {{path/to/file}}`

- Specify the line numbering format to [r]ight or [l]eft justified, keeping leading [z]eros or [n]ot:

`nl --number-format {{rz|ln|rn}}`

- Specify the line numbering's width (6 by default):

`nl --number-width {{col_width}} {{path/to/file}}`

- Use a specific string to separate the line numbers from the lines (TAB by default):

`nl --number-separator {{separator}} {{path/to/file}}`
