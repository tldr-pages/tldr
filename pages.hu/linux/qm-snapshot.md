# qm snapshot

> Virtuális gép pillanatképek létrehozása. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Pillanatfelvétel készítése egy adott virtuális gépről:

`qm snapshot {{vm_id}} {{snapshot_name}}`

- Pillanatfelvétel létrehozása egy adott leírással:

`qm snapshot {{vm_id}} {{snapshot_name}} --description {{description}}`

- A vmstate-et is tartalmazó pillanatfelvétel létrehozása:

`qm snapshot {{vm_id}} {{snapshot_name}} --description {{description}} --vmstate 1`
