# git update-ref

> Comanda Git pentru crearea, actualizarea și ștergerea refs Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-update-ref>

- Ștergeți un ref, util pentru resetarea moale primul comite:

`git update-ref -d {{HEAD}}`

- Actualizare ref cu un mesaj:

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`
