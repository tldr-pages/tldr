# pueue pause

> Folyamatban lévő feladatok vagy csoportok szüneteltetése. Lásd még: `pueue start`. További információ: <https://github.com/Nukesor/pueue>.

- Az alapértelmezett csoport összes feladatának szüneteltetése:

`pueue pause`

- Egy futó feladat szüneteltetése:

`pueue pause {{task_id}}`

- Egy futó feladat szüneteltetése és az összes közvetlen gyermekének leállítása:

`pueue pause --children {{task_id}}`

- Egy csoport összes feladatának szüneteltetése és új feladatok indításának megakadályozása:

`pueue pause --group {{group_name}}`

- Az összes feladat szüneteltetése és az összes csoport új feladatok indításának megakadályozása:

`pueue pause --all`
