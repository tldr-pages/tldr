# git clone

> Klone ein existierendes Repository.
> Weitere Informationen: <https://git-scm.com/docs/git-clone>.

- Klone ein existierendes Repository:

`git clone {{url_zu_repository}}`

- Klone ein existierendes Repository in ein bestimmtes Verzeichnis:

`git clone {{url_zu_repository}} {{pfad/zu/verzeichnis}}`

- Klone ein existierendes Repository und seine Submodule:

`git clone --recursive {{url_zu_repository}}`

- Klone ein lokales Repository:

`git clone -l {{pfad/zu/lokalem_repository}}`

- Klone ohne Meldungen:

`git clone -q {{url_zu_repository}}`

- Klone ein existierendes Repository und rufe nur die neuesten 10 Commits im Standard-Branch ab (spart Zeit):

`git clone --depth {{10}} {{url_zu_repository}}`

- Klone ein existierendes Repository, aber lade nur einen bestimmten Branch herunter:

`git clone --branch {{name}} --single-branch {{url_zu_repository}}`

- Klone ein existierendes Repository mit einem bestimmten SSH Befehl:

`git clone --config core.sshCommand="{{ssh -i pfad/zu/privat_ssh_schlüssel}}" {{url_zu_repository}}`
