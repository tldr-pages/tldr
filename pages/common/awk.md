# awk

> A versatile programming language for working on files.
> Get help or version: awk --help|--version.
> More information: <https://manned.org/awk.1>.

- Execute commands:

`awk '{ print gensub("apple", "mango", "g") }'`

- Execute a script:

`awk --file {{path/to/file}}`

- Check a script for syntax errors:

`awk --lint --file {{path/to/file}}`

- Execute commands with the specified field separator:

`awk --field-separator="{{,}}" '{ print $1 }'`

- Replace a string with the specified replacement for all lines:

`awk '{ print gensub("{{regular_expression}}", "{{replacement}}", "g") }'`

- Print the specified field of each line:

`awk '{ print ${{1}} }'`

- Print the specified field range of each line:

`awk '{ for (i={{1}}; i <= {{10}}; i++) print $i }'`
