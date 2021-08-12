# blkdiscard

> Elimină sectoarele dispozitivelor de pe dispozitivele de stocare. Utile pentru SSD-uri.
> Mai multe informaţii: <https://manned.org/blkdiscard>

- Aruncați toate sectoarele de pe un dispozitiv, eliminând toate datele:

`blkdiscard /dev/{{device}}`

- Aruncați în siguranță toate blocurile de pe un dispozitiv, eliminând toate datele:

`blkdiscard --secure /dev/{{device}}`

- Aruncați primul 100MB al unui dispozitiv:

`blkdiscard --length {{100MB}} /dev/{{device}}`
