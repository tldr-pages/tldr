# man

> Da formato y muestra páginas del manual.
> Más información: <https://manned.org/man>.

- Muestra la página del manual para un comando:

`man {{comando}}`

- Mostrar la página del manual para un comando de la sección 7:

`man {{7}} {{comando}}`

- Listar todas las secciones disponibles para un comando:

`man --whatis {{comando}}`

- Muestra las rutas usadas para la búsqueda de las páginas:

`man --path`

- Muestra la ubicación de la página del manual en lugar de la propia página:

`man --where {{comando}}`

- Muestra la página del manual usando una ubicación específica:

`man --locale={{locale}} {{comando}}`

- Busca las páginas del manual que contienen la string indicada:

`man --apropos "{{cadena_a_buscar}}"`
