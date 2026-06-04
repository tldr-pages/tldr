# bun build

> Bundla file JavaScript e TypeScript con il bundler nativo veloce di Bun.
> Maggiori informazioni: <https://bun.com/docs/bundler>.

- Bundla un entry point in un singolo file di output:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}}`

- Bundla più entry point in una directory di output:

`bun build {{path/to/entry1.ts path/to/entry2.ts ...}} --outdir {{path/to/dist}}`

- Bundla con sourcemap per il debug:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --sourcemap`

- Bundla con minificazione per la produzione:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --minify`

- Bundla per un ambiente target specifico:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --target {{browser|bun|node}}`

- Bundla in un eseguibile standalone:

`bun build {{path/to/entry.ts}} --compile --outfile {{path/to/executable}}`

- Osserva i cambiamenti dei file e ricostruisci automaticamente:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --watch`

- Bundla con dipendenze esterne non incluse nell'output:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} {{[-e|--external]}} {{react react-dom}}`
