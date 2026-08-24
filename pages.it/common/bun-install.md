# bun install

> Installa le dipendenze JavaScript di un progetto da `package.json`.
> Maggiori informazioni: <https://bun.com/docs/pm/cli/install>.

- Installa tutte le dipendenze elencate in `package.json`:

`bun {{[i|install]}}`

- Installa un singolo pacchetto (alias di `bun add`):

`bun {{[i|install]}} {{nome_pacchetto}}@{{versione}}`

- Installa un pacchetto globalmente:

`bun {{[i|install]}} {{[-g|--global]}} {{nome_pacchetto}}`

- Installa solo le dipendenze di produzione (salta `devDependencies`):

`bun {{[i|install]}} {{[-p|--production]}}`

- Installa le dipendenze esattamente dal lockfile `bun.lockb` (frozen lockfile):

`bun {{[i|install]}} --frozen-lockfile`

- Forza il download di tutti i pacchetti dal registro, ignorando la cache:

`bun {{[i|install]}} {{[-f|--force]}}`
