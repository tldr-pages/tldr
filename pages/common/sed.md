# sed

> Edit text in a scriptable manner.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Replace the first occurrence of a regular expression in each line of a file, and print the result:

`sed 's/{{regular_expression}}/{{replace}}/' {{filename}}`

- Replace all occurrences of an extended regular expression in a file, and print the result:

`sed -r 's/{{regular_expression}}/{{replace}}/g' {{filename}}`

- Replace all occurrences of a string in a file, overwriting the file (i.e. in-place):

`sed -i 's/{{find}}/{{replace}}/g' {{filename}}`

- Replace only on lines matching the line pattern:

`sed '/{{line_pattern}}/s/{{find}}/{{replace}}/' {{filename}}`

- Delete lines matching the line pattern:

`sed '/{{line_pattern}}/d' {{filename}}`

- Print the first 11 lines of a file:

`sed 11q {{filename}}`

- Apply multiple find-replace expressions to a file:

`sed -e 's/{{find}}/{{replace}}/' -e 's/{{find}}/{{replace}}/' {{filename}}`

- Replace separator `/` by any other character not used in the find or replace patterns, e.g. `#`:

`sed 's#{{find}}#{{replace}}#' {{filename}}`
