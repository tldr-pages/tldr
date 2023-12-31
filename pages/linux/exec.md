# exec

> Execute a command without creating a child process.
> More information: <https://linuxcommand.org/lc3_man_pages/exech.html>.

- Execute a specific command:

`exec {{command -with -flags}}`

- Execute a command with a (mostly) empty environment:

`exec -c {{command -with -flags}}`

- Execute a command as a login shell:

`exec -l {{command -with -flags}}`

- Execute a command with a different name:

`exec -a {{name}} {{command -with -flags}}`
