# gh label

> Munka a GitHub-címkékkel a parancssorban. További információ: <https://cli.github.com/manual/gh_label>.

- Az aktuális könyvtárban lévő adattár címkéinek listázása:

`gh label list`

- Az aktuális könyvtárban lévő adattár címkéinek megtekintése az alapértelmezett webböngészőben:

`gh label list --web`

- Címke létrehozása az aktuális könyvtárban lévő adattárhoz egy adott névvel, leírással és színnel hexadecimális formátumban:

`gh label create {{name}} --description "{{description}}" --color {{color_hex}}`

- Az aktuális könyvtárban lévő adattár címkéjének törlése, megerősítést kérve:

`gh label delete {{name}}`

- Az aktuális könyvtárban lévő adattár adott címkéjének nevének és leírásának frissítése:

`gh label edit {{name}} --name {{new_name}} --description "{{description}}"`

- Címkék klónozása egy adott adattárból az aktuális könyvtárban lévő adattárba:

`gh label clone {{owner}}/{{repository}}`

- Súgó megjelenítése egy alparancshoz:

`gh label {{subcommand}} --help`
