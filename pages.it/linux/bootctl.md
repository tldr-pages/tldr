# bootctl

> Controlla le impostazioni di avvio del firmware EFI e gestisce il boot loader.
> Maggiori informazioni: <https://www.freedesktop.org/software/systemd/man/bootctl.html>.

- Mostra informazioni sul firmware di sistema e i boot loader:

`bootctl`

- Mostra tutte le voci di boot loader disponibili:

`bootctl list`

- Imposta un flag per avviare nel firmware di sistema al prossimo riavvio (simile a `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Specifica il percorso alla partizione EFI di sistema (predefinito `/efi/`, `/boot/` o `/boot/efi`):

`bootctl --esp-path /{{path/to/efi_system_partition}}/`

- Installa `systemd-boot` nella partizione EFI di sistema:

`sudo bootctl install`

- Rimuove tutte le versioni installate di `systemd-boot` dalla partizione EFI di sistema:

`sudo bootctl remove`
