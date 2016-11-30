# nl

> A utility for numbering lines, either from a file, or from standard input.

- Number lines in a file:

`nl {{source_file}}`

- Number lines where there is printable text only:

`nl -t {{source_file}}`

- Number lines that match a regular expression (Starting with a Capital 
A is Exampled):

`nl -b p^A {{source_file}}`

- Can be useful as an alternative to grep {{source_file}} -n 
{{search_term}}:

`nl ./file | grep match` 

Which outputs `{{line_number}} {{search_term}}`

