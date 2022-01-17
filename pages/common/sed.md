# sed

> Edit text in a scriptable manner.
> Get help or version: sed --help|--version.
> More information: <https://manned.org/sed.1>.

- Execute commands:

`sed '{{s/apple/mango/g}}'`

- Execute a script:

`sed --file={{path/to/file}}`

- Execute commands with enabled extended regular expressions:

`sed --regexp-extended '{{s/(apple)/\U\1/g}}'`

- Execute a script and replace file with it's output:

`sed --in-place --file={{path/to/file}}`

- Execute commands without automatic buffer printing:

`sed --quiet '{{1p}}'`

- Replace a string with the specified replacement for all lines:

`sed 's/{{regular_expression}}/{{replacement}}/g' {{path/to/file}}`

- Print just the first line:

`sed --quiet '{{1}}p' {{path/to/file}}`
