# git changelog

> Változásnapló-jelentés készítése a repository commits és címkék alapján. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-changelog>.

- A meglévő fájl frissítése vagy egy új `History.md` fájl létrehozása a legutóbbi Git-tag óta történt commit üzenetekkel:

`git changelog`

- Listázza az aktuális verzió commitjait:

`git changelog --list`

- A `2.1.0` nevű címkétől a mostani napig terjedő commitok listázása:

`git changelog --list --start-tag {{2.1.0}}`

- List pretty formated range of commits between the tag `0.5.0` and the tag `1.0.0`:

`git changelog --start-tag {{0.5.0}} --final-tag {{1.0.0}}`

- List pretty formated range of commits between the commit `0b97430` and the tag `1.0.0`:

`git changelog --start-commit {{0b97430}} --final-tag {{1.0.0}}`

- Kimeneti fájlként adja meg a `CHANGELOG.md` címet:

`git changelog {{CHANGELOG.md}}`

- Az aktuális changelog fájl tartalmának teljes cseréje:

`git changelog --prune-old`
