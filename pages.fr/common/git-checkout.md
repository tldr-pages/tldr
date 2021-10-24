# git checkout

> Extraire une branche ou des chemins vers l'arborescence de travail.
> Plus d'informations : <https://git-scm.com/docs/git-checkout>.

- Créer une branche et basculer dessus :

`git checkout -b {{nom_de_branche}}`

- Créer une branche depuis une référence spécifique et basculer dessus (par exemple, branche locale/distante, tag, commit) :

`git checkout -b {{nom_de_branche}} {{référence}}`

- Basculer sur une branche locale existante :

`git checkout {{nom_de_branche}}`

- Basculer sur la branche précédente :

`git checkout -`

- Basculer sur une branche distante existante :

`git checkout --track {{nom_distant}}/{{nom_de_branche}}`

- Annule tout les changements dans le répertoire courant (voir `git reset` pour plus de commandes d'annulation) :

`git checkout .`

- Annule tout les changements dans le fichier spécifié :

`git checkout {{filename}}`

- Remplace un fichier par sa version d'une autre branche :

`git checkout {{nom_de_branche}} -- {{filename}}`
