# lxc-create

> Crea container Linux.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/getting-started/>.

- Crea un container interattivamente in `/var/lib/lxc/`:

`sudo lxc-create {{[-n|--name]}} {{nome_container}} {{[-t|--template]}} download`

- Crea un container in una directory di destinazione:

`sudo lxc-create {{[-P|--lxcpath]}} /{{percorso/alla/cartella}}/ {{[-n|--name]}} {{nome_container}} {{[-t|--template]}} download`

- Crea un container passando opzioni a un template:

`sudo lxc-create {{[-n|--name]}} {{nome_container}} {{[-t|--template]}} download -- {{[-d|--dist]}} {{nome_distro}} {{[-r|--release]}} {{versione_release}} {{[-a|--arch]}} {{architettura}}`

- Mostra aiuto:

`lxc-create {{[-?|--help]}}`
