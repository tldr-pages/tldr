# gh repo

> Munka a GitHub tárolókkal a parancssoron. További információ: <https://cli.github.com/manual/gh_repo>.

- Új adattár létrehozása (ha az adattár neve nincs megadva, az alapértelmezett név az aktuális könyvtár neve lesz):

`gh repo create {{name}}`

- Adattár klónozása:

`gh repo clone {{owner}}/{{repository}}`

- Elágazás és klónozás egy adattárból:

`gh repo fork {{owner}}/{{repository}} --clone`

- Adattár megtekintése az alapértelmezett webböngészőben:

`gh repo view {{repository}} --web`

- Egy adott felhasználó vagy szervezet tulajdonában lévő tárolók listázása (ha a tulajdonos nincs megadva, az alapértelmezett tulajdonos az aktuálisan bejelentkezett felhasználó lesz):

`gh repo list {{owner}}`

- Csak a nem villás tárolók listázása:

`gh repo list {{owner}} --non-forks`

- Adott elsődleges kódolási nyelvvel rendelkező adattárak listázása:

`gh repo list {{owner}} --language {{language_name}}`
