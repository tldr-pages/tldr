# git clone

> Egy meglévő tárolóhely klónozása. További információ: <https://git-scm.com/docs/git-clone>.

- Egy meglévő tárolóhely klónozása:

`git clone {{remote_repository_location}}`

- Egy meglévő tárolóhely klónozása egy adott könyvtárba:

`git clone {{remote_repository_location}} {{path/to/directory}}`

- Egy meglévő tároló és annak almoduljainak klónozása:

`git clone --recursive {{remote_repository_location}}`

- Helyi tárolóhely klónozása:

`git clone -l {{path/to/local/repository}}`

- Csendben klónozás:

`git clone -q {{remote_repository_location}}`

- Egy meglévő tárolóhely klónozása: Csak az alapértelmezett ág 10 legfrissebb commitját kéri le (hasznos időmegtakarítás):

`git clone --depth {{10}} {{remote_repository_location}}`

- Meglévő tárolóhely klónozása csak egy adott ágat lekérve:

`git clone --branch {{name}} --single-branch {{remote_repository_location}}`

- Egy meglévő tároló klónozása egy adott SSH-paranccsal:

`git clone --config core.sshCommand="{{ssh -i path/to/private_ssh_key}}" {{remote_repository_location}}`
