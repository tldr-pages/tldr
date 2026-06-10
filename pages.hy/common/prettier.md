#ավելի գեղեցիկ

> JavaScript-ի, JSON-ի, CSS-ի, YAML-ի և այլնի համար նախատեսված կոդի ձևաչափ:.
> Լրացուցիչ տեղեկություններ. <https://prettier.io/docs/cli>:.

- Ձևաչափեք ֆայլը և տպեք արդյունքը `stdout`:

`prettier {{path/to/file}}`

- Ստուգեք, արդյոք որոշակի ֆայլ ֆորմատավորված է.:

`prettier --check {{path/to/file}}`

- Գործարկել հատուկ կազմաձևման ֆայլով.:

`prettier --config {{path/to/config_file}} {{path/to/file}}`

- Ձևաչափեք ֆայլը կամ գրացուցակը, փոխարինելով բնօրինակը.:

`prettier --write {{path/to/file_or_directory}}`

- Ձևաչափեք ֆայլերը կամ գրացուցակները ռեկուրսիվորեն՝ օգտագործելով մեկ չակերտներ և առանց վերջնակետերի.:

`prettier --single-quote --trailing-comma {{none}} --write {{path/to/file_or_directory}}`

- Ձևաչափեք JavaScript և TypeScript ֆայլերը ռեկուրսիվորեն՝ փոխարինելով բնօրինակը.:

`prettier --write "**/*.{js,jsx,ts,tsx}"`
