# grub-reboot

> Establece la entrada de arranque por defecto para GRUB, solo para el siguiente arranque.
> Más información: <https://manned.org/grub-reboot>.

- Establece la entrada de arranque por defecto a un número de entrada, nombre o identificador para el siguiente arranque:

`sudo grub-reboot {{numero_entrada}}`

- Establece la entrada de arranque por defecto a un número de entrada, nombre o identificador para un directorio de arranque alternativo para el siguiente arranque:

`sudo grub-reboot --boot-directory /{{ruta/al/directorio_arranque}} {{numero_entrada}}`
