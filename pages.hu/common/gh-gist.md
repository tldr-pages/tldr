# gh gist

> Munka a GitHub listákkal a parancssoron. További információ: <https://cli.github.com/manual/gh_gist>.

- Új Gist létrehozása fájlok szóközzel elválasztott listájából:

`gh gist create {{path/to/files}}`

- Új Gist létrehozása leírással:

`gh gist create {{path/to/file}} --desc "{{description}}"`

- Gist szerkesztése:

`gh gist edit {{id_or_url}}`

- Az aktuálisan bejelentkezett felhasználó tulajdonában lévő Gistek listázása:

`gh gist list --limit {{int}}`

- Gist megtekintése az alapértelmezett böngészőben Markdown megjelenítés nélkül:

`gh gist view {{id_or_url}} --web --raw`
