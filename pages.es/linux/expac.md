# expac

> Una herramienta de extracción de datos para bases de datos alpm, que ofrece una flexibilidad similar a printf para utilidades basadas en pacman.
> Vea también: `pacman`.
> Más información: <https://github.com/falconindy/expac#name>.

- Lista las dependencias de un paquete:

`expac -S '%D' {{paquete}}`

- Lista las dependencias opcionales de un paquete:

`expac -S "%o" {{paquete}}`

- Lista el tamaño de descarga de los paquetes en MiB:

`expac -S -H M '%k\t%n' {{paquete1 paquete2 ...}}`

- Lista los paquetes marcados para actualización con su tamaño de descarga:

`expac -S -H M '%k\t%n' $(pacman -Qqu) | sort -sh`

- Listar los paquetes instalados explícitamente con sus dependencias opcionales:

`expac -d '\n\n' -l '\n\t' -Q '%n\n\t%O' $(pacman -Qeq)`
