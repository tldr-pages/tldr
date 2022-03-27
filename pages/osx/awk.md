# awk

> A versatile programming language for working on files.
> See also: `sed`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/awk.1>.

- Execute the specified expression:

`awk '{{{ print gensub("apple", "mango", "g") }}}'`

- Execute the specified script:

`awk -f {{path/to/script.awk}}`

- Execute the expression with the specified field separator:

`awk -F "{{,}}" '{{{ print $1 }}}'`

- Replace the string with the specified replacement for all lines (`gensub` function):

`awk '{ print gensub("{{regular_expression}}", "{{replacement}}", "g") }'`

- Print the specified field of each line (`print` statement):

`awk '{ print ${{1}} }'`

- Print the specified field range of each line (`for` loop):

`awk '{ for (i = {{1}}; i <= {{10}}; i++) print $i }'`
