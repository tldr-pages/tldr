# bun add

> Aggiungi e installa nuove dipendenze nel progetto corrente.
> Maggiori informazioni: <https://bun.com/docs>.

- Installa un singolo pacchetto:

`bun {{[a|add]}} {{package}}`

- Installa più pacchetti:

`bun {{[a|add]}} {{package1 package2 ...}}`

- Installa da un repository Git:

`bun {{[a|add]}} {{git_url}}`

- Installa una versione specifica:

`bun {{[a|add]}} {{package}}@{{version}}`

- Installa da un file o una directory locale:

`bun {{[a|add]}} file:{{path/to/file_or_directory}}`

- Aggiungi una dipendenza di sviluppo:

`bun {{[a|add]}} {{[-d|--dev]}} {{package}}`

- Aggiungi un pacchetto globalmente:

`bun {{[a|add]}} {{[-g|--global]}} {{package}}`
