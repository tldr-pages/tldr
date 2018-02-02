# trap

> Automatically execute commands after receiving signals by processes or the operating system.
> Can be used to perform cleanups for interruptions by the user or other causes.

- List available signals to set traps for:

`trap -l`

- List active traps for the current shell:

`trap -p`

- Set a trap to execute commands when one or more signals are detected:

`trap '{{shell_commands}}' {{signal_names}}`

- Remove active traps:

`trap - {{signal_names}}`

- Set a trap to delete a file after the user has interrupted a download:

`trap 'rm -i master.zip' SIGINT ERR`
