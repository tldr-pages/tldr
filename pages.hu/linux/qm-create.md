# qm create

> Virtuális gép létrehozása vagy visszaállítása a QEMU/KVM Virtual Machine Managerben. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Virtuális gép létrehozása:

`qm create {{100}}`

- A gép automatikus indítása a létrehozás után:

`qm create {{100}} --start 1`

- Adja meg a gépen lévő operációs rendszer típusát:

`qm create {{100}} --ostype {{win10}}`

- Meglévő gép cseréje (archiválást igényel):

`qm create {{100}} --archive {{path/to/backup_file.tar}} --force 1`

- Olyan szkript megadása, amely a virtuális gép állapotától függően automatikusan végrehajtódik:

`qm create {{100}} --hookscript {{path/to/script.pl}}`
