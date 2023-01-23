# pvecm

> Proxmox VE Cluster Manager. További információ: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- Az aktuális csomópont hozzáadása egy meglévő fürthöz:

`pvecm add {{hostname_or_ip}}`

- Egy csomópont hozzáadása a fürtkonfigurációhoz (belső használat):

`pvecm addnode {{node}}`

- Visszaadja a csomóponton elérhető fürtcsatlakozási API verzióját:

`pvecm apiver`

- Új fürtkonfiguráció létrehozása:

`pvecm create {{clustername}}`

- Egy csomópont eltávolítása a fürtkonfigurációból:

`pvecm delnode {{node}}`

- A fürtcsomópontok helyi nézetének megjelenítése:

`pvecm nodes`

- A fürt állapotának helyi nézetének megjelenítése:

`pvecm status`
