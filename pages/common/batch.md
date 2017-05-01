# batch

> Execute commands at a later time when the system load levels permit.
> Make sure the atd (or atrun) is running.

- Execute a command from standard input:

`echo "{{./make_db_backup.sh}}" | batch`

- Execute commands from a given file:

`batch -f {{path/to/file}}`

- Execute commands from standard input (press CTRL+D when finished):

`batch`
