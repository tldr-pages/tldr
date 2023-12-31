# trap

> Execute a command upon an event.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#trap>.

- List the commands and the names of the expected events:

`trap`

- Execute a command when a signal is received:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- Remove commands:

`trap - {{SIGHUP}} {{SIGINT}}`
