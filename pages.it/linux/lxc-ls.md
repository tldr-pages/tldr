# lxc-ls

> Elenca i container Linux.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/manpages/man1/lxc-ls.1.html>.

- Elenca tutti i container:

`sudo lxc-ls`

- Elenca i container attivi (inclusi congelati e in esecuzione):

`sudo lxc-ls --active`

- Elenca solo i container congelati:

`sudo lxc-ls --frozen`

- Elenca solo i container fermati:

`sudo lxc-ls --stopped`

- Elenca i container in un output elaborato a colonne:

`sudo lxc-ls {{[-f|--fancy]}}`

- Mostra aiuto:

`lxc-ls {{[-?|--help]}}`
