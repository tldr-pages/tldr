# qm config

> A virtuális gép konfigurációjának megjelenítése a függőben lévő konfigurációs módosítások alkalmazásával. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- A virtuális gép konfigurációjának megjelenítése:

`qm config {{vm_id}}`

- A virtuális gép függőben lévő értékei helyett az aktuális konfigurációs értékek megjelenítése:

`qm config --current {{true}} {{vm_id}}`

- A konfigurációs értékek lekérése az adott pillanatfelvételről:

`qm config --snapshot {{snapshot_name}} {{vm_id}}`
