# pueue edit

> Editați comanda sau calea unei activități ascunse sau în coadă.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Editați o activitate, consultați `pueue status` pentru a obține ID-ul de activitate:

`pueue edit {{task_id}}`

- Editați calea din care este executată o sarcină:

`pueue edit {{task_id}} --path`

- Editați o comandă cu editorul specificat:

`EDITOR={{nano}} pueue edit {{task_id}}`
