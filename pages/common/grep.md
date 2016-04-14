# grep

> Matches patterns in input text.
> Supports simple patterns and regular expressions.

- Search for an exact string:

`grep {{something}} {{file_path}}`

- Search without case-sensitivity:

`grep -i {{something}} {{file_path}}`

- Search recursively in current directory for an exact string:

`grep -r {{something}} .`

- Use a regex:

`grep -e {{^regex$}} {{file_path}}`

- See 3 lines of context:

`grep -C 3 {{something}} {{file_path}}`

- Print the count of matches instead of the matching text:

`grep -c {{something}} {{file_path}}`

- Print line number for each match:

`grep -n {{something}} {{file_path}}`

- Use the standard input instead of a file:

`cat {{file_path}} | grep {{something}}`

- Invert match for excluding specific strings:

`grep -v {{something}}`
