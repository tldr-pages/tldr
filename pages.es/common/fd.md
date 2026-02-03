# fd

> Busca entradas en el sistema de archivos.
> Vea también: `find`.
> Más información: <https://github.com/sharkdp/fd#how-to-use>.

- Busca de forma recursiva archivos que coincidan con un patrón específico en el directorio actual:

`fd "{{string|regex}}"`

- Busca archivos que comiencen con una cadena específica:

`fd "{{^string}}"`

- Busca archivos con una extensión específica:

`fd {{[-e|--extension]}} {{txt}}`

- Busca archivos en un directorio específico:

`fd "{{string|regex}}" {{ruta/al/directorio}}`

- Incluye archivos ignorados y ocultos en la búsqueda:

`fd {{[-H|--hidden]}} {{[-I|--no-ignore]}} "{{string|regex}}"`

- Excluye archivos que coincidan con un patrón glob específico:

`fd {{string}} {{[-E|--exclude]}} {{glob}}`

- Ejecuta un comando en cada resultado de búsqueda devuelto:

`fd "{{string|regex}}" {{[-x|--exec]}} {{comando}}`

- Busca archivos solo en el directorio actual:

`fd {{[-d|--max-depth]}} 1 "{{string|regex}}"`
