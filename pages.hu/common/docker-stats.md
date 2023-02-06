# docker stats

> A konténerek erőforrás-felhasználási statisztikáinak élő adatfolyamának megjelenítése. További információ: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Az összes futó konténer statisztikájának élő stream megjelenítése:

`docker stats`

- A konténerek szóközzel elválasztott listájára vonatkozó statisztikák élő folyamának megjelenítése:

`docker stats {{container_name}}`

- Az oszlopok formátumának módosítása a konténer CPU-használati százalékának megjelenítéséhez:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Az összes (futó és leállított) konténer statisztikájának megjelenítése:

`docker stats --all`

- A streaming statisztikák kikapcsolása és csak az aktuális statisztikák kinyerése:

`docker stats --no-stream`
