# git checkout

> Extrait une branche ou des chemins vers l'arborescence de travail.
> Plus d'informations : <https://git-scm.com/docs/git-checkout>.

- Crée une branche et bascule dessus :

`git checkout -b {{nom_branche}}`

- Crée une branche depuis une référence spécifique et bascule dessus (par exemple, branche locale/distante, tag, validation) :

`git checkout -b {{nom_branche}} {{référence}}`

- Bascule sur une branche locale existante :

`git checkout {{nom_branche}}`

- Bascule sur la branche précédente :

`git checkout -`

- Bascule sur une branche distante existante :

`git checkout {{[-t|--track]}} {{nom_distant}}/{{nom_branche}}`

- Annule tout les changements dans le répertoire actuel (voir `git reset` pour plus de commandes d'annulation) :

`git checkout .`

- Annule tout les changements dans le fichier spécifié :

`git checkout {{nom_fichier}}`

- Remplace un fichier par sa version d'une autre branche :

`git checkout {{nom_branche}} -- {{nom_fichier}}`
