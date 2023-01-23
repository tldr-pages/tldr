# mount

> Egy teljes fájlrendszerhez való hozzáférést biztosít egy könyvtárban. További információ: <https://manned.org/mount.8>.

- Az összes csatlakoztatott fájlrendszer megjelenítése:

`mount`

- Egy eszköz csatlakoztatása egy könyvtárba:

`mount -t {{filesystem_type}} {{path/to/device_file}} {{path/to/target_directory}}`

- Egy adott könyvtár létrehozása, ha az nem létezik, és egy eszköz csatlakoztatása hozzá:

`mount --mkdir {{path/to/device_file}} {{path/to/target_directory}}`

- Eszköz csatlakoztatása egy adott felhasználó könyvtárába:

`mount -o uid={{user_id}},gid={{group_id}} {{path/to/device_file}} {{path/to/target_directory}}`

- CD-ROM eszköz (ISO9660 fájltípussal) csatlakoztatása a `/cdrom` címre (csak olvasható):

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- A `/etc/fstab` alatt definiált összes fájlrendszer csatlakoztatása:

`mount -a`

- A `/etc/fstab` alatt leírt konkrét fájlrendszer csatlakoztatása (pl. `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount {{/my_drive}}`

- Egy könyvtár mountolása egy másik könyvtárba:

`mount --bind {{path/to/old_dir}} {{path/to/new_dir}}`
