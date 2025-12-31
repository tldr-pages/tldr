# bg

> Reprend l'exécution de tâches qui ont été suspendues (en utilisant `<Ctrl z>` par exemple) en arrière-plan.
> Plus d'informations : <https://www.gnu.org/software/bash/manual/bash.html#index-bg>.

- Reprend l'exécution de la dernière tâche suspendue en arrière-plan :

`bg`

- Reprend l'exécution d'une tâche précise (utiliser `jobs -l` pour obtenir son ID) en arrière-plan :

`bg %{{job_id}}`
