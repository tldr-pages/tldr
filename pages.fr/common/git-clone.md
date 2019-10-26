# git clone

> Clone un repository existant.
> Plus d'informations : <https://git-scm.com/docs/git-clone>.

- Clone un repository existant :

`git clone {{remote_repository_location}}`

- Clone un repository existant et ses sous-modules : 

`git clone --recursive {{remote_repository_location}}`

- Pour cloner depuis une machine local :

`git clone -l`

- Clone silencieusement :

`git clone -q`

- Clone un repository existant, et reduit le repository au nombre de revision spécifié :

`git clone --depth {{10}} {{remote_repository_location}}`
