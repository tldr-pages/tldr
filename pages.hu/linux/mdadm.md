# mdadm

> RAID-kezelő segédprogram. További információ: <https://manned.org/mdadm>.

- Tömb létrehozása:

`sudo mdadm --create {{/dev/md/MyRAID}} --level {{raid_level}} --raid-devices {{number_of_disks}} {{/dev/sdXN}}`

- Tömb leállítása:

`sudo mdadm --stop {{/dev/md0}}`

- A lemez hibásként való megjelölése:

`sudo mdadm --fail {{/dev/md0}} {{/dev/sdXN}}`

- Lemez eltávolítása:

`sudo mdadm --remove {{/dev/md0}} {{/dev/sdXN}}`

- Lemez hozzáadása a tömbhöz:

`sudo mdadm --assemble {{/dev/md0}} {{/dev/sdXN}}`

- RAID-információk megjelenítése:

`sudo mdadm --detail {{/dev/md0}}`

- Lemez visszaállítása RAID metaadatok törlésével:

`sudo mdadm --zero-superblock {{/dev/sdXN}}`
