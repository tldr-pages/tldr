# husky

> Natív Git hooks made easy. További információ: <https://typicode.github.io/husky>.

- Telepítse a Husky-t az aktuális könyvtárba:

`husky install`

- A Husky telepítése egy adott könyvtárba:

`husky install {{path/to/directory}}`

- Egy adott parancs beállítása a `pre-push` kampóként a Git számára:

`husky set {{.husky/pre-push}} "{{command}} {{command_arguments}}"`

- Egy adott parancs hozzáadása az aktuális `pre-commit` horoghoz:

`husky add {{.husky/pre-commit}} "{{command}} {{command_arguments}}"`

- Husky horgok eltávolítása az aktuális könyvtárból:

`husky uninstall`

- Súgó megjelenítése:

`husky`
