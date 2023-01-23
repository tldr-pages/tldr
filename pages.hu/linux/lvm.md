# lvm

> Fizikai kötetek, kötetcsoportok és logikai kötetek kezelése a Logical Volume Manager (LVM) interaktív shell segítségével. További információ: <https://man7.org/linux/man-pages/man8/lvm.8.html>.

- Indítsa el a Logikai kötetkezelő interaktív héját:

`sudo lvm`

- A Logikai kötetkezelő parancsok felsorolása:

`sudo lvm help`

- Egy meghajtó vagy partíció inicializálása fizikai kötetként való használatra:

`sudo lvm pvcreate {{/dev/sdXY}}`

- A fizikai kötetekre vonatkozó információk megjelenítése:

`sudo lvm pvdisplay`

- Létrehoz egy vg1 nevű kötetcsoportot a fizikai kötetből a `/dev/sdXY` oldalon:

`sudo lvm vgcreate {{vg1}} {{/dev/sdXY}}`

- A kötetcsoportokról szóló információk megjelenítése:

`sudo lvm vgdisplay`

- 10G méretű logikai kötet létrehozása a vg1 kötetcsoportból:

`sudo lvm lvcreate -L {{10G}} {{vg1}}`

- A logikai kötetekről szóló információk megjelenítése:

`sudo lvm lvdisplay`
