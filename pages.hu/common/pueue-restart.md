# pueue restart

> Feladatok újraindítása. További információ: <https://github.com/Nukesor/pueue>.

- Egy adott feladat újraindítása:

`pueue restart {{task_id}}`

- Egyszerre több feladat újraindítása, és azonnali indításuk (ne állítsa őket sorba):

`pueue restart --start-immediately {{task_id}} {{task_id}}`

- Egy adott feladat újraindítása egy másik útvonalról:

`pueue restart --edit-path {{task_id}}`

- Szerkesszen egy parancsot az újraindítás előtt:

`pueue restart --edit {{task_id}}`

- Egy feladat helyben történő újraindítása (külön feladatként történő sorba állítás nélkül):

`pueue restart --in-place {{task_id}}`

- Az összes sikertelen feladat újraindítása és elrejtése:

`pueue restart --all-failed --stashed`
