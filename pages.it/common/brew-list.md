# brew list

> Elenca formule/cask installati o i loro file.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

- Elenca tutte le formule e i cask installati:

`brew {{[ls|list]}}`

- Elenca i file appartenenti a una formula installata:

`brew {{[ls|list]}} {{formula}}`

- Elenca gli artifact di un cask:

`brew {{[ls|list]}} {{cask}}`

- Elenca solo le formule:

`brew {{[ls|list]}} --formula`

- Elenca solo i cask:

`brew {{[ls|list]}} --cask`

- Elenca solo le formule fissate:

`brew {{[ls|list]}} --pinned`
