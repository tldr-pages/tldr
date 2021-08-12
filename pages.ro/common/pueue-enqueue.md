# pueue enqueue

> Enqueue activități ascunse.
> A se vedea de asemenea: „pueue stash”.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Enqueue mai multe sarcini ascunse simultan:

`pueue enqueue {{task_id}} {{task_id}}`

- Enqueue o sarcină ascunsă după 60 de secunde:

`pueue enqueue --delay {{60}} {{task_id}}`

- Enqueue o sarcină ascuns miercurea viitoare:

`pueue enqueue --delay {{wednesday}} {{task_id}}`

- Enqueue o sarcină ascuns după patru luni:

`pueue enqueue --delay "4 months" {{task_id}}`

- Enqueue o sarcină ascunsă pe 2021-02-19:

`pueue enqueue --delay {{2021-02-19}} {{task_id}}`

- Listează toate formatele de dată/oră disponibile:

`pueue enqueue --help`
