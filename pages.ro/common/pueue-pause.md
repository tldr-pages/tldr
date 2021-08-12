# pueue pause

> Pauză rularea activităților sau grupurilor.
> A se vedea, de asemenea,: `pueue start`.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Întrerupeți toate activitățile din grupul implicit:

`pueue pause`

- Pauză o sarcină de rulare:

`pueue pause {{task_id}}`

- Întrerupeți o sarcină de funcționare și opriți toți copiii săi direcți:

`pueue pause --children {{task_id}}`

- Întrerupeți toate activitățile dintr-un grup și împiedicați-l să înceapă activități noi:

`pueue pause --group {{group_name}}`

- Întrerupeți toate activitățile și împiedicați toate grupurile să înceapă activități noi:

`pueue pause --all`
