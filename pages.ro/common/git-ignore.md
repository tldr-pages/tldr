# git ignore

> Afișați/actualizați fișierele `.gitignore`.
> Parte din `git-extras`. A se vedea, de asemenea, `git ignore-io`.
> Mai multe informaţii: <https://github.com/tj/git-extras/blob/master/Commands.md#git-ignore>

- Afișează conținutul tuturor fișierelor „.gitignore” globale și locale:

`git ignore`

- Ignorați fișierul (fișierele) privat, actualizând fișierul `.git/info/exclude`:

`git ignore {{file_pattern}} --private`

- Ignorați fișierul (fișierele) local, actualizând fișierul local `.gitignore`:

`git ignore {{file_pattern}}`

- Ignorați fișierul (fișierele) la nivel global, actualizând fișierul „.gitignore” global:

`git ignore {{file_pattern}} --global`
