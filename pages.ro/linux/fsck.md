# fsck

> Verificaţi integritatea unui sistem de fişiere sau reparaţi-l. În momentul executării comenzii, sistemul de fișiere trebuie demontat.
> Mai multe informaţii: <https://manned.org/fsck>

- Verificați sistemul de fișiere `/dev/sdx`, raportând orice blocuri deteriorate:

`fsck {{/dev/sdX}}`

- Verificați sistemul de fișiere `/dev/sdx`, raportând orice blocuri deteriorate și permițând interactiv utilizatorului să aleagă să le repare pe fiecare:

`fsck -r {{/dev/sdX}}`

- Verificați sistemul de fișiere `/dev/sdx`, raportând orice blocuri deteriorate și reparându-le automat:

`fsck -a {{/dev/sdX}}`
