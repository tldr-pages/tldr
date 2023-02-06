# grub-install

> A GRUB telepítése egy eszközre. További információ: <https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>.

- A GRUB telepítése BIOS rendszerre:

`grub-install --target={{i386-pc}} {{path/to/device}}`

- A GRUB telepítése UEFI rendszerre:

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --bootloader-id={{GRUB}}`

- A GRUB telepítése bizonyos modulok előzetes betöltésével:

`grub-install --target={{x86_64-efi}} --efi-directory={{path/to/efi_directory}} --modules="{{part_gpt part_msdos}}"`
