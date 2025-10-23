# confettysh

> Display animated confetti and fireworks over SSH.
> See also: `ssh`.
> More information: <https://github.com/charmbracelet/confettysh>.

- Start a local `confettysh` server:

`confettysh`

- Run the server on a custom port:

`confettysh {{[-p|--port]}} {{2323}}`

- Connect to the local server and show fireworks:

`ssh {{[-p|--port]}} {{2222}} localhost -t fireworks`
