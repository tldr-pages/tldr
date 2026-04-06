# tload

> Show system load average using ASCII art.
> See also: `uptime`, `w`, `top`, `ps`.
> More information: <https://manned.org/tload>.

- Run tload:

`tload`

- Change the graph [s]cale (recommended value=10 to maintain a 1:1 scale based on the system load percentage):

`tload {{[-s|--scale]}} {{value}}`

- Change the refresh rate (seconds) for the graph:

`tload {{[-d|--delay]}} {{value}}`

- View a server's load using tload:

`ssh {{username@host}} -t tload {{[-s|--scale]}} 10 {{[-d|--delay]}} 1`
