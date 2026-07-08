# lxc-create

> Crea container Linux.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/getting-started/>.

- Crea un container interattivamente in `/var/lib/lxc/`:

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- Crea un container in una directory di destinazione:

`sudo lxc-create {{[-P|--lxcpath]}} /{{path/to/directory}}/ {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- Crea un container passando opzioni a un template:

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download -- {{[-d|--dist]}} {{distro_name}} {{[-r|--release]}} {{release_version}} {{[-a|--arch]}} {{architecture}}`

- Mostra aiuto:

`lxc-create {{[-?|--help]}}`
