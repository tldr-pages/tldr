# gh browse

> Nyisson meg egy GitHub-tárat a böngészőben, vagy nyomtassa ki az URL-t. További információ: <https://cli.github.com/manual/gh_browse>.

- Nyissa meg az aktuális adattár honlapját az alapértelmezett webböngészőben:

`gh browse`

- Egy adott adattár honlapjának megnyitása az alapértelmezett webböngészőben:

`gh browse {{owner}}/{{repository}}`

- Az aktuális adattár beállítási oldalának megnyitása az alapértelmezett webböngészőben:

`gh browse --settings`

- Az aktuális adattár wikioldalának megnyitása az alapértelmezett webböngészőben:

`gh browse --wiki`

- Egy adott issue vagy pull request megnyitása a webböngészőben:

`gh browse {{issue_or_pull_request_number}}`

- Egy adott ág megnyitása a webböngészőben:

`gh browse --branch {{branch_name}}`

- Az aktuális adattár egy adott fájljának vagy könyvtárának megnyitása a webböngészőben:

`gh browse {{path_from_root_of_repository}}`

- A cél-URL kinyomtatása a webböngésző megnyitása nélkül:

`gh browse --no-browser`
