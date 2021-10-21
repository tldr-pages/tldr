# git rev-parse

> Afficher les métadonnées liées à des révisions spécifiques.
> Plus d'informations : <https://git-scm.com/docs/git-rev-parse>.

- Afficher l'empreinte du commit de la branche courante :

`git rev-parse {{nom_de_branche}}`

- Affiche le nom de la branche courante :

`git rev-parse --abbrev-ref {{HEAD}}`

- Obtenir le chemin absolu du répertoire racine :

`git rev-parse --show-toplevel`
