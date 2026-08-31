# pct destroy

> Distrugge un container.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_destroy>.

- Distrugge un container:

`pct {{[des|destroy]}} {{100}}`

- Distrugge un container anche se in esecuzione:

`pct {{[des|destroy]}} {{100}} --force`

- Elimina anche tutti i riferimenti a questo container:

`pct {{[des|destroy]}} {{100}} --purge`
