# batch

> Execute commands at a later time when the system load levels permit.
> \*Make sure the atd (or atrun) is running.

- Execute a command from standard input:

`echo "{{./make_db_backup.sh}}" | batch`

- Execute a commands from a file:

`batch -f {{some_commands_file}}`

- Or just enter batch write commands on separate lines and press CTRL+D:

`batch`
