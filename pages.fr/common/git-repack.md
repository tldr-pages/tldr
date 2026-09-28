# git repack

> Empaquete les objets décompressés dans un dépôt Git.
> Plus d'informations : <https://git-scm.com/docs/git-repack>.

- Empaquete les objets décompressés dans le répertoire actuel :

`git repack`

- Supprime également les objets redondants après empaquetage :

`git repack -d`

- Réempaquete tous les objets dans un seul paquet :

`git repack -a`

- Limite le réempaquetage aux objets locaux :

`git repack -l`
