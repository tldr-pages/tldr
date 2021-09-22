# git clone

> Kloon een bestaande repository.
> Meer informatie: <https://git-scm.com/docs/git-clone>.

- Kloon een bestaande repository:

`git clone {{remote_repository_locatie}}`

- Kloon een bestaande repository in een specifieke map:

`git clone {{remote_repository_locatie}} {{pad/naar/map}}`

- Kloon een bestaande repository en haar submodules:

`git clone --recursive {{remote_repository_locatie}}`

- Kloon een lokale repository:

`git clone -l {{pad/naar/lokale-repository}}`

- Kloon stilletjes:

`git clone -q {{remote_repository_locatie}}`

- Kloon een bestaande repository, maar haal enkel de recentste tien commits op van de standaard branch (handig op tijd te besparen):

`git clone --depth {{10}} {{remote_repository_locatie}}`

- Kloon een bestaande repository, haal enkel een specifiek branch op:

`git clone --branch {{naam}} --single-branch {{remote_repository_locatie}}`

- Kloon een bestaande repository, en maak gebruik van een specifieke SSH commando:

`git clone --config core.sshCommand="{{ssh -i pad/naar/ssh_prive_sleutel}}" {{remote_repository_locatie}}`
