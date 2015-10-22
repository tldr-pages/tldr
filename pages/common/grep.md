# grep

> Matches patterns in input text
> Supports simple patterns and regular expressions

- search for an exact string

`grep {{something}} {{file_path}}`

- search recursively in current directory for an exact string

`grep -r {{something}} .`

- use a regex

`grep -e {{^regex$}} {{file_path}}`

- see 3 lines of context

`grep -C 3 {{something}} {{file_path}}`

- print the count of matches instead of the matching text

`grep -c {{something}} {{file_path}}`

- use the standard input instead of a file

`cat {{file_path}} | grep {{something}}`

- invert match for excluding specific strings

`grep -v {{something}}`
