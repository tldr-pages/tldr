# qm showcmd

> A VM indításához használt parancssor megjelenítése (debug info). További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Egy adott virtuális gép parancssorának megjelenítése:

`qm showcmd {{vm_id}}`

- Az emberi olvashatóság javítása érdekében minden egyes opciót új sorba helyezzen:

`qm showcmd --pretty {{true}} {{vm_id}}`

- Konfigurációs értékek lekérése egy adott pillanatfelvételből:

`qm showcmd --snapshot {{string}} {{vm_id}}`
