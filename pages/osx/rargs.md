# rargs

> Execute a command for each line of standard input.
> Like `xargs`, but with pattern matching support.
> More information: <https://github.com/lotabout/rargs>.

- Execute a command for every line of input, just like `xargs` (`{0}` indicates where to substitute in the text):

`{{command}} | rargs {{command}} {0}`

- Do a dry run, which prints the commands that would be run instead of executing them:

`{{command}} | rargs -e {{command}} {0}`

- Remove the `.bak` extension from every file in a list:

`{{command}} | rargs -p '(.*).bak mv {0} {1}`

- Execute commands in parallel:

`{{command}} | rargs -w {{max-procs}}`

- Consider each line of input to be separated by a NUL character (`\0`) instead of a newline (`\n`):

`{{command}} | rargs -0 {{command}} {0}`
