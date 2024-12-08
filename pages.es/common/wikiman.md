# wikiman

> Motor de búsqueda sin conexión para documentación.
> Soporta páginas de manuales, Arch Wiki, Gentoo Wiki, documentación de FreeBSD y tldr-pages.
> Más información: <https://github.com/filiparag/wikiman>.

- Busca un tema específico en todas las fuentes instaladas:

`wikiman {{término_de_búsqueda}}`

- Busca un tema en una fuente específica:

`wikiman -s {{fuente}} {{término_de_búsqueda}}`

- Busca un tema en dos o más fuentes específicas:

`wikiman -s {{fuente1,fuente2,...}} {{término_de_búsqueda}}`

- Lista de fuentes existentes:

`wikiman -S`

- Muestra ayuda:

`wikiman -h`
