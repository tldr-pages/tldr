# trap

> Execute a command upon an event.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-trap>.

- List the available event names (e.g. `SIGWINCH`):

`trap -l`

- List the commands and the names of the expected events:

`trap`

- Execute a command when a signal is received:

`trap 'echo "Caught signal {{SIGHUP}}"' {{[1|SIGHUP]}}`

- Remove commands:

`trap - {{SIGHUP SIGINT ...}}`

- Ignore a signal:

`trap '' {{[2|SIGINT]}}`

- Execute a command when the current shell exits:

`trap '{{echo "Initiating cleanup"}}' EXIT`

- Execute a command before every single command:

`trap '{{echo "Debug output"}}' DEBUG`

- Display help:

`help trap`
