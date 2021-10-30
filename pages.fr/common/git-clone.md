# git clone

> Clone un dépôt existant.
> Plus d'informations : <https://git-scm.com/docs/git-clone>.

- Clone un dépôt existant :

`git clone {{location_du_depot_distant}}`

- Clone un dépôt existant et ses sous-modules :

`git clone --recursive {{location_du_depot_distant}}`

- Clone un dépôt local :

`git clone -l`

- Clone silencieusement :

`git clone -q`

- Clone un dépôt existant en ne récupérant que les 10 commits les plus récents sur la branche par défaut (plus rapide) :

`git clone --depth {{10}} {{location_du_depot_distant}}`
