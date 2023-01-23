# pueue kill

> Folyamatban lévő feladatok vagy egész csoportok megállítása. További információ: <https://github.com/Nukesor/pueue>.

- Az alapértelmezett csoportban lévő összes feladat megállítása:

`pueue kill`

- Egy adott feladat megállítása:

`pueue kill {{task_id}}`

- Egy feladat megállítása és az összes gyermekfolyamatának befejezése:

`pueue kill --children {{task_id}}`

- Egy csoport összes feladatának megállítása és a csoport szüneteltetése:

`pueue kill --group {{group_name}}`

- Az összes csoport összes feladatának megállítása és az összes csoport szüneteltetése:

`pueue kill --all`
