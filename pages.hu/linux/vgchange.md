# vgchange

> A Logical Volume Manager (LVM) kötetcsoport attribútumainak módosítása. Lásd még: `lvm`. További információ: <https://manned.org/vgchange>.

- Az összes kötetcsoportban lévő logikai kötetek aktiválási állapotának módosítása:

`sudo vgchange --activate {{y|n}}`

- A megadott kötetcsoportban lévő logikai kötetek aktiválási állapotának módosítása (meghatározás a `vgscan`) segítségével:

`sudo vgchange --activate {{y|n}} {{volume_group}}}`
