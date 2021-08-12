# findmnt

> Găsiți sistemul de fișiere.
> Mai multe informaţii: <https://manned.org/findmnt>

- Listează toate sistemele de fișiere montate:

`findmnt`

- Caută un dispozitiv:

`findmnt {{/dev/sdb1}}`

- Caută un punct de montare:

`findmnt {{/}}`

- Găsiți sisteme de fișiere în anumite tipuri:

`findmnt -t {{ext4}}`

- Găsiți sisteme de fișiere cu etichetă specifică:

`findmnt LABEL={{BigStorage}}`
