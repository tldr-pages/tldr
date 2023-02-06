# gh codespace

> Csatlakoztassa és kezelje kódtereit a GitHubban. További információ: <https://cli.github.com/manual/gh_codespace>.

- Interaktívan hozzon létre egy kódteret a GitHubban:

`gh codespace create`

- Az összes elérhető kódterek listája:

`gh codespace list`

- Csatlakozás egy kódtérhez SSH-n keresztül interaktívan:

`gh codespace ssh`

- Egy adott fájl átvitele egy kódtérbe interaktívan:

`gh codespace cp {{path/to/source_file}} remote:{{path/to/remote_file}}`

- Egy kódtér portjainak listázása interaktívan:

`gh codespace ports`

- A kódtér naplóinak megjelenítése interaktívan:

`gh codespace logs`

- Kódtér törlése interaktívan:

`gh codespace delete`

- Súgó megjelenítése egy alparancshoz:

`gh codespace {{code|cp|create|delete|edit|...}} --help`
