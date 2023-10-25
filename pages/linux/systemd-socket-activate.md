# systemd-socket-activate

> Socket activation for systemd services.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-socket-activate.html>.

- Activate a service when a specific socket is connected:

`systemd-socket-activate {{path/to/socket.service}}`

- Activate multiple sockets for a service:

`systemd-socket-activate {{path/to/socket1.service}} {{path/to/socket2.service}}`

- Pass environment variables to the service being activated:

`{{SYSTEMD_SOCKET_ACTIVATION=1}} systemd-socket-activate {{path/to/socket.service}}`

- Activate a service along with a notification socket:

`systemd-socket-activate {{path/to/socket.socket}} {{path/to/service.service}}`

- Activate a service with a specified port:

`systemd-socket-activate {{path/to/socket.service}} -l {{8080}}`
