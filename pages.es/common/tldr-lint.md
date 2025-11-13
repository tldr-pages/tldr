# tldr-lint

> Verifica y formatea páginas `tldr`.
> Nota: `tldrl` se puede utilizar como alias de `tldr-lint`.
> Más información: <https://github.com/tldr-pages/tldr-lint#usage>.

- Verifica una sola página o todas las páginas de un directorio:

`tldr-lint {{ruta/a/página_o_directorio}}`

- Ignora códigos de error específicos de `tldr-lint` durante la verificación:

`tldr-lint {{[-I|--ignore]}} {{TLDR001,TLDR002,...}}`

- Formatea una página específica a `stdout`:

`tldr-lint {{[-f|--format]}} {{path/to/page.md}}`

- Formatea una página en el mismo lugar:

`tldr-lint {{[-f|--format]}} {{[-i|--in-place]}} {{ruta/a/página.md}}`
