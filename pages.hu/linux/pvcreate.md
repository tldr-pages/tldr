# pvcreate

> Egy lemez vagy partíció inicializálása fizikai kötetként való használatra. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/pvcreate.8.html>.

- A `/dev/sda1` kötet inicializálása az LVM általi használatra:

`pvcreate {{/dev/sda1}}`

- Kényszeríti a létrehozást megerősítő kérés nélkül:

`pvcreate --force {{/dev/sda1}}`
