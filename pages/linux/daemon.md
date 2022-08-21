# daemon

> Run processes into daemons.
> More information: <https://manned.org/man/daemon.1>.

- Run a command as a daemon:

`daemon --name="{{name}}" {{command}}`

- Run a command as daemon which will restart if the command crashes:

`daemon --name="{{name}}" --respawn {{command}}`

- Run a command as a daemon, writing logs to a specific file:

`daemon --name="{{name}}" --errlog={{path/to/logfile}} {{command}}`

- Stop a daemon:

`daemon --name="{{name}}" --stop`

- List daemons:

`daemon --list`
