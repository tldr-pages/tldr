# git shortlog

> Összefoglalja a `git log` kimenetét. További információ: <https://git-scm.com/docs/git-shortlog>.

- Az összes átdolgozás összefoglalója, a szerző neve szerint ábécérendben csoportosítva:

`git shortlog`

- Az összes elvégzett commit összefoglalója, a commitok száma szerint rendezve:

`git shortlog -n`

- A commitok összesítésének megtekintése, a committer személye (név és e-mail cím) szerint csoportosítva:

`git shortlog -c`

- Az utolsó 5 commit összefoglalójának megtekintése (azaz egy revíziós tartomány megadása):

`git shortlog HEAD~{{5}}..HEAD`

- Az összes felhasználó, e-mail cím és a commitok száma az aktuális ágban:

`git shortlog -sne`

- Az összes felhasználó, e-mail cím és a commitok száma az összes ágban:

`git shortlog -sne --all`
