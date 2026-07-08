# lxc-start

> Avvia un container.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/getting-started/>.

- Avvia il servizio lxc:

`systemctl start lxc-net`

- Avvia un container:

`sudo lxc-start {{container_name}}`

- Avvia un container in primo piano:

`sudo lxc-start {{container_name}} {{[-F|--foreground]}}`

- Esce da un container in primo piano (esegui questo in un terminale separato):

`sudo lxc-stop {{container_name}}`

- Scrivi log di debug in un file:

`sudo lxc-start {{container_name}} {{[-l|--logpriority]}} DEBUG {{[-o|--logfile]}} {{path/to/logfile}}`

- Mostra aiuto:

`lxc-start {{[-?|--help]}}`
