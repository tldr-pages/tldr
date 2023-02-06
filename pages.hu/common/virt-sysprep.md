# virt-sysprep

> Virtuális gépkép visszaállítása, konfigurációjának megszüntetése vagy testreszabása. További információ: <https://manned.org/virt-sysprep>.

- Az összes támogatott művelet felsorolása (az engedélyezett műveletek csillaggal vannak jelölve):

`virt-sysprep --list-operations`

- Az összes engedélyezett művelet futtatása, de valójában nem alkalmazza a módosításokat:

`virt-sysprep --domain {{vm_name}} --dry-run`

- Csak a megadott műveletek futtatása:

`virt-sysprep --domain {{vm_name}} --operations {{operation1,operation2,...}}`

- Új `/etc/machine-id` fájl generálása és a testreszabások engedélyezése, hogy a hálózati konfliktusok elkerülése érdekében megváltoztathassa az állomás nevét:

`virt-sysprep --domain {{vm_name}} --enable {{customizations}} --hostname {{host_name}} --operation {{machine-id}}`
