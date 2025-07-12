# assoc

> Muestra o cambia las asociaciones entre extensiones de archivo y tipos de archivo.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- Lista todas las asociaciones entre extensiones de archivo y tipos de archivo:

`assoc`

- Muestra el tipo de archivo asociado para una extensión específica:

`assoc {{.txt}}`

- Establece el tipo de archivo asociado para una extensión específica:

`assoc .{{txt}}={{archivotxt}}`

- Visualiza la salida de `assoc` una pantalla a la vez:

`assoc | {{extra}}`
