# man

> Da formato y muestra páginas del manual.
> Más información: <https://manned.org/man>.

- Muestra la página del manual de un comando:

`man {{comando}}`

- Abre la página del manual de un comando en un navegador (requiere que la variable `BROWSER` esté establecida):

`man {{[-Hbrowser_name|--html=browser_name]}} {{command}}`

- Muestra la página del manual de la sección 7 de un comando:

`man {{7}} {{comando}}`

- Lista todas las secciones disponibles para un comando:

`man {{[-f|--whatis]}} {{comando}}`

- Muestra las rutas usadas en la búsqueda de las páginas:

`man {{[-w|--path]}}`

- Muestra la ubicación de la página del manual en lugar de la propia página:

`man {{[-w|--where]}} {{comando}}`

- Muestra la página del manual usando un idioma (locale) específico (p.e. es para español):

`man {{[-L|--locale]}} {{idioma}} {{comando}}`

- Busca las páginas del manual que contienen la cadena de búsqueda:

`man {{[-k|--apropos]}} "{{cadena_de_búsqueda}}"`
