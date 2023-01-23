# qmrestore

> A QemuServer vzdump biztonsági mentések visszaállítása. További információ: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Virtuális gép visszaállítása az eredeti tárolón lévő adott biztonsági mentési fájlból:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}}`

- A meglévő virtuális gép felülírása egy adott biztonsági mentési fájlból az eredeti tárolón:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --force true`

- A virtuális gép visszaállítása egy adott biztonsági mentési fájlból egy adott tárolón:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --storage {{local}}`

- A virtuális gép azonnali indítása a biztonsági másolatból, miközben a visszaállítás a háttérben történik (csak a Proxmox Backup Server esetén):

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --live-restore true`
