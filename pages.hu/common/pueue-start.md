# pueue start

> Bizonyos feladatok vagy feladatcsoportok működésének folytatása. Lásd még: `pueue pause`. További információ: <https://github.com/Nukesor/pueue>.

- Az alapértelmezett csoport összes feladatának folytatása:

`pueue start`

- Egy adott feladat folytatása:

`pueue start {{task_id}}`

- Több feladat egyidejű folytatása:

`pueue start {{task_id}} {{task_id}}`

- Az összes feladat folytatása és gyermekeik elindítása:

`pueue start --all --children`

- Egy adott csoport összes feladatának folytatása:

`pueue start group {{group_name}}`
