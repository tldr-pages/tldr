# git clone

> Cloner un dépôt existant.
> Plus d'informations : <https://git-scm.com/docs/git-clone>.

- Cloner un dépôt existant :

`git clone {{emplacement_du_depot_distant}}`

- Cloner un dépôt existant dans un répertoire spécifique:

`git clone {{emplacement_du_depot_distant}} {{chemin/vers/repertoire}}`

- Cloner un dépôt existant et ses sous-modules :

`git clone --recursive {{emplacement_du_depot_distant}}`

- Cloner un dépôt local :

`git clone -l {{chemin/vers/depot/local}}`

- Cloner silencieusement :

`git clone -q {{emplacement_du_depot_distant}}`

- Cloner un dépôt existant en ne récupérant que les 10 commits les plus récents sur la branche par défaut (plus rapide):

`git clone --depth {{10}} {{emplacement_du_depot_distant}}`

- Cloner un dépôt existant en ne récupérant qu'une branche spécifique :

`git clone --branch {{nom}} --single-branch {{emplacement_du_depot_distant}}`

- Cloner un dépôt existant en utilisant une commande SSH spécifique:

`git clone --config core.sshCommand="{{ssh -i chemin/vers/clef_ssh_privee}}" {{emplacement_du_depot_distant}}`
