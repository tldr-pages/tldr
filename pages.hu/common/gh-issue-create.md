# gh issue create

> GitHub-ügyek létrehozása egy tárolóhoz a parancssorból. További információ: <https://cli.github.com/manual/gh_issue_create>.

- Új issue létrehozása az aktuális adattárhoz interaktívan:

`gh issue create`

- Új issue létrehozása interaktívan a `bug` címkével:

`gh issue create --label "{{bug}}"`

- Új issue létrehozása interaktívan és hozzárendelése a megadott felhasználókhoz:

`gh issue create --assignee {{user1,user2,...}}`

- Új issue létrehozása címmel, törzzsel, és hozzárendelése az aktuális felhasználóhoz:

`gh issue create --title "{{title}}" --body "{{body}}" --assignee "{{@me}}"`

- Új issue létrehozása interaktívan, a test szövegének beolvasása egy fájlból:

`gh issue create --body-file {{path/to/file}}`

- Új issue létrehozása az alapértelmezett webböngészőben:

`gh issue create --web`

- A súgó megjelenítése:

`gh issue create --help`
