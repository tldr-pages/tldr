# upt

> Interfaz unificada para gestionar paquetes en varios sistemas operativos, tales como Windows, diversas distribuciones de Linux, macOS, FreeBSD e incluso Haiku.
> Requiere que el gestor de paquetes nativo del sistema operativo esté instalado.
> Vea también: `flatpak`, `brew`, `scoop`, `apt`, `dnf`.
> Más información: <https://github.com/sigoden/upt>.

- Actualiza la lista de paquetes disponibles:

`upt update`

- Busca un paquete determinado:

`upt search {{término_de_búsqueda}}`

- Muestra información sobre un paquete:

`upt info {{paquete}}`

- Instala un paquete determinado:

`upt install {{paquete}}`

- Elimina un paquete determinado:

`upt {{remove|uninstall}} {{paquete}}`

- Actualiza todos los paquetes instalados:

`upt upgrade`

- Actualiza un paquete determinado:

`upt upgrade {{paquete}}`

- Lista los paquetes instalados:

`upt list`
