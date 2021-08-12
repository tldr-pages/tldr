# pueue kill

> Omoară activitățile care rulează sau grupurile întregi.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Omoară toate activitățile din grupul implicit:

`pueue kill`

- Omoară o anumită sarcină:

`pueue kill {{task_id}}`

- Ucide o sarcină și de a termina toate procesele sale copil:

`pueue kill --children {{task_id}}`

- Ucideți toate activitățile dintr-un grup și întrerupeți grupul:

`pueue kill --group {{group_name}}`

- Omoară toate sarcinile din toate grupurile și întrerupe toate grupurile:

`pueue kill --all`
