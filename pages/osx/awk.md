# awk

> A versatile programming language for working on files.
> See also: `sed`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/awk.1>.

- Execute commands:

`awk '{ print gensub("apple", "mango", "g") }'`

- Execute a script:

`awk -f {{path/to/script.awk}}`

- Execute commands with the specified field separator:

`awk -F "{{,}}" '{ print $1 }'`

- Replace a string with the specified replacement for all lines:

`awk '{ print gensub("{{regular_expression}}", "{{replacement}}", "g") }'`

- Print the specified field of each line:

`awk '{ print ${{1}} }'`

- Print the specified field range of each line:

`awk '{ for (i={{1}}; i <= {{10}}; i++) print $i }'`
