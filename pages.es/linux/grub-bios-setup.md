# grub-bios-setup

> Configura un dispositivo para usar GRUB con una configuración BIOS.
> Se debe usar `grub-install` en lugar de `grub-bios-setup` en la mayoría de los casos.
> Más información: <https://manned.org/grub-bios-setup.8>.

- Configura un dispositivo para arrancar con GRUB:

`grub-bios-setup {{/dev/sdX}}`

- Instala incluso si se detectan problemas:

`grub-bios-setup {{[-f|--force]}} {{/dev/sdX}}`

- Instala GRUB en un directorio específico:

`grub-bios-setup {{[-d|--directory]}} {{/boot/grub}} {{/dev/sdX}}`
