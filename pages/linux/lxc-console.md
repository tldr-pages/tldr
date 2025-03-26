# lxc-console

> Attach to a container.
> More information: <https://linuxcontainers.org/lxc/manpages//man1/lxc-console.1.html>.

- Start a console in a container:

`agetty {{[-L|--local-line]}} {{38400}} tty1`

- Connect to an lxc console:

`sudo lxc-console {{container_name}}`

- Exit `lxc-console`:

`<Ctrl a><q>`

- Display help:

`lxc-console {{[-?|--help]}}`
