# git rev-parse

> Affiche les métadonnées liées à des révisions spécifiques.
> Plus d'informations : <https://git-scm.com/docs/git-rev-parse>.

- Affiche l'empreinte du commit de la branche courante :

`git rev-parse {{nom_de_branche}}`

- Affiche le nom de la branche courante :

`git rev-parse --abbrev-ref {{HEAD}}`

- Obtient le chemin absolu du répertoire racine :

`git rev-parse --show-toplevel`
