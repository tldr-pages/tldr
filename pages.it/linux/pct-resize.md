# pct resize

> Ridimensiona l'archiviazione del container.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_resize>.

- Ridimensiona il container a 20GB:

`pct {{[resi|resize]}} {{100}} rootfs 20G`

- Aggiungi 10GB all'archiviazione del container:

`pct {{[resi|resize]}} {{100}} rootfs +10G`

- Ridimensiona un volume montato:

`pct {{[resi|resize]}} {{100}} mp{{0}} {{+10G}}`
