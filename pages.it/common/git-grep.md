# git grep

> Cerca stringhe nello storico dei file tracciati nel repository.
> Supporta molti degli stessi parametri accettati dal comando `grep` tradizionale.
> Maggiori informazioni: <https://git-scm.com/docs/git-grep>.

- Cerca una stringa nei file tracciati:

`git grep {{stringa_ricercata}}`

- Cerca una stringa nei file tracciati che soddisfano un dato pattern:

`git grep {{stringa_ricercata}} -- {{file_glob_pattern}}`

- Cerca una stringa nei file tracciati, sottomoduli inclusi:

`git grep --recurse-submodules {{stringa_ricercata}}`

- Cerca una stringa in uno dato momento della cronologia del repository:

`git grep {{stringa_ricercata}} {{HEAD~2}}`

- Cerca una stringa in tutti i rami:

`git grep {{stringa_ricercata}} $(git rev-list --all)`
