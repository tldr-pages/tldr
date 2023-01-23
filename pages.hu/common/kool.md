# kool

> Szoftverfejlesztő környezetek építése a parancssorból. További információ: <https://kool.dev/docs/>.

- Projekt létrehozása egy adott előbeállítás használatával:

`kool create {{preset}} {{project_name}}`

- Az aktuális könyvtárban található `kool.yml` fájlban meghatározott konkrét szkript futtatása:

`kool run {{script}}`

- Szolgáltatások indítása/leállítása az aktuális könyvtárban:

`kool {{start|stop}}`

- Az aktuális könyvtárban lévő szolgáltatások állapotának megjelenítése:

`kool status`

- Frissítés a legújabb verzióra:

`kool self-update`

- A megadott héj befejező szkriptjének kinyomtatása:

`kool completion {{bash|fish|powershell|zsh}}`
