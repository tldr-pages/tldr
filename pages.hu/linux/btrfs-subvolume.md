# btrfs subvolume

> A btrfs alkötegek és pillanatfelvételek kezelése. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Hozzon létre egy új üres alkötetet:

`sudo btrfs subvolume create {{path/to/new_subvolume}}`

- A megadott fájlrendszer összes alkötegének és pillanatfelvételének listázása:

`sudo btrfs subvolume list {{path/to/btrfs_filesystem}}`

- Alkötet törlése:

`sudo btrfs subvolume delete {{path/to/subvolume}}`

- Csak olvasható pillanatkép létrehozása egy meglévő alkötetről:

`sudo btrfs subvolume snapshot -r {{path/to/source_subvolume}} {{path/to/target}}`

- Létrehoz egy írható-olvasható pillanatképet egy meglévő részfolyóiratról:

`sudo btrfs subvolume snapshot {{path/to/source_subvolume}} {{path/to/target}}`

- Részletes információk megjelenítése egy alkötetről:

`sudo btrfs subvolume show {{path/to/subvolume}}`
