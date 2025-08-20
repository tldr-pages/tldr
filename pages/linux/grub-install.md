# grub-install

> Install GRUB to a device.
> More information: <https://www.gnu.org/software/grub/manual/grub/grub.html#Installing-GRUB-using-grub_002dinstall>.

- Install GRUB on a BIOS system:

`sudo grub-install {{path/to/device}}`

- Install GRUB on a BIOS system while specifying architecture:

`sudo grub-install --target {{i386-pc}} {{path/to/device}}`

- Install GRUB on an UEFI system:

`sudo grub-install --efi-directory {{path/to/efi_directory}}`

- Install GRUB on an UEFI system while specifying architecture and boot menu text:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{path/to/efi_directory}} --bootloader-id {{GRUB}}`

- Install GRUB pre-loading specific modules:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{path/to/efi_directory}} --modules "{{part_gpt part_msdos}}"`

- Display help:

`grub-install {{[-?|--help]}}`
