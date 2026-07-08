# lxc-attach

> Si collega a un container.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/getting-started/>.

- Si collega a un container:

`sudo lxc-attach {{container_name}}`

- Si collega a un container senza passargli le variabili d'ambiente dell'host:

`sudo lxc-attach {{container_name}} --clear-env`

- Mostra aiuto:

`lxc-attach {{[-?|--help]}}`
