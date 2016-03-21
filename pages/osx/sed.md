# sed

> Run replacements based on regular expressions.

- Replace the first occurrence of a string in a file, and print the result:

`sed 's/{{find}}/{{replace}}/' {{filename}}`

- Replace only on lines matching the line pattern:

`sed '/{{line_pattern}}/s/{{find}}/{{replace}}/'`

- Replace all occurrences of a string in a file, overwriting the file (i.e. in-place):

`sed -i '' 's/{{find}}/{{replace}}/g' {{filename}}`

- Replace all occurrences of an extended regular expression in a file:

`sed -E 's/{{regex}}/{{replace}}/g' {{filename}}`

- Apply multiple find-replace expressions to a file:

`sed -e 's/{{find}}/{{replace}}/' -e 's/{{find}}/{{replace}}/' {{filename}}`
