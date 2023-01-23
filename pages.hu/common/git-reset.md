# git reset

> Visszavonja a commitokat vagy a változtatásokat, visszaállítva az aktuális Git HEAD-et a megadott állapotba. Ha egy elérési utat adunk meg, akkor "unstage"-ként működik; ha egy commit hash-t vagy ágat adunk meg, akkor "uncommit"-ként működik. További információ [: https://git-scm.com/docs/git-reset](https://git-scm.com/docs/git-reset).

- Unstage everything:

`git reset`

- Bizonyos fájl(ok) unstage-elése:

`git reset {{path/to/file1 path/to/file2 ...}}`

- Interaktívan eltávolítja egy fájl egyes részeit:

`git reset --patch {{path/to/file}}`

- Visszavonja az utolsó commitot, megtartva annak változásait (és minden további commit nélküli változtatást) a fájlrendszerben:

`git reset HEAD~`

- Az utolsó két commit visszavonása, a változtatások hozzáadása az indexhez, azaz a commithoz való rendezéshez:

`git reset --soft HEAD~2`

- A még el nem könyvelt változtatások elvetése, akár szakaszoltak, akár nem (csak a még el nem könyvelt változtatásokhoz használja a `git checkout`):

`git reset --hard`

- A tároló visszaállítása egy adott commit-ra, az azóta történt commit, staged és nem commit változások elvetésével:

`git reset --hard {{commit}}`
