# winget

> Administrador de paquetes de Windows.
> Más información: <https://learn.microsoft.com/windows/package-manager/winget>.

- Instala un paquete:

`winget {{[add|install]}} {{paquete}}`

- Elimina un paquete (Nota: `remove` también se puede usar en lugar de `uninstall`):

`winget {{[rm|uninstall]}} {{paquete}}`

- Muestra información sobre un paquete:

`winget show {{paquete}}`

- Busca un paquete:

`winget search {{paquete}}`

- Actualiza todos los paquetes a las versiones más recientes:

`winget upgrade {{[-r|--all]}}`

- Lista todos los paquetes instalados que se pueden gestionar con `winget`:

`winget {{[ls|list]}} {{[-s|--source]}} winget`

- Importa paquetes desde un archivo o exportar paquetes instalados a un archivo:

`winget {{import|export}} {{--import-file|--output}} {{ruta/al/archivo}}`

- Valida manifiestos antes de enviar un PR al repositorio winget-pkgs:

`winget validate {{ruta/al/manifiesto}}`
