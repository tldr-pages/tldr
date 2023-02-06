# git show

> Különböző típusú Git objektumok (commitok, címkék stb.) megjelenítése. További információ: <https://git-scm.com/docs/git-show>.

- A legutóbbi commitra vonatkozó információk megjelenítése (hash, üzenet, változások és egyéb metaadatok):

`git show`

- Információk megjelenítése egy adott commitról:

`git show {{commit}}`

- Információk megjelenítése egy adott címkéhez tartozó commitról:

`git show {{tag}}`

- Információk megjelenítése egy ág HEAD-jétől számított 3. commitról:

`git show {{branch}}~{{3}}`

- A commit üzenetének megjelenítése egyetlen sorban, elnyomva a diff kimenetet:

`git show --oneline -s {{commit}}`

- Csak statisztikák megjelenítése (hozzáadott/eltávolított karakterek) a módosított fájlokról:

`git show --stat {{commit}}`

- Csak a hozzáadott, átnevezett vagy törölt fájlok listájának megjelenítése:

`git show --summary {{commit}}`

- A fájl tartalmának megjelenítése egy adott revízió (pl. ág, címke vagy commit) szerinti állapotában:

`git show {{revision}}:{{path/to/file}}`
