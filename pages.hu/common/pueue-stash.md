# pueue stash

> Tárolja a feladatokat, hogy megakadályozza azok automatikus indítását. Lásd még: `pueue start` és `pueue enqueue`. További információ: <https://github.com/Nukesor/pueue>.

- Egy várakoztatott feladat elrejtése:

`pueue stash {{task_id}}`

- Egyszerre több feladat elrejtése:

`pueue stash {{task_id}} {{task_id}}`

- Egy elrejtett feladat azonnali indítása:

`pueue start {{task_id}}`

- Sorba állítani egy feladatot, hogy az az előző feladatok befejezésekor kerüljön végrehajtásra:

`pueue enqueue {{task_id}}`
