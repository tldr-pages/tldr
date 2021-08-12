# grub-install

> Instalați GRUB pe un dispozitiv.
> Mai multe informaţii: <https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>

- Instalați GRUB pe un sistem BIOS:

`grub-install --target={{i386-pc}} {{path/to/device}}`

- Instalați GRUB pe un sistem UEFI:

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --bootloader-id={{GRUB}}`

- Instalați modulele specifice de pre-încărcare GRUB:

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --modules="{{part_gpt part_msdos}}"`
