# trap

> Execute a command upon an event.
> More information: <https://manned.org/trap>.

- List the available event names (e.g. `SIGWINCH`):

`trap -l`

- List the commands and the names of the expected events:

`trap -p`

- Execute a command when a signal is received:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- Remove commands:

`trap - {{SIGHUP}} {{SIGINT}}`
