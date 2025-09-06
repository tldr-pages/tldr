# xcode-select

> Cambia entre diferentes versiones de Xcode y las herramientas incluidas para desarrolladores.
> También se utiliza para actualizar la ruta a Xcode si se mueve después de la instalación.
> Más información: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Instala las herramientas de línea de comandos de Xcode:

`xcode-select --install`

- Selecciona una ruta determinada como directorio de desarrollador activo:

`xcode-select --switch {{ruta/al/Xcode.app/Contents/Developer}}`

- Selecciona una instancia de Xcode determinada y utiliza su directorio de desarrollador como directorio activo:

`xcode-select --switch {{ruta/al/archivo/Xcode_file.app}}`

- Muestra el directorio de desarrollador seleccionado:

`xcode-select --print-path`

- Descarta cualquier directorio de desarrolladores especificado por el usuario para que se encuentre mediante el mecanismo de búsqueda predeterminado:

`sudo xcode-select --reset`
