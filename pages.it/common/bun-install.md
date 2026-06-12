# bun install

> Installa le dipendenze JavaScript di un progetto da `package.json`.
> More information: <https://bun.com/docs/pm/cli/install>.

- Installa tutte le dipendenze elencate in `package.json`:
- 
`bun {{[i|install]}}`

- Installa un singolo pacchetto (alias di `bun add`):
- 
`bun {{[i|install]}} {{pacchetto}}@{{versione}}`

- Installa un pacchetto globalmente:
- 
`bun {{[i|install]}} {{[-g|--global]}} {{pacchetto}}`

- Installa solo le dipendenze di produzione (salta le `devDependencies`):
- 
`bun {{[i|install]}} {{[-p|--production]}}`

- Installa le dipendenze esattamente dal lockfile `bun.lockb` (lockfile congelato):
- 
`bun {{[i|install]}} --frozen-lockfile`

- Forza il download di tutti i pacchetti dal registry ignorando la cache:
- 
`bun {{[i|install]}} {{[-f|--force]}}`
