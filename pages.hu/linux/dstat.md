# dstat

> Sokoldalú eszköz a rendszer erőforrás-statisztikák készítésére. További információ: <http://dag.wieers.com/home-made/dstat>.

- CPU-, lemez-, net-, lapozó- és rendszerstatisztikák megjelenítése:

`dstat`

- Statisztikák megjelenítése 5 másodpercenként és csak 4 frissítéssel:

`dstat {{5}} {{4}}`

- Csak CPU- és memóriastatisztikák megjelenítése:

`dstat --cpu --mem`

- Az összes elérhető dstat bővítmény listája:

`dstat --list`

- A legtöbb memóriát és a legtöbb CPU-t használó folyamat megjelenítése:

`dstat --top-mem --top-cpu`

- Az akkumulátor százalékos arányának és a hátralévő akkumulátor-időnek a megjelenítése:

`dstat --battery --battery-remain`
