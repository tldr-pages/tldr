# git for-each-repo

> Executați o comandă Git într-o listă de depozite.
> Notă: această comandă este experimentală și se poate schimba.
> Mai multe informaţii: <https://git-scm.com/docs/git-for-each-repo>

- Rulați întreținerea pe fiecare dintr-o listă de depozite stocate în variabila de configurare a utilizatorului `maintenance .repo`:

`git for-each-repo --config={{maintenance.repo}} {{maintenance run}}`

- Rulați `git tragl` pe fiecare depozit listat într-o variabilă de configurare globală:

`git for-each-repo --config={{global_configuration_variable}} {{pull}}`
