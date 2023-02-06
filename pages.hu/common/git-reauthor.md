# git reauthor

> A szerzői identitással kapcsolatos adatok módosítása. Mivel ez a parancs átírja a Git-előzményeket, a `--force` parancsra a következő pusholáskor lesz szükség. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor>.

- Egy szerző e-mail címének és nevének módosítása a teljes Git-tárban:

`git reauthor --old-email {{old@example.com}} --correct-email {{new@example.com}} --correct-name "{{name}}"`

- Az email és a név módosítása a Git konfigurációban meghatározottakra:

`git reauthor --old-email {{old@example.com}} --use-config`

- Az összes commit e-mail címének és nevének módosítása, függetlenül az eredeti szerzőtől:

`git reauthor --all --correct-email {{name@example.com}} --correct-name {{name}}`
