# qm guest passwd

> Jelszó beállítása egy adott felhasználó számára a QEMU/KVM Virtual Machine Managerben. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Jelszó beállítása egy adott felhasználóhoz egy virtuális gépen interaktívan:

`qm guest passwd {{vm_id}} {{username}}`

- Interaktívan beállíthat egy már eleve hashelt jelszót egy adott felhasználóhoz egy virtuális gépen:

`qm guest passwd {{vm_id}} {{username}} --crypted 1`
