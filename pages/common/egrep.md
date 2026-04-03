# egrep

> Find patterns in files using extended `regex`es.
> Note: This command is an alias of `grep --extended-regexp`.
> More information: <https://manned.org/egrep>.

- Search for one or more repeated characters:

`egrep '{{a}}+' {{path/to/file}}`

- Search for zero or one occurrences of a character (optional match):

`egrep '{{a}}?' {{path/to/file}}`

- Search for 10 repetitions of a character:

`egrep '{{a}}{10}' {{path/to/file}}`

- Search for 3 to 7 repetions of a character:

`egrep '{{a}}{3,7}' {{path/to/file}}`

- Search for one of the listed options:

`egrep '{{cat}}|{{dog}}|{{mouse}}' {{path/to/file}}`

- Search for one of the listed options inside a larger pattern:

`egrep 'c({{a|o|u}})p' {{path/to/file}}`

- Search using standard character classes (more info: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{path/to/file}}`
