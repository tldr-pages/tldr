# tea

> Parancssori eszköz a Gitea szerverekkel való interakcióhoz. További információ: <https://gitea.com/gitea/tea>.

- Bejelentkezés egy Gitea szerverre:

`tea login add --name "{{name}}" --url "{{url}}" --token "{{token}}"`

- Az összes tároló megjelenítése:

`tea repos ls`

- A problémák listájának megjelenítése:

`tea issues ls`

- Egy adott tárolóhoz tartozó problémák listájának megjelenítése:

`tea issues ls --repo "{{repository}}"`

- Új issue létrehozása:

`tea issues create --title "{{title}}" --body "{{body}}"`

- A nyitott pull-kérelmek listájának megjelenítése:

`tea pulls ls`

- Az aktuális adattár megnyitása böngészőben:

`tea open`
