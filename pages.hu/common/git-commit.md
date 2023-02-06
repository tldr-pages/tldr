# git commit

> Fájlok commitolása a tárolóba. További információ: <https://git-scm.com/docs/git-commit>.

- Elvégezhető fájlok rögzítése az adattárba egy üzenettel:

`git commit -m "{{message}}"`

- Elvégezhető fájlok rögzítése egy fájlból beolvasott üzenettel:

`git commit --file {{path/to/commit_message_file}}`

- Az összes módosított fájl automatikus szakaszolása és üzenettel történő rögzítése:

`git commit -a -m "{{message}}"`

- Lekötött fájlok átvitele és \[S\]ignálása a `~/.gitconfig` oldalon meghatározott GPG-kulccsal:

`git commit -S -m "{{message}}"`

- A legutóbbi commit frissítése az aktuálisan szakaszolt változtatások hozzáadásával, a commit hash-jának megváltoztatásával:

`git commit --amend`

- Csak bizonyos (már beállított) fájlok commitolása:

`git commit {{path/to/file1}} {{path/to/file2}}`

- Létrehoz egy commitot, még akkor is, ha nincsenek staged fájlok:

`git commit -m "{{message}}" --allow-empty`
