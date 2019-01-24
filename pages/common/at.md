# at

> Execute commands once at a later time.
> Service atd (or atrun) should be running for the actual executions.

- Execute commands from standard input in 5 minutes (press `Ctrl + D` when done):

`at now + 5 minutes`

- Execute a command from standard input at 10:00 AM today:

`echo "{{./make_db_backup.sh}}" | at 1000`

- Execute commands from a given file next Tuesday:

`at -f {{path/to/file}} 9:30 PM Tue`
