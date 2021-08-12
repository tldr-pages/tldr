# git show-branch

> Arată sucursale și angajamente lor.
> Mai multe informaţii: <https://git-scm.com/docs/git-show-branch>

- Afișați un rezumat al ultimelor angajamente pe o sucursală:

`git show-branch {{branch_name|ref|commit}}`

- Comparați angajamente în istoria mai multor angajamente sau sucursale:

`git show-branch {{branch_name|ref|commit}}`

- Comparați toate ramurile de urmărire la distanță:

`git show-branch --remotes`

- Comparați sucursalele locale și de urmărire la distanță:

`git show-branch --all`

- Listați cele mai recente angajamente în toate sucursalele:

`git show-branch --all --list`

- Comparați o ramură dată cu ramura curentă:

`git show-branch --current {{commit|branch_name|ref}}`

- Afișează numele de comitere în locul numelui relativ:

`git show-branch --sha1-name --current {{current|branch_name|ref}}`

- Continuă să mergi un anumit număr de comite trecut de strămoşul comun:

`git show-branch --more {{5}} {{commit|branch_name|ref}} {{commit|branch_name|ref}} {{...}}`
