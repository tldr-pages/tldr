# tldr-lint

> Controleer en formatteer `tldr` pagina's.
> Opmerking: `tldrl` kan gebruikt worden als een alias voor `tldr-lint`.
> Meer informatie: <https://github.com/tldr-pages/tldr-lint#usage>.

- Controleer een enkele pagina of alle pagina's in een map:

`tldr-lint {{pad/naar/pagina_of_map}}`

- Negeer specifieke `tldr-lint` foutcodes tijdens het controleren:

`tldr-lint {{[-I|--ignore]}} {{TLDR001,TLDR002,...}}`

- Formatteer een specifieke pagina naar `stdout`:

`tldr-lint {{[-f|--format]}} {{pad/naar/pagina.md}}`

- Formatteer een pagina in place:

`tldr-lint {{[-f|--format]}} {{[-i|--in-place]}} {{pad/naar/pagina.md}}`
