# prctl

> Obtient ou définit les contrôles de ressources des processus, tâches et projets en cours d'exécution.
> Plus d'informations : <https://www.unix.com/man-page/sunos/1/prctl>.

- Examine les limites et les autorisations des processus :

`prctl {{id_processus}}`

- Examine les limites et les autorisations de processus dans un format analysable par machine :

`prctl -P {{id_processus}}`

- Obtient une limite spécifique pour un processus en cours d'exécution :

`prctl -n process.max-file-descriptor {{id_processus}}`
