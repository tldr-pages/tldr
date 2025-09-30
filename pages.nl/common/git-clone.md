# git clone

> Kloon een bestaande repository.
> Meer informatie: <https://git-scm.com/docs/git-clone>.

- Kloon een bestaande repository naar een nieuwe map (de standaardmap is de repository-naam):

`git clone {{externe_repository_locatie}} {{pad/naar/map}}`

- Kloon een bestaande repository en zijn submodules:

`git clone --recursive {{externe_repository_locatie}}`

- Kloon alleen de `.git`-map van een bestaande repository:

`git clone {{[-n|--no-checkout]}} {{externe_repository_locatie}}`

- Kloon een lokale repository:

`git clone {{[-l|--local]}} {{pad/naar/lokale_repository}}`

- Kloon in stille modus:

`git clone {{[-q|--quiet]}} {{externe_repository_locatie}}`

- Kloon een bestaande repository, waarbij alleen de nieuwste 10 commits op de standaard-branch worden opgehaald (handig om tijd te besparen):

`git clone --depth 10 {{externe_repository_locatie}}`

- Kloon een bestaande repository, waarbij alleen een specifieke branch wordt opgehaald:

`git clone {{[-b|--branch]}} {{naam}} --single-branch {{externe_repository_locatie}}`

- Kloon een bestaande repository met een specifiek SSH-commando:

`git clone {{[-c|--config]}} core.sshCommand="{{ssh -i pad/naar/privésleutel}}" {{externe_repository_locatie}}`
