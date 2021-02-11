# grub-install

> Install GRUB to a device.
> More information: <https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>.

- Install GRUB on a BIOS system:

`grub-install --target={{i386-pc}} {{/dev/sdX}}`

- Install GRUB on an UEFI system:

`grub-install --target={{x86_64-efi}} --efi-directory={{/efi/}} --bootloader-id={{GRUB}}`
