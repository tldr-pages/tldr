# dockerd

> Starting docker daemon, persistent process that manages docker containers.
> More information: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- Run docker daemon and config it to listening to specific sockets:

`dockerd --host {{socket1}} --host {{socket2}}`

- Run docker daemon with specific daemon PID file:

`dockerd --pidfile {{path/to/pid_file}}`

- Run docker daemon in debug mode:

`dockerd --debug={{boolean}}`

- Run docker daemon, set it to log only specific log level or more severe events:

`dockerd --log-level={{log_level}}`
