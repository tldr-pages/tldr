# pct create

> Crea container LXC in Proxmox.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_create>.

- Crea un container da un template con dimensione 4GB, assegnagli 512MiB di memoria e accesso illimitato alla CPU:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- Crea un container da un template e assegnagli un limite di memoria specifico in megabyte:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --memory {{8192}}`

- Crea un container da un template e assegnagli un hostname e una password:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --hostname {{hostname}} --password {{password}}`

- Crea un container da un template e assegnagli accesso alla rete:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --net0 name={{eth0}},bridge={{vmbr0}},ip={{dhcp|manual|10.0.0.1/24}} --features nesting=1`

- Avvia un container immediatamente dopo la creazione:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --start`
