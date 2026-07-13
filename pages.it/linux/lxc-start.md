# lxc-start

> Avvia un container.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/getting-started/>.

- Avvia il servizio lxc:

`systemctl start lxc-net`

- Avvia un container:

`sudo lxc-start {{nome_container}}`

- Avvia un container in primo piano:

`sudo lxc-start {{nome_container}} {{[-F|--foreground]}}`

- Esce da un container in primo piano (esegui questo in un terminale separato):

`sudo lxc-stop {{nome_container}}`

- Scrivi log di debug in un file:

`sudo lxc-start {{nome_container}} {{[-l|--logpriority]}} DEBUG {{[-o|--logfile]}} {{percorso/al/logfile}}`

- Mostra aiuto:

`lxc-start {{[-?|--help]}}`
