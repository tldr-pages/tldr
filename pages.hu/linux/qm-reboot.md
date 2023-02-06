# qm reboot

> A virtuális gép újraindítása a virtuális gép leállításával, majd a függőben lévő módosítások alkalmazása után újraindítása. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Virtuális gép újraindítása:

`qm reboot {{vm_id}}`

- Egy virtuális gép újraindítása legfeljebb 10 másodperces várakozás után:

`qm reboot --timeout {{10}} {{vm_id}}`
