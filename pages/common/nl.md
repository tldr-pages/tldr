# nl

> A utility for numbering lines, either from a file, or from `stdin`.
> More information: <https://www.gnu.org/software/coreutils/nl>.

- Number non-blank lines in a file:

`nl {{path/to/file}}`

- Read from `stdin`:

`{{command}} | nl -`

- Number [a]ll lines including blank lines or do not [n]umber:

`nl -b {{a|n}} {{path/to/file}}`

- Number only the body lines that match a basic regular expression (BRE) pattern:

`nl -b p'FooBar[0-9]' {{path/to/file}}`

- Use a specific increment for line numbering:

`nl -i {{increment}} {{path/to/file}}`

- Specify the line numbering format to [r]ight or [l]eft justified, keeping leading [z]eros or [n]ot:

`nl -n {{rz|ln|rn}}`

- Specify the line numbering's width (6 by default):

`nl -w {{col_width}} {{path/to/file}}`

- Use a specific string to separe the line numbers from the lines (6 by default):

`nl -s {{separator}} {{path/to/file}}`
