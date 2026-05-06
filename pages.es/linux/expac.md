# expac

> Una herramienta de extracción de datos para bases de datos alpm, que ofrece una flexibilidad similar a printf para utilidades basadas en pacman.
> Vea también: `pacman`.
> Más información: <https://github.com/falconindy/expac#name>.

- Lista las dependencias de un paquete:

`expac {{[-S|--sync]}} '%D' {{paquete}}`

- Lista las dependencias opcionales de un paquete:

`expac {{[-S|--sync]}} "%o" {{paquete}}`

- Lista el tamaño de descarga de los paquetes en MiB:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' {{paquete1 paquete2 ...}}`

- Lista los paquetes marcados para actualización con su tamaño de descarga:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' $(pacman -Qqu) | sort {{[-sh|--sort --human-numeric-sort]}}`

- Enumera los paquetes instalados explícitamente con sus dependencias opcionales:

`expac {{[-d|--delim]}} '\n\n' {{[-l|--listdelim]}} '\n\t' {{[-Q|--query]}} '%n\n\t%O' $(pacman -Qeq)`
