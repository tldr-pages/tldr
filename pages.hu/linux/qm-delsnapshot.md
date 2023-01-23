# qm delsnapshot

> Virtuális gép pillanatképek törlése. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Pillanatkép törlése:

`qm delsnapshot {{vm_id}} {{snapshot_name}}`

- Pillanatfelvétel törlése egy konfigurációs fájlból (még akkor is, ha a lemezes pillanatfelvétel eltávolítása sikertelen):

`qm delsnapshot {{vm_id}} {{snapshot_name}} --force 1`
