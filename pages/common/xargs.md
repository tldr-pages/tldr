# xargs

> Execute a command with piped arguments coming from another command, a file, etc.
> The input is treated as a single block of text and split into separate pieces on spaces, tabs, newlines and end-of-file.
> More information: <https://manned.org/man/freebsd-13.0/xargs.1>.

- Execute a specific command with arguments read from the standard input:

`{{cat path/to/file}} | xargs {{command}}`

- Execute a command with a specific argument [d]elimiter:

`{{cat path/to/file}} | xargs -d '{{,}}' {{command}}`

- Execute a command with a specific [E]nd of file string:

`{{cat path/to/file}} | xargs -E '{{EOF}}' {{command}}`

- Execute a command with a specific argument count until all are consumed:

`{{cat path/to/file}} | xargs -n {{1..infinity}} {{command}}`

- Execute a command with a specific argument replacement str[I]ng:

`{{cat path/to/file}} | xargs -I '{{%}}' {{command}} {{%}}`

- Set a specific limit for [P]arallel processes (`0` disables this limit):

`{{cat path/to/file}} | xargs -P '{{0..infinity}}' {{command}}`

- Execute a command with a `\0` argument delimiter:

`{{find . -name '*.sh' -print0}} | xargs -0 {{command}}`
