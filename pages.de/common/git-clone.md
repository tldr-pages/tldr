# git clone

> Klone ein existierendes Repository.
> Mehr Informationen: <https://git-scm.com/docs/git-clone>.

- Klone ein existierendes Repository:

`git clone {{url_zu_repository}}`

- Klone ein existierendes Repository und seine Submodule:

`git clone --recursive {{url_zu_repository}}`

- Klone ein lokales Repository:

`git clone -l {{pfad/zu/lokalem_repository}}`

- Klone ohne Meldungen:

`git clone -q {{url_zu_repository}}`

- Klone ein existierendes Repository und rufe nur die neusten 10 Commits im standardmäßigen Branch ab (spart Zeit):

`git clone --depth {{10}} {{url_zu_repository}}`
