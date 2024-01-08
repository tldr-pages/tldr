# trap

> Execute a command upon an event.
> More information: <https://manned.org/trap.1posix>.

- List the commands and the names of the expected events:

`trap`

- Execute a command when a signal is received:

`trap 'echo "Caught signal {{SIGHUP}}"' {{HUP}}`

- Remove commands:

`trap - {{HUP}} {{INT}}`
