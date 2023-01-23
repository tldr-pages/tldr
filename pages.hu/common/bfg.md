# bfg

> A nagyméretű fájlok vagy jelszavak eltávolítása a Git előzményeiből, mint a git-filter-branch. Megjegyzés: ha a tárolód távolihoz van csatlakoztatva, akkor kényszerítened kell a push-t. További információ: <https://rtyley.github.io/bfg-repo-cleaner/>.

- Távolítson el egy érzékeny adatokat tartalmazó fájlt, de hagyja érintetlenül a legutóbbi commitot:

`bfg --delete-files {{file_with_sensitive_data}}`

- Eltávolítja a megadott fájlban említett összes szöveget, bárhol is található az adattár előzményeiben:

`bfg --replace-text {{path/to/file.txt}}`
