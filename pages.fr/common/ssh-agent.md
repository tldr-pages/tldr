# ssh-agent

> Lance un agent SSH.
> Un agent SSH permet de stocker des clés SSH déchiffrées, jusqu'à ce qu'elle soient retirées ou que l'agent soit arrêté.
> Voir également `ssh-add`, qui permet d'ajouter et de gérer les clés enregistrées par l'agent SSH.
> Plus d'informations : <https://man.openbsd.org/ssh-agent>.

- Démarre un agent SSH pour le shell actuel :

`eval $(ssh-agent)`

- Arrête l'agent actuellement en fonctionnement :

`ssh-agent -k`
