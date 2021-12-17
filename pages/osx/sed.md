# sed

> Edit text in a scriptable manner.
> More information: <https://manned.org/sed.1>.

- Execute an expression:

`sed "{{expression}}"`

- Execute a script:

`sed --file={{path/to/file}}`

- Execute an expression with enabled extended regular expressions:

`sed --regexp-extended "{{expression}}"`

- Execute a script and replace file with it's output:

`sed --in-place --file={{path/to/file}}`

- Execute an expression without automatic buffer printing:

`sed --quiet "{{expression}}"`

- Replace a string with the specified replacement for all lines:

`sed "s/{{regular_expression}}/{{replacement}}/g" {{path/to/file}}`

- Print the version:

`sed --version`
