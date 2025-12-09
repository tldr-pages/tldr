# git rev-list

> Liste les révisions (commits) dans l'ordre chronologique inverse.
> Plus d'informations : <https://git-scm.com/docs/git-rev-list>.

- Lister tout les commits dans la branche courante :

`git rev-list {{HEAD}}`

- Lister tout les commits plus récents qu'une date spécifique, sur une branche spécifique :

`git rev-list --since={{'2019-12-01 00:00:00'}} {{master}}`

- Lister tout les commits de merge depuis un commit spécifique :

`git rev-list --merges {{commit}}`
