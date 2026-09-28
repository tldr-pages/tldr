# git cherry

> Recherche des validations qui n'ont pas encore été appliquées en amont.
> Plus d'informations : <https://git-scm.com/docs/git-cherry>.

- Affiche les validations (et leurs messages) avec des validations équivalentes en amont :

`git cherry {{[-v|--verbose]}}`

- Spécifie une branche amont et une branche de rubrique différentes :

`git cherry {{origin}} {{topic}}`

- Limite les commits à ceux dans la limite donnée :

`git cherry {{origin}} {{topic}} {{base}}`
