# git blame

> A commit hash és az utolsó szerző megjelenítése a fájl minden egyes sorában. További információ: <https://git-scm.com/docs/git-blame>.

- Fájl nyomtatása a szerző nevével és a commit hash-sel minden sorban:

`git blame {{path/to/file}}`

- Fájl nyomtatása a szerző e-mail címével és a commit hash-sel minden sorban:

`git blame -e {{path/to/file}}`

- Fájl nyomtatása a szerző nevével és a commit hash-sel minden sorban egy adott commitnál:

`git blame {{commit}} {{path/to/file}}`

- Fájl nyomtatása a szerző nevével és a commit hash-val minden egyes sorban egy adott commit előtt:

`git blame {{commit}}~ {{path/to/file}}`
