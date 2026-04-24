# tload

> Show system load average using ASCII art.
> See also: `uptime`, `w`, `top`, `ps`.
> More information: <https://manned.org/tload>.

- Run tload:

`tload`

- Display a graph with a specific vertical scale (e.g. 10 for a 1:1 scale):

`tload {{[-s|--scale]}} {{value}}`

- Change the refresh rate for the graph:

`tload {{[-d|--delay]}} {{seconds}}`

- Display a graph for a specific terminal:

`tload {{/dev/tty1}}`
