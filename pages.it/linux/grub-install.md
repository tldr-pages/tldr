# grub-install

> Installa GRUB su un dispositivo.
> Maggiori informazioni: <https://www.gnu.org/software/grub/manual/grub/grub.html#Installing-GRUB-using-grub_002dinstall>.

- Installa GRUB su un sistema BIOS:

`sudo grub-install {{path/to/device}}`

- Installa GRUB su un sistema BIOS specificando l'architettura:

`sudo grub-install --target {{i386-pc}} {{path/to/device}}`

- Installa GRUB su un sistema UEFI:

`sudo grub-install --efi-directory {{path/to/efi_directory}}`

- Installa GRUB su un sistema UEFI specificando architettura e testo del menu di avvio:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{path/to/efi_directory}} --bootloader-id {{GRUB}}`

- Installa GRUB pre-caricando moduli specifici:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{path/to/efi_directory}} --modules "{{part_gpt part_msdos}}"`

- Mostra aiuto:

`grub-install {{[-?|--help]}}`
