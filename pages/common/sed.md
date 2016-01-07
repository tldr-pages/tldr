# sed

> Run replacements based on regular expressions.

- Replace all occurrences of a string in a file, and print the result:

`sed 's/{{find}}/{{replace}}/g' {{filename}}`

- Replace all occurrences of a string in a file, and overwrite the file contents:

`sed -i 's/{{find}}/{{replace}}/g' {{filename}}`

- Replace all occurrences of an extended regular expression in a file:

`sed -E 's/{{regex}}/{{replace}}/g' {{filename}}`

- Replace all occurrences of multiple strings in a file:

`sed -e 's/{{find}}/{{replace}}/g' -e 's/{{find}}/{{replace}}/g' {{filename}}`
