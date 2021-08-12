# git-maintenance

> Executați activități pentru a optimiza datele din depozitul Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-maintenance>

- Înregistrați depozitul curent în lista de depozite a utilizatorului pentru a avea zilnic lucrări de întreținere:

`git maintenance register`

- Începeți să rulați întreținerea în depozitul curent:

`git maintenance start`

- Opriți programul de întreținere de fundal pentru depozitul curent:

`git maintenance stop`

- Eliminați depozitul curent din lista de depozit de întreținere a utilizatorului:

`git maintenance unregister`

- Rulați o anumită sarcină de întreținere pe depozitul curent:

`git maintenance run --task={{commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch}}`
