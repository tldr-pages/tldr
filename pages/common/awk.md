# awk

> A versatile programming language for working on files.
> See also: `sed`, `ed`.
> More information: <https://github.com/onetrueawk/awk>.

- Execute a specific expression:

`{{command}} | awk '{{{ print gensub("apple", "mango", "g") }}}'`

- Execute a specific script:

`{{command}} | awk --file {{path/to/script.awk}}`

- Check a specific script for syntax errors:

`awk --lint --file {{path/to/script.awk}}`

- Execute a expression with a specific field separator:

`{{command}} | awk --field-separator="{{,}}" '{{{ print $1 }}}'`

- Replace a string with a specific replacement for all lines (`gensub` function):

`{{command}} | awk '{ print gensub("{{regular_expression}}", "{{replacement}}", "g") }'`

- Print a specific field of each line (`print` statement):

`{{command}} | awk '{ print ${{1}} }'`

- Print a specific field range of each line (`for` loop):

`{{command}} | awk '{ for (i = {{1}}; i <= {{10}}; i++) print $i }'`
