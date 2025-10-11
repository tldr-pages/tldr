# grub-install

> Instala GRUB en un dispositivo.
> Más información: <https://www.gnu.org/software/grub/manual/grub/grub.html#Installing-GRUB-using-grub_002dinstall>.

- Instala GRUB en un sistema BIOS:

`sudo grub-install {{ruta/al/dispositivo}}`

- Instala GRUB en un sistema BIOS especificando la arquitectura:

`sudo grub-install --target {{i386-pc}} {{ruta/al/dispositivo}}`

- Instala GRUB en un sistema UEFI:

`sudo grub-install --efi-directory {{ruta/al/directorio_efi}}`

- Instala GRUB en un sistema UEFI especificando la arquitectura y el texto del menú de arranque:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{ruta/al/directorio_efi}} --bootloader-id {{GRUB}}`

- Instala GRUB precargando módulos específicos:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{ruta/al/directorio_efi}} --modules "{{part_gpt part_msdos}}"`

- Muestra la ayuda:

`grub-install {{[-?|--help]}}`
