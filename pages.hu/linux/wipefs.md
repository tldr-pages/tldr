# wipefs

> A fájlrendszer, raid vagy partíciós tábla aláírásainak törlése egy eszközről. További információ: <https://manned.org/wipefs>.

- Megadott eszköz aláírásainak megjelenítése:

`sudo wipefs {{/dev/sdX}}`

- Egy adott eszköz összes elérhető aláírástípusának törlése, rekurzió nélkül a partíciókban:

`sudo wipefs --all {{/dev/sdX}}`

- Az eszköz és a partíciók összes elérhető aláírástípusának törlése glob-mintát használva:

`sudo wipefs --all {{/dev/sdX}}*`

- Száraz futtatás végrehajtása:

`sudo wipefs --all --no-act {{/dev/sdX}}`

- Törlés kikényszerítése, még akkor is, ha a fájlrendszer fel van szerelve:

`sudo wipefs --all --force {{/dev/sdX}}`
