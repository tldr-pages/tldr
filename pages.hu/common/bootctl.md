# bootctl

> Az EFI firmware boot beállításainak vezérlése és a bootloader kezelése. További információ: <https://manned.org/bootctl>.

- A rendszer firmware-ével és a bootloaderekkel kapcsolatos információk megjelenítése:

`sudo bootctl status`

- Beállíthat egy zászlót, hogy a következő indításkor a rendszer firmware-ét indítsa el (hasonlóan a `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Az EFI rendszerpartíció elérési útvonalának megadása (alapértelmezés szerint `/efi/`, `/boot/` vagy `/boot/efi`):

`sudo bootctl --esp-path={{/path/to/efi_system_partition/}}`

- Az összes rendelkezésre álló bootloader bejegyzés megjelenítése:

`sudo bootctl list`

- A `systemd-boot` telepítése az EFI rendszerpartícióra:

`sudo bootctl install`

- A `systemd-boot` összes telepített verziójának eltávolítása az EFI rendszerpartícióról:

`sudo bootctl remove`
