# man

> Da formato y muestra páginas del manual.
> Más información: <https://www.man7.org/linux/man-pages/man1/man.1.html>.

- Mostrar la página del manual para un comando:

`man {{command}}`

- Mostrar la página del manual para un comando de la sección 7:

`man {{7}} {{command}}`

- Listar todas las secciones disponibles para un comando:

`man --whatis {{command}}`

- Muestra las rutas usadas para la búsqueda de las páginas:

`man --path`

- Muestra la ubicación de la página del manual en lugar de la propia página:

`man --where {{command}}`

- Muestra la página del manual usando una ubicación específica:

`man --locale={{locale}} {{command}}`

- Busca las páginas del manual que contienen la string indicada:

`man --apropos "{{search_string}}"`
