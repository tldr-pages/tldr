# git rev-parse

> Afficher les métadonnées liées à des révisions spécifiques.
> Plus d'informations : <https://git-scm.com/docs/git-rev-parse>.

- Afficher le hash de commit de la branche courrante :

`git rev-parse {{nom_de_branche}}`

- Affiche le nom de la branche courrante :

`git rev-parse --abbrev-ref {{HEAD}}`

- Obtenir le chamin absolu du repertoire racine :

`git rev-parse --show-toplevel`
