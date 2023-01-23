# btrfs

> A copy-on-write (COW) elven alapuló fájlrendszer Linux számára. Néhány alparancsnak, mint például a `btrfs device`, saját használati dokumentációja van. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Alkötet létrehozása:

`sudo btrfs subvolume create {{path/to/subvolume}}`

- Alkötetek listázása:

`sudo btrfs subvolume list {{path/to/mount_point}}`

- Helyhasználati információk megjelenítése:

`sudo btrfs filesystem df {{path/to/mount_point}}`

- Enable quota:

`sudo btrfs quota enable {{path/to/subvolume}}`

- Kvóta megjelenítése:

`sudo btrfs qgroup show {{path/to/subvolume}}`
