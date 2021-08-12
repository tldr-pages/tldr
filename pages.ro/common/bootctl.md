# bootctl

> Controlați setările de boot ale firmware-ului EFI și gestionați încărcătorul de
> Mai multe informaţii: <https://man.archlinux.org/man/bootctl.1>

- Afișați informații despre firmware-ul sistemului și bootloaderele:

`sudo bootctl status`

- Setați un steag pentru a porni în firmware-ul sistemului la următoarea pornire (similar cu `sudo systemctl reboot —firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Specificați calea către partiția de sistem EFI (implicit la `/efi/`, `/boot/` sau `/boot/efi`):

`sudo bootctl --esp-path={{/path/to/efi_system_partition/}}`

- Afișează toate intrările disponibile bootloader:

`sudo bootctl list`

- Instalați `systemd-boot” în partiția de sistem EFI:

`sudo bootctl install`

- Eliminați toate versiunile instalate de `systemd-boot” din partiția de sistem EFI:

`sudo bootctl remove`
