# gh extension

> A GitHub CLI bővítmények kezelése. További információ: <https://cli.github.com/manual/gh_extension>.

- Új GitHub CLI-bővítményprojekt inicializálása egy azonos nevű könyvtárban:

`gh extension create {{extension_name}}`

- Bővítmény telepítése egy GitHub-tárból:

`gh extension install {{owner}}/{{repository}}`

- Telepített bővítmények listázása:

`gh extension list`

- Egy adott bővítmény frissítése:

`gh extension upgrade {{extension_name}}`

- Az összes bővítmény frissítése:

`gh extension upgrade --all`

- Telepített bővítmények listázása:

`gh extension list`

- Bővítmény eltávolítása:

`gh extension remove {{extension_name}}`

- Segítség megjelenítése egy alparancsról:

`gh extension {{subcommand}} --help`
