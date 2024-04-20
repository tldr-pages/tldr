# dockerd

> A persistent process to start and manage Docker containers.
> More information: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- Run Docker daemon:

`dockerd`

- Run Docker daemon and configure it to listen to specific sockets (UNIX and TCP):

`dockerd --host unix://{{path/to/tmp.sock}} --host tcp://{{ip}}`

- Run with specific daemon PID file:

`dockerd --pidfile {{path/to/pid_file}}`

- Run in debug mode:

`dockerd --debug`

- Run and set a specific log level:

`dockerd --log-level {{debug|info|warn|error|fatal}}`
