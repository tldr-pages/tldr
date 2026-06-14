# պոեզիայի կառուցում

> Կառուցեք «Պոեզիայի» փաթեթը որպես թարբոլ և անիվ:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#build>:.

- Կառուցեք tarball և անիվ նախագծի համար.:

`poetry build`

- Կառուցեք անիվի փաթեթ.:

`poetry build {{[-f|--format]}} wheel`

- Կառուցեք աղբյուրի բաշխում (sdist):

`poetry build {{[-f|--format]}} sdist`

- Մաքրեք ելքային գրացուցակը նախքան կառուցելը.:

`poetry build --clean`

- Սահմանեք ելքային գրացուցակը.:

`poetry build {{[-o|--output]}} {{path/to/directory}}`
