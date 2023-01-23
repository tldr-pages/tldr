# pre-commit

> Létrehozhat Git horgokat, amelyek a commit előtt lefutnak. További információ: <https://pre-commit.com>.

- Telepítse a pre-commit-et a Git hooks-okba:

`pre-commit install`

- Futtasson pre-commit horgokat az összes staged fájlon:

`pre-commit run`

- Futtasson pre-commit horgokat minden fájlra, legyen az staged vagy unstaged:

`pre-commit run --all-files`

- A pre-commit cache kitakarítása:

`pre-commit clean`
