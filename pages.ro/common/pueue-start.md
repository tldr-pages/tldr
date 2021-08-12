# pueue start

> Reluați funcționarea anumitor activități sau grupuri de activități.
> A se vedea, de asemenea,: `pueue pause`.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Reluați toate activitățile din grupul implicit:

`pueue start`

- Reluați o anumită sarcină:

`pueue start {{task_id}}`

- Reluați mai multe sarcini simultan:

`pueue start {{task_id}} {{task_id}}`

- Reluați toate sarcinile și începeți copiii lor:

`pueue start --all --children`

- Reluați toate sarcinile într-un anumit grup:

`pueue start group {{group_name}}`
