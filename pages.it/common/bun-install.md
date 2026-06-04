# bun install

> Installa le dipendenze di un progetto usando Bun.
> Maggiori informazioni: <https://bun.com/docs/pm/cli/install>.

- Installa le dipendenze definite in `package.json`:

`bun install`

- Installa le dipendenze e aggiorna il lockfile:

`bun install --force`

- Installa una dipendenza opzionale:

`bun install {{nome-pacchetto}} --optional`

- Installa le dipendenze in modalità produzione solo, senza devDependencies:

`bun install --production`

- Installa le dipendenze usando un registry personalizzato:

`bun install --registry {{https://registry.example.com}}`

- Installa le dipendenze in una directory specifica:

`bun install --path {{path/to/node_modules}}`

- Mostra i moduli installati:

`bun install --print`

- Visualizza l'help:

`bun install --help`
