# git cherry

> Rechercher des commits qui n'ont pas encore été appliqués en amont.
> Plus d'informations : <https://git-scm.com/docs/git-cherry>.

- Afficher les commits (et leurs messages) avec des commits équivalents en amont :

`git cherry -v`

- Spécifiez une branche amont et une branche de rubrique différentes :

`git cherry {{origin}} {{topic}}`

- Limiter les commits à ceux dans la limite donnée :

`git cherry {{origin}} {{topic}} {{base}}`
