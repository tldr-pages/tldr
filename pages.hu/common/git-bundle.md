# git bundle

> Objektumok és hivatkozások csomagolása egy archívumba. További információ: <https://git-scm.com/docs/git-bundle>.

- Hozzon létre egy csomagfájlt, amely egy adott ág összes objektumát és hivatkozását tartalmazza:

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- Az összes ágat tartalmazó csomagfájl létrehozása:

`git bundle create {{path/to/file.bundle}} --all`

- Az aktuális ág utolsó 5 commit-ját tartalmazó csomagfájl létrehozása:

`git bundle create {{path/to/file.bundle}} -{{5}} {{HEAD}}`

- Csomagfájl létrehozása a legutóbbi 7 napból:

`git bundle create {{path/to/file.bundle}} --since={{7.days}} {{HEAD}}`

- Ellenőrizze, hogy a csomagfájl érvényes-e és alkalmazható-e az aktuális tárolóhoz:

`git bundle verify {{path/to/file.bundle}}`

- A csomagban található hivatkozások listájának kiírása a szabványos kimenetre:

`git bundle unbundle {{path/to/file.bundle}}`

- Egy adott ág feloldása egy csomagfájlból az aktuális adattárba:

`git pull {{path/to/file.bundle}} {{branch_name}}`
