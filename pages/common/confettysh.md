# confettysh

> A fun SSH server that displays animated confetti or fireworks in the terminal.
> Built with Charmbracelet's Wish framework and Maas Lalani's confeTTY project.
> More information: <https://github.com/charmbracelet/confettysh>.

- Start a local confettysh server:

`confettysh`

- Connect to a running confettysh server on the default port:

`ssh -p 2222 localhost`

- Run the confetti animation:

`ssh -p 2222 localhost -t confetti`

- Run the fireworks animation:

`ssh -p 2222 localhost -t fireworks`

- Run the server on a custom port:

`confettysh --port {{2323}}`
