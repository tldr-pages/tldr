# btrfs device

> Eszközök kezelése btrfs fájlrendszerben. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Egy vagy több eszköz hozzáadása egy btrfs fájlrendszerhez:

`sudo btrfs device add {{path/to/block_device1}} [{{path/to/block_device2}}] {{path/to/btrfs_filesystem}}`

- Eszköz eltávolítása egy btrfs fájlrendszerből:

`sudo btrfs device remove {{path/to/device|device_id}} [{{...}}]`

- Hibastatisztikák megjelenítése:

`sudo btrfs device stats {{path/to/btrfs_filesystem}}`

- Az összes lemez átvizsgálása és a kernel tájékoztatása az összes észlelt btrfs fájlrendszerről:

`sudo btrfs device scan --all-devices`

- Lemezenkénti részletes kiosztási statisztikák megjelenítése:

`sudo btrfs device usage {{path/to/btrfs_filesystem}}`
