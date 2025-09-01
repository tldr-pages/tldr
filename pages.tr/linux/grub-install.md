# grub-install

> Bir cihaza GRUB kurun.
> Daha fazla bilgi için: <https://www.gnu.org/software/grub/manual/grub/grub.html#Installing-GRUB-using-grub_002dinstall>.

- Bir BIOS sisteme GRUB kurun:

`sudo grub-install {{cihaz/yolu}}`

- GRUB'u, bir BIOS sistemine belirtilen mimari ile kurun:

`sudo grub-install --target {{i386-pc}} {{cihaz/yolu}}`

- Bir UEFI sisteme GRUB kurun:

`sudo grub-install --efi-directory {{efi/dizini/yolu}}`

- GRUB'u, UEFI bir sisteme belirtilen mimari ve belirtilen önyükleme menü yazısı ile kurun:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{efi/dizin/yolu}} --bootloader-id {{GRUB}}`

- GRUB'u, yükleme öncesi özel modüller ile kurun:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{efi/dizin/yolu}} --modules "{{part_gpt part_msdos}}"`

- Yardımı görüntüleyin:

`grub-install {{[-?|--help]}}`
