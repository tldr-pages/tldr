# git clone

> Clone un dépôt existant.
> Plus d'informations : <https://git-scm.com/docs/git-clone>.

- Clone un dépôt existant dans un répertoire spécifique (le répertoire par défaut porte le nom du dépôt):

`git clone {{emplacement_dépôt_distant}} {{chemin/vers/répertoire}}`

- Clone un dépôt existant et ses sous-modules :

`git clone --recursive {{emplacement_dépôt_distant}}`

- Clone uniquement le repertoire `.git` d'un depot existant :

`git clone {{[-n|--no-checkout]}} {{emplacement_dépôt_distant}}`

- Clone un dépôt local :

`git clone {{[-l|--local]}} {{chemin/vers/dépôt_local}}`

- Clone silencieusement :

`git clone {{[-q|--quiet]}} {{emplacement_dépôt_distant}}`

- Clone un dépôt existant en ne récupérant que les 10 validations les plus récentes sur la branche par défaut (plus rapide) :

`git clone --depth 10 {{emplacement_dépôt_distant}}`

- Clone un dépôt existant en ne récupérant qu'une branche spécifique :

`git clone {{[-b|--branch]}} {{nom_branche}} --single-branch {{emplacement_dépôt_distant}}`

- Clone un dépôt existant en utilisant une commande SSH spécifique :

`git clone {{[-c|--config]}} core.sshCommand="{{ssh -i chemin/vers/clé_ssh_privée}}" {{emplacement_dépôt_distant}}`
