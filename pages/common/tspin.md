# tspin

> A log file highlighter based on the `less` pager and basically behaves like any pager.
> More information: <https://github.com/bensadeh/tailspin>.

- Read from file and view in `less`:

`tspin {{path/to/application.log}}`

- Read from another command and print to stdout:

`journalctl {{[-b|--boot]}} {{[-f|--follow]}} | tspin`

- Read from file and print to `stdout`:

`tspin {{path/to/application.log}} {{[-p|--print]}}`

- Read from `stdin` and print to `stdout`:

`echo "2021-01-01 12:00:00 [INFO] This is a log message" | tspin`
