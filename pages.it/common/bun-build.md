# bun build

> Bundla file JavaScript e TypeScript con il bundler nativo veloce di Bun.
> Maggiori informazioni: <https://bun.com/docs/bundler>.

- Bundla un entry point in un singolo file di output:

`bun build {{percorso/dell/entry.ts}} --outfile {{percorso/del/output.js}}`

- Bundla più entry point in una directory di output:

`bun build {{percorso/dell/entry1.ts percorso/dell/entry2.ts ...}} --outdir {{percorso/del/dist}}`

- Bundla con sourcemap per il debug:

`bun build {{percorso/dell/entry.ts}} --outfile {{percorso/del/output.js}} --sourcemap`

- Bundla con minificazione per la produzione:

`bun build {{percorso/dell/entry.ts}} --outfile {{percorso/del/output.js}} --minify`

- Bundla per un ambiente target specifico:

`bun build {{percorso/dell/entry.ts}} --outfile {{percorso/del/output.js}} --target {{browser|bun|node}}`

- Bundla in un eseguibile standalone:

`bun build {{percorso/dell/entry.ts}} --compile --outfile {{percorso/dell/executable}}`

- Osserva i cambiamenti dei file e ricostruisci automaticamente:

`bun build {{percorso/dell/entry.ts}} --outfile {{percorso/del/output.js}} --watch`

- Bundla con dipendenze esterne non incluse nell'output:

`bun build {{percorso/dell/entry.ts}} --outfile {{percorso/del/output.js}} {{[-e|--external]}} {{react react-dom}}`
