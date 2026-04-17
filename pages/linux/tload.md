# tload

> Show system load average using ASCII art.
> See also: `uptime`, `w`, `top`, `ps`.
> More information: <https://manned.org/tload>.

- Run tload:

`tload`

- Change the graph scale (recommended value=10 to maintain a 1:1 scale based on the system load percentage):

`tload {{[-s|--scale]}} {{value}}`

- Change the refresh rate for the graph:

`tload {{[-d|--delay]}} {{seconds}}`

- Display a graph for a specific terminal:

`tload {{/dev/tty1}}`
