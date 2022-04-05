# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/sed.1>.

- Execute the specified expression:

`{{command}} | sed '{{s/apple/mango/g}}'`

- Execute the specified script:

`{{command}} | sed -f {{path/to/script.sed}}`

- Execute the specified expression with enabled extended regular expressions:

`{{command}} | sed -E '{{s/(apple)/\U\1/g}}'`

- Execute the specified expression without automatic buffer printing (print just the first line (`[p]rint` command)):

`{{command}} | sed -n '{{1p}}'`

- Execute the specified expression and replace the file with it's output:

`sed -i '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace the string with the specified replacement for all lines (`[s]ubstitute` command):

`{{command}} | sed 's/{{regular_expression}}/{{replacement}}/g'`
