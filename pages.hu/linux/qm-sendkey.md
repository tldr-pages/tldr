# qm sendkey

> QEMU monitor kódolási kulcs esemény küldése egy virtuális gépnek. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- A megadott kulcsesemény küldése egy adott virtuális gépnek:

`qm sendkey {{vm_id}} {{key}}`

- Engedélyezi a root felhasználó számára a kulcsesemény küldését és a zárak figyelmen kívül hagyását:

`qm sendkey --skiplock {{true}} {{vm_id}} {{key}}`
