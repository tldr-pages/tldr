# btrfs check

> A btrfs fájlrendszer ellenőrzése vagy javítása. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- A btrfs fájlrendszer ellenőrzése:

`sudo btrfs check {{path/to/partition}}`

- Egy btrfs fájlrendszer ellenőrzése és javítása (veszélyes):

`sudo btrfs check --repair {{path/to/partition}}`

- Az ellenőrzés előrehaladásának megjelenítése:

`sudo btrfs check --progress {{path/to/partition}}`

- Ellenőrizze az egyes adatblokkok ellenőrző összegét (ha a fájlrendszer jó):

`sudo btrfs check --check-data-csum {{path/to/partition}}`

- A `n`-th superblock használata (`n` lehet 0, 1 vagy 2):

`sudo btrfs check --super {{n}} {{path/to/partition}}`

- Állítsa újra az ellenőrzőösszeg-fát:

`sudo btrfs check --repair --init-csum-tree {{path/to/partition}}`

- Állítsa újra a kiterjedési fát:

`sudo btrfs check --repair --init-extent-tree {{path/to/partition}}`
