# daemon

> Turns other processes into daemons.
> More information: <https://manned.org/daemon.1>.

- Run a command as a daemon:

`daemon {{[-n|--name]}} "{{name}}" {{command}}`

- Run a command as a daemon which will restart if the command crashes:

`daemon {{[-n|--name]}} "{{name}}" {{[-r|--respawn]}} {{command}}`

- Run a command as a daemon which will restart if it crashes, with two attempts every 10 seconds:

`daemon {{[-n|--name]}} "{{name}}" {{[-r|--respawn]}} {{[-A|--attempts]}} 2 {{[-L|--delay]}} 10 {{command}}`

- Run a command as a daemon, writing logs to a specific file:

`daemon {{[-n|--name]}} "{{name}}" {{[-l|--errlog]}} {{path/to/file.log}} {{command}}`

- Kill a daemon (SIGTERM):

`daemon {{[-n|--name]}} "{{name}}" --stop`

- List daemons:

`daemon --list`
