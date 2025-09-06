# pathchk

> Controleer de geldigheid en draagbaarheid van padnamen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- Controleer padnamen op geldigheid in het huidige systeem:

`pathchk {{pad1 pad2 ...}}`

- Controleer padnamen op geldigheid in een breder scala van POSIX-conforme systemen:

`pathchk -p {{pad1 pad2 ...}}`

- Controleer padnamen op geldigheid in alle POSIX-conforme systemen:

`pathchk {{[-p -P|--portability]}} {{pad1 pad2 ...}}`

- Controleer alleen op lege padnamen of leidende streepjes (-):

`pathchk -P {{pad1 pad2 ...}}`
