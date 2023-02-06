# pueue enqueue

> A tárolt feladatok sorba állítása. Lásd még: `pueue stash`. További információ: <https://github.com/Nukesor/pueue>.

- Egyszerre több elrejtett feladat sorba állítása:

`pueue enqueue {{task_id}} {{task_id}}`

- Egy elrejtett feladat 60 másodperc elteltével történő várakoztatása:

`pueue enqueue --delay {{60}} {{task_id}}`

- Enqueue a stashed task next Wednesday:

`pueue enqueue --delay {{wednesday}} {{task_id}}`

- Enqueue a stasheed task after four months:

`pueue enqueue --delay "4 months" {{task_id}}`

- Enqueue a stashed task on 2021-02-19:

`pueue enqueue --delay {{2021-02-19}} {{task_id}}`

- Az összes elérhető dátum/idő formátum felsorolása:

`pueue enqueue --help`
