# xargs

> Execute a command with piped arguments coming from another command, a file, etc.
> The input is treated as a single block of text and split into separate pieces on spaces, tabs, newlines and end-of-file.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- Execute a specific command with arguments read from the standard input:

`{{cat path/to/file}} | xargs {{command}}`

- Execute a command with a specific argument delimiter:

`{{cat path/to/file}} | xargs --delimiter='{{,}}' {{command}}`

- Execute a command with a specific end of file string:

`{{cat path/to/file}} | xargs --eof='{{EOF}}' {{command}}`

- Execute a command with a specific argument count until all are consumed:

`{{cat path/to/file}} | xargs --max-args={{1..infinity}} {{command}}`

- Execute a command with a specific argument replacement string:

`{{cat path/to/file}} | xargs --replace='{{%}}' {{command}} {{%}}`

- Set a specific limit for parallel processes (`0` disables this limit):

`{{cat path/to/file}} | xargs --max-procs='{{0..infinity}}' {{command}}`

- Execute a command with a `\0` argument delimiter:

`{{find . -name '*.sh' -print0}} | xargs --null {{command}}`
