# trap

> Automatically execute commands after receiving signals by processes or the operating system.
> Can be used to perform cleanups for interruptions by the user or other actions.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#trap>.

- List active traps for the current shell:

`trap`

- Set a trap to execute commands when one or more signals are detected:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- Remove active traps:

`trap - {{SIGHUP}} {{SIGINT}}`
