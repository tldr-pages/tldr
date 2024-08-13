# sbctl

> Un gestor de claves de arranque seguro fácil de usar.
> Nota: no registrar los certificados de Microsoft puede bloquear su sistema. Vea <https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom>.
> Más información: <https://github.com/Foxboron/sbctl#usage>.

- Muestra el estado actual del arranque seguro:

`sbctl status`

- Crea claves de arranque seguro personalizadas (todo se almacena en `/var/lib/sbctl`):

`sbctl create-keys`

- Inscribe las claves de arranque seguro personalizadas y los certificados de proveedor UEFI de Microsoft:

`sbctl enroll-keys --microsoft`

- Firma un binario EFI con la clave creada y guarda el archivo en la base de datos:

`sbctl sign {{-s|--save}} {{ruta/al/binario_efi}}`

- Vuelve a firmar todos los archivos guardados:

`sbctl sign-all`

- Comprueba que se han firmado todos los ejecutables EFI de la partición EFI del sistema:

`sbctl verify`
