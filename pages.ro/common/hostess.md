# hostess

> Un utilitar de linie de comandă idempotent pentru gestionarea fișierului `/etc/hosts`.
> Mai multe informaţii: <https://github.com/cbednarski/hostess>

- Lista domeniilor, ips țintă și starea on/off:

`hostess list`

- Adăugați un domeniu care indică mașina dvs. în fișierul dvs. hosts:

`hostess add {{local.example.com}} {{127.0.0.1}}`

- Eliminați un domeniu din fișierul dvs. gazdă:

`hostess del {{local.example.com}}`

- Dezactivați un domeniu (dar nu-l eliminați complet):

`hostess off {{local.example.com}}`
