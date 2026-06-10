# bun run

> Կատարեք JavaScript/TypeScript ֆայլ կամ սկրիպտ `package.json`-ից:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/runtime>:.

- Գործարկել `package.json`-ով սահմանված սկրիպտը՝:

`bun run {{script_name}}`

- Գործարկել JavaScript կամ TypeScript ֆայլ ուղղակիորեն.:

`bun run {{path/to/file.ts}}`

- Գործարկել ֆայլը «դիտելու» ռեժիմում (վերագործարկվում է ավտոմատ կերպով, երբ ֆայլը փոխվում է).:

`bun run --watch {{path/to/file.ts}}`

- Գործարկել ֆայլը հատուկ կազմաձևման ֆայլի միջոցով.:

`bun run {{[-c|--config]}} {{path/to/bunfig.toml}} {{path/to/file.ts}}`
