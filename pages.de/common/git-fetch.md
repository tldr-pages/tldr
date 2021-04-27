# git fetch

> Lade Objekte und Referenzen (refs) von einem entfernten Repository.
> Weitere Informationen: <https://git-scm.com/docs/git-fetch>.

- Hole die neuesten Änderungen von dem standardmäßigen Repository im Upstream (wenn gesetzt):

`git fetch`

- Hole neue Branches von einem bestimmten Repository im Upstream:

`git fetch {{name_des_upstream_repository}}`

- Hole die neuesten Änderungen von allen Repositories im Upstream:

`git fetch --all`

- Lade auch die Tags des Repository im Upstream:

`git fetch --tags`

- Lösche lokale Referenzen auf entfernte Branches, die im Upstream-Repository nicht mehr existieren:

`git fetch --prune`
