# qm resume

> Reanuda una máquina virtual.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_resume>.

- Reanuda una máquina virtual dada:

`qm resume {{id_mv}}`

- Recupera una máquina virtual específica omitiendo cualquier bloqueo (requiere root):

`sudo qm resume {{id_mv}} --skiplock true`
