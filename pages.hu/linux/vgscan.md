# vgscan

> Az összes támogatott Logical Volume Manager (LVM) blokkeszközön lévő kötetcsoportok keresése. Lásd még: `lvm`, `vgchange`. További információ: <https://manned.org/vgscan>.

- A kötetcsoportok keresése és az egyes megtalált csoportokra vonatkozó információk kinyomtatása:

`sudo vgscan`

- A kötetcsoportok keresése és a `/dev` oldalon a megtalált csoportok logikai köteteinek eléréséhez szükséges speciális fájlok hozzáadása, ha azok még nem léteznek:

`sudo vgscan --mknodes`
