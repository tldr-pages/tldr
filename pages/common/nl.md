# nl

> Number lines from a file or from `stdin`.
> More information: <https://manned.org/nl.1p>.

- Number non-blank lines in a file:

`nl {{path/to/file}}`

- Read from `stdin`:

`{{command}} | nl -`

- Number [a]ll [b]ody lines including blank lines or do [n]ot number body lines:

`nl -b {{a|n}} {{path/to/file}}`

- Number only the [b]ody lines that match a basic regular expression (BRE) [p]attern:

`nl -b p'FooBar[0-9]' {{path/to/file}}`

- Use a specific [i]ncrement for line numbering:

`nl -i {{increment}} {{path/to/file}}`

- Specify the line numbering format to [r]ight or [l]eft justified, keeping leading [z]eros or [n]ot:

`nl -n {{rz|ln|rn}}`

- Specify the line numbering's [w]idth (6 by default):

`nl -w {{col_width}} {{path/to/file}}`

- Use a specific string to [s]eparate the line numbers from the lines (TAB by default):

`nl -s {{separator}} {{path/to/file}}`
