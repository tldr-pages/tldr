# diskpart

> Administrador de discos, volúmenes y particiones.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Ejecuta diskpart por sí mismo en un símbolo del sistema administrativo para ingresar a su línea de comandos:

`diskpart`

- [Interactivo] Lista todos los discos:

`list disk`

- [Interactivo] Selecciona un volumen:

`select volume {{volúmen}}`

- [Interactivo] Asigna una letra de unidad al volumen seleccionado:

`assign letter {{letra}}`

- [Interactivo] Crea una nueva partición:

`create partition primary`

- [Interactivo] Activa el volumen seleccionado:

`active`

- [Interactivo] Sale de diskpart:

`exit`
