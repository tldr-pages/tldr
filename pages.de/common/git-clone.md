# git clone

> Klone ein existierendes Repository.
> Mehr Informationen: <https://git-scm.com/docs/git-clone>.

- Klone ein existierendes Repository:

`git clone {{entfernter_repository_speicherort}}`

- Klone ein existierendes Repository und seine Submodule:

`git clone --recursive {{entfernter_repository_speicherort}}`

- Klone ein lokales Repository:

`git clone -l {{pfad/zum/lokalen/repository}}`

- Klone leise (ohne Meldungen):

`git clone -q {{entfernter_repository_speicherort}}`

- Klone ein existierendes Repository und rufe nur die neusten 10 Commits im standardmäßigen Branch ab (spart Zeit):

`git clone --depth {{10}} {{entfernter_repository_speicherort}}`
