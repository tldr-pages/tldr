# qm guest exec

> Egy adott parancs végrehajtása egy vendégügynökön keresztül. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Egy adott parancs végrehajtása egy vendégügynökön keresztül:

`qm guest exec {{vm_id}} {{command}} {{arg1 arg2 ...}}`

- Egy adott parancs aszinkron végrehajtása vendégügynökön keresztül:

`qm guest exec {{vm_id}} {{arg1 arg2 ...}} --synchronous 0`

- Egy adott parancs végrehajtása vendégügynökön keresztül, 10 másodperces időkorlátozással:

`qm guest exec {{vm_id}} {{arg1 arg2 ...}} --timeout {{10}}`

- Egy adott parancs végrehajtása egy vendégügynökön keresztül, és az STDIN-ből az EOF-ig történő bemenet továbbítása a vendégügynöknek:

`qm guest exec {{vm_id}} {{arg1 arg2 ...}} --pass-stdin 1`
