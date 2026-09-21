# diskpart

> Administrador de discos, volúmenes y particiones.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Ejecuta diskpart por sí mismo en un símbolo del sistema administrativo para ingresar a su línea de comandos:

`diskpart`

- Lista todos los discos:

`list disk`

- Seleccionar un volumen:

`select volume {{volúmen}}`

- Asignar una letra de unidad al volumen seleccionado:

`assign letter {{letra}}`

- Crea una nueva partición:

`create partition primary`

- Activar el volumen seleccionado:

`active`

- Salir de diskpart:

`exit`
