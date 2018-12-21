# trap

> Automatically execute commands after receiving signals by processes or the operating system.
> Can be used to perform cleanups for interruptions by the user or other actions.

- List available signals to set traps for:

`trap -l`

- List active traps for the current shell:

`trap -p`

- Set a trap to execute commands when one or more signals are detected:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- Remove active traps:

`trap - {{SIGHUP}} {{SIGINT}}`
