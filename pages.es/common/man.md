# man

> Formatea y muestra páginas de manual.
> Vea también: `whatis`, `apropos`.
> Más información: <https://manned.org/man>.

- Muestra la página de manual de un comando:

`man {{comando}}`

- Abre la página de manual de un comando en un navegador (se puede omitir `=nombre_navegador` si está definida la variable `$BROWSER`):

`man {{[-H|--html=]}}{{nombre_navegador}} {{comando}}`

- Muestra la página de manual de un comando de la sección 7:

`man 7 {{comando}}`

- Muestra todas las secciones disponibles para un comando:

`man {{[-f|--whatis]}} {{comando}}`

- Muestra la ruta en la que se buscan las páginas de manual:

`man {{[-w|--path]}}`

- Muestra la ubicación de una página de manual en lugar de la propia página:

`man {{[-w|--where]}} {{comando}}`

- Muestra la página de manual utilizando una configuración regional específica:

`man {{[-L|--locale]}} {{configuración_regional}} {{comando}}`

- Busca páginas de manual que contengan una cadena de búsqueda:

`man {{[-k|--apropos]}} "{{cadena_de_búsqueda}}"`
