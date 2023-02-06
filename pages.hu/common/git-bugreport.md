# git bugreport

> A rendszer és a felhasználó hibakeresési információit rögzíti, és egy szöveges fájlt generál, amely segít a Gitben történő hibabejelentésben. További információ: <https://git-scm.com/docs/git-bugreport>.

- Új hibajelentő fájl létrehozása az aktuális könyvtárban:

`git bugreport`

- Új hibajelentésfájlt hoz létre a megadott könyvtárban, létrehozva azt, ha nem létezik:

`git bugreport --output-directory {{path/to/directory}}`

- Új hibajelentésfájl létrehozása a megadott fájlnév utótaggal a `strftime` formátumban:

`git bugreport --suffix {{%m%d%y}}`
