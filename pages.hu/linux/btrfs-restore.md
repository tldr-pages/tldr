# btrfs restore

> Próbálja megmenteni a fájlokat egy sérült btrfs fájlrendszerből. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- A btrfs fájlrendszer összes fájljának visszaállítása egy adott könyvtárba:

`sudo btrfs restore {{path/to/btrfs_device}} {{path/to/target_directory}}`

- A btrfs fájlrendszerből visszaállítandó fájlok listázása (nem írja ki):

`sudo btrfs restore --dry-run {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Egy adott regexnek megfelelő fájlok visszaállítása (\[c\]ase-érzékeny) btrfs fájlrendszerből visszaállítandó fájlok (a célfájl(ok) összes szülői könyvtárának is meg kell felelnie):

`sudo btrfs restore --path-regex {{regex}} -c {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Fájlok visszaállítása btrfs fájlrendszerből egy adott gyökérfa `bytenr` használatával (lásd `btrfs-find-root`):

`sudo btrfs restore -t {{bytenr}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Fájlok visszaállítása btrfs fájlrendszerből (metaadatokkal, kiterjesztett attribútumokkal és Symlinkekkel együtt), a célfájlok felülírásával:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{path/to/btrfs_device}} {{path/to/target_directory}}`
