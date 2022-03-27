# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/sed.1>.

- Execute the specified expression:

`sed '{{s/apple/mango/g}}'`

- Execute the specified script:

`sed -f {{path/to/script.sed}}`

- Execute the specified expression with enabled extended regular expressions:

`sed -E '{{s/(apple)/\U\1/g}}'`

- Execute the specified expression without automatic buffer printing:

`sed -n '{{1p}}'`

- Execute the specified expression and replace the file with it's output:

`sed -i '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace the string with the specified replacement for all lines (`[s]ubstitute` command):

`sed 's/{{regular_expression}}/{{replacement}}/g'`

- Print just the first line (`[p]rint` command):

`sed -n '{{1}}p'`
