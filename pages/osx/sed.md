# sed

> Edit text in a scriptable manner.
> There are no options to get help or version.
> More information: <https://manned.org/man/freebsd-13.0/sed.1>.

- Execute commands:

`sed '{{s/apple/mango/g}}'`

- Execute a script:

`sed -f {{path/to/file}}`

- Execute commands with enabled [E]xtended regular expressions:

`sed -E '{{s/apple/mango/g}}'`

- Execute a script and replace file with it's output:

`sed -i -f {{path/to/file}}`

- Execute commands without automatic buffer printing:

`sed -n '{{1p}}'`

- Replace a string with the specified replacement for all lines:

`sed 's/{{regular_expression}}/{{replacement}}/g' {{path/to/file}}`

- Print just the first line:

`sed -n '{{1}}p' {{path/to/file}}`
