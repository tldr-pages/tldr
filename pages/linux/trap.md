# trap

> Execute a command upon an event.
> More information: <https://manned.org/trap>.

- List available signals to set traps for:

`trap -l`

- List active traps for the current shell:

`trap -p`

- Set a trap to execute commands when one or more signals are detected:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- Remove active traps:

`trap - {{SIGHUP}} {{SIGINT}}`
