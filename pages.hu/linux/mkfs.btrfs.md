# mkfs.btrfs

> Létrehoz egy btrfs fájlrendszert. Alapértelmezett értéke: `raid1`, ami egy adott adatblokk 2 példányát adja meg 2 különböző eszközön elosztva. További információ: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- Egyetlen eszközön btrfs fájlrendszer létrehozása:

`sudo mkfs.btrfs --metadata single --data single {{/dev/sda}}`

- Létrehoz egy btrfs fájlrendszert több eszközön raid1 segítségével:

`sudo mkfs.btrfs --metadata raid1 --data raid1 {{/dev/sda}} {{/dev/sdb}} {{/dev/sdN}}`

- Címke beállítása a fájlrendszerhez:

`sudo mkfs.btrfs --label "{{label}}" {{/dev/sda}} [{{/dev/sdN}}]`
