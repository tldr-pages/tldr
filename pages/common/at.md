# at

> Execute commands once at a later time.
> Results will be sent to the users mail.
> More information: <https://manned.org/at>.

- Start the `atd` daemon:

`systemctl start atd`

- Create commands interactively and execute them in 5 minutes (press `<Ctrl> + D` when done):

`at now + 5 minutes`

- Create commands interactively and execute them at a specific time:

`at {{hh:mm}}`

- Execute a command from `stdin` at 10:00 AM today:

`echo "{{command}}" | at 1000`

- Execute commands from a given file next Tuesday:

`at -f {{path/to/file}} 9:30 PM Tue`
