# lxc-attach

> Si collega a un container.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/getting-started/>.

- Si collega a un container:

`sudo lxc-attach {{nome_container}}`

- Si collega a un container senza passargli le variabili d'ambiente dell'host:

`sudo lxc-attach {{nome_container}} --clear-env`

- Mostra aiuto:

`lxc-attach {{[-?|--help]}}`
