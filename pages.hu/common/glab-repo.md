# glab repo

> Munka a GitLab tárolókkal a parancssoron. További információ: <https://glab.readthedocs.io/en/latest/repo/index.html#synopsis>.

- Új adattár létrehozása (ha az adattár neve nincs megadva, az alapértelmezett név az aktuális könyvtár neve lesz):

`glab repo create {{name}}`

- Adattár klónozása:

`glab repo clone {{owner}}/{{repository}}`

- Elágazás és klónozás egy adattárból:

`glab repo fork {{owner}}/{{repository}} --clone`

- Adattár megtekintése az alapértelmezett webböngészőben:

`glab repo view {{owner}}/{{repository}} --web`

- Néhány tároló keresése a GitLab példányban:

`glab repo search -s {{search_string}}`
