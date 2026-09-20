# git cherry

> Recherche des commits qui n'ont pas encore été appliqués en amont.
> Plus d'informations : <https://git-scm.com/docs/git-cherry>.

- Affiche les commits (et leurs messages) avec des commits équivalents en amont :

`git cherry {{[-v|--verbose]}}`

- Spécifie une branche amont et une branche de rubrique différentes :

`git cherry {{origin}} {{topic}}`

- Limite les commits à ceux dans la limite donnée :

`git cherry {{origin}} {{topic}} {{base}}`
