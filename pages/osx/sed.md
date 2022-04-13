# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/sed.1>.

- Execute a specific expression:

`{{command}} | sed '{{s/apple/mango/g}}'`

- Execute a specific script:

`{{command}} | sed -f {{path/to/script.sed}}`

- Execute a specific expression with enabled extended regular expressions:

`{{command}} | sed -E '{{s/(apple)/\U\1/g}}'`

- Execute a specific expression without automatic buffer printing (print just the first line (`[p]rint` command)):

`{{command}} | sed -n '{{1p}}'`

- Execute a specific expression and replace a file with it's output:

`sed -i '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace a string with a specific replacement for all lines (`[s]ubstitute` command):

`{{command}} | sed 's/{{regular_expression}}/{{replacement}}/g'`
