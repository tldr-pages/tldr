# qm migrate

> Virtuális gép áttelepítése. Új áttelepítési feladat létrehozására szolgál. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Egy adott virtuális gép áttelepítése:

`qm migrate {{vm_id}} {{target}}`

- Az aktuális I/O-sávszélesség-korlátozás felülírása 10 KiB/s sebességgel:

`qm migrate {{vm_id}} {{target}} --bwlimit 10`

- Virtuális gépek migrációjának engedélyezése helyi eszközök használatával (csak root):

`qm migrate {{vm_id}} {{target}} --force true`

- Online/live migráció használata, ha egy virtuális gép fut:

`qm migrate {{vm_id}} {{target}} --online true`

- Élő tároló migráció engedélyezése helyi lemezek esetén:

`qm migrate {{vm_id}} {{target}} --with-local-disks true`
