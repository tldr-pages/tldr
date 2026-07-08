# lxc-console

> Si collega a un container.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/manpages//man1/lxc-console.1.html>.

- Avvia una console in un container:

`agetty {{[-L|--local-line]}} {{38400}} tty1`

- Si connette a una console lxc:

`sudo lxc-console {{container_name}}`

- Esce da `lxc-console`:

`<Ctrl a><q>`

- Mostra aiuto:

`lxc-console {{[-?|--help]}}`
