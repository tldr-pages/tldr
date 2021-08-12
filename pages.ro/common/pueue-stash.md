# pueue stash

> Ascundere activități pentru a împiedica pornirea automată a acestora.
> A se vedea, de asemenea, `pueue start` și `pueue enqueue`.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Ascunzând o sarcină în cozi:

`pueue stash {{task_id}}`

- Ascunde mai multe sarcini simultan:

`pueue stash {{task_id}} {{task_id}}`

- Începeți imediat o sarcină ascunsă:

`pueue start {{task_id}}`

- Enqueue o activitate care urmează să fie executată atunci când se termină activitățile precedente:

`pueue enqueue {{task_id}}`
