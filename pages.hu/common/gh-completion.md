# gh completion

> Shell-kiegészítő szkriptek generálása a GitHub CLI-parancsokhoz. További információ: <https://cli.github.com/manual/gh_completion>.

- Az alparancsok súgójának megjelenítése:

`gh completion`

- Kiegészítő szkript nyomtatása:

`gh completion --shell {{bash|zsh|fish|powershell}}`

- A `gh` befejező szkript csatolása a `~/.bashrc`:

`gh completion --shell {{bash}} >> {{~/.bashrc}}`

- A `gh` befejező szkript csatolása a `~/.zshrc` címhez:

`gh completion --shell {{zsh}} >> {{~/.zshrc}}`
