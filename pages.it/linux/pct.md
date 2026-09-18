# pct

> Gestisce container LXC in Proxmox.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- Elenca tutti i container:

`pct list`

- Avvia/Ferma/Riavvia un container specifico:

`pct {{start|stop|reboot}} {{100}}`

- Accedi alla shell di un container specifico:

`pct {{[en|enter]}} {{100}}`

- Crea un container da un template con dimensione 4GB:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- Ridimensiona il disco del container a 20G:

`pct {{[resi|resize]}} {{100}} {{rootfs|mpX}} {{20G}}`

- Mostra la configurazione di un container, specificando il suo ID:

`pct {{[conf|config]}} {{100}}`

- Crea uno snapshot di un container specifico con descrizione:

`pct {{[sn|snapshot]}} {{100}} {{my-snapshot}} --description {{Descrizione dello snapshot}}`

- Distrugge un container e rimuove tutte le risorse correlate:

`pct {{[des|destroy]}} {{100}} --purge`
