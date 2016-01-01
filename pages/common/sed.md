# sed

> Run replacements based on regular expressions

- replace all occurrences of a string in a file, and print the result

`sed 's/{{find}}/{{replace}}/g' {{filename}}`

- replace all occurrences of a string in a file, and overwrite the file contents

`sed -i 's/{{find}}/{{replace}}/g' {{filename}}`

- replace all occurrences of an extended regular expression in a file

`sed -E 's/{{regex}}/{{replace}}/g' {{filename}}`

- replace all occurrences of multiple strings in a file

`sed -e 's/{{find}}/{{replace}}/g' -e 's/{{find}}/{{replace}}/g' {{filename}}`
