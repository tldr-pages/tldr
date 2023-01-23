# genfstab

> Arch Linux telepítő szkript az fstab fájlhoz való hozzáadásra alkalmas kimenet létrehozására. További információ: <https://man.archlinux.org/man/extra/arch-install-scripts/genfstab.8>.

- Egy fstab kompatibilis kimenet megjelenítése egy kötetcímke alapján:

`genfstab -L {{path/to/mount_point}}`

- Az fstab kompatibilis kimenet megjelenítése egy kötet UUID alapján:

`genfstab -U {{path/to/mount_point}}`

- Az fstab fájl létrehozásának szokásos módja, root jogosultságokat igényel:

`genfstab -U {{/mnt}} >> {{/mnt/etc/fstab}}`

- Kötet csatolása az fstab fájlhoz az automatikus csatoláshoz:

`genfstab -U {{path/to/mount_point}} | sudo tee -a /etc/fstab`
