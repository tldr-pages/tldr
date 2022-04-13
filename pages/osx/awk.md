# awk

> A versatile programming language for working on files.
> See also: `sed`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/awk.1>.

- Execute a specific expression:

`{{command}} | awk '{{{ print gensub("apple", "mango", "g") }}}'`

- Execute a specific script:

`{{command}} | awk -f {{path/to/script.awk}}`

- Execute a expression with a specific field separator:

`{{command}} | awk -F "{{,}}" '{{{ print $1 }}}'`

- Replace a string with a specific replacement for all lines (`gensub` function):

`{{command}} | awk '{ print gensub("{{regular_expression}}", "{{replacement}}", "g") }'`

- Print a specific field of each line (`print` statement):

`{{command}} | awk '{ print ${{1}} }'`

- Print a specific field range of each line (`for` loop):

`{{command}} | awk '{ for (i = {{1}}; i <= {{10}}; i++) print $i }'`
