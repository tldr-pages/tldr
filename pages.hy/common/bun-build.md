# bun build

> Փաթեթավորեք JavaScript և TypeScript ֆայլերը Bun-ի արագ բնիկ փաթեթով:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/bundler>:.

- Միավորել մուտքի կետը մեկ ելքային ֆայլի մեջ.:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}}`

- Միավորել բազմաթիվ մուտքային կետեր ելքային գրացուցակում.:

`bun build {{path/to/entry1.ts path/to/entry2.ts ...}} --outdir {{path/to/dist}}`

- Աղբյուրի քարտեզներով փաթեթ՝ վրիպազերծման համար.:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --sourcemap`

- Արտադրության համար մինիֆիկացումով փաթեթ.:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --minify`

- Փաթեթ հատուկ թիրախային միջավայրով.:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --target {{browser|bun|node}}`

- Փաթեթ առանձին գործարկվողի համար.:

`bun build {{path/to/entry.ts}} --compile --outfile {{path/to/executable}}`

- Դիտեք ֆայլի փոփոխությունները և ինքնաբերաբար վերակառուցեք.:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --watch`

- Արտաքին կախվածություններով փաթեթ, որը ներառված չէ ելքի մեջ.:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} {{[-e|--external]}} {{react react-dom}}`
