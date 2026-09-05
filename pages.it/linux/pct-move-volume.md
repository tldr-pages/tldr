# pct move-volume

> Sposta un volume in un archivio differente o in un container differente.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_move-volume>.

- Sposta il filesystem root di un container in un archivio differente:

`pct {{[mov|move-volume]}} {{100}} rootfs {{id_archivio}}`

- Elimina l'associazione del filesystem al vecchio volume una volta completato lo spostamento:

`pct {{[mov|move-volume]}} {{100}} rootfs {{id_archivio}} --delete`
