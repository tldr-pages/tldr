# at

> execute commands once at a later time
> make sure the atd (or atrun) is running

- Execute commands from standard input in 5 minutes
  (press CTRL+D after entering commands)
`at now + 5 min`

- Execute a command from standard input at 10:00 AM today :

`echo "./make_db_backup.sh" | at 1000`

- Execute a command from some_file at 9:30 PM Tuesday:

`at -f some_file 9:30 PM Tue`
