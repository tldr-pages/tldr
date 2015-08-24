# sed

> Run replacements based on regular expressions

- replace the first occurrence of a string in a file, and print the result

`sed 's/{{find}}/{{replace}}/' {{filename}}`

- replace all occurrences of a string in a file, overwriting the file (i.e. in-place)

`sed -i 's/{{find}}/{{replace}}/g' {{filename}}`

- replace all occurrences of an extended regular expression in a file

`sed -r 's/{{regex}}/{{replace}}/g' {{filename}}`

- apply multiple find-replace expressions to a file

`sed -e 's/{{find}}/{{replace}}/' -e 's/{{find}}/{{replace}}/' {{filename}}`


