# awk

> A versatile programming language for working on files.
> More information: <https://manned.org/awk.1>.

- Execute an expression:

`awk "{{expression}}"`

- Execute a script:

`awk --file {{path/to/file}}`

- Check a script for syntax errors:

`awk --lint --file {{path/to/file}}`

- Execute an expression with the specified field separator:

`awk --field-separator="{{,}}" "{{expression}}"`

- Execute an expression with the specified variables:

`awk --assign "{{variable}}={{value}}" "{{expression}}"`

- Print the specified field of each line:

`awk "{ print \$1 }"`

- Print the specified field range of each line:

`awk "{ for (i=1; i <= 10; i++) print \$i }"`

- Print the version:

`awk --version`
