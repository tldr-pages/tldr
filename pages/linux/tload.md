# tload

> Show system load average using ASCII art.
> See also: `uptime`, `w`, `top`, `ps`.
> More information: <https://manned.org/tload>.

- Run:

`tload`

- Change the graph scale (recommended value=10 to maintain a 1:1 scale based on the system load percentage):

`tload -s {value}`

- Change the refresh rate (seconds) for the graph:

`tload -d {value}`

- View a server's load using tload:

`ssh user@ip_server -t tload -s 10 -d 1`

