# hugo

> Sablon alapú statikus webhely-generátor. Modulokat, komponenseket és témákat használ. További információ: https: [//gohugo.io](https://gohugo.io).

- Új Hugo webhely létrehozása:

`hugo new site {{path/to/site}}`

- Új Hugo téma létrehozása (a témák letölthetők a https://themes.gohugo.io/ oldalról is):

`hugo new theme {{theme_name}}`

- Új oldal létrehozása:

`hugo new {{section_name}}/{{path/to/file}}`

- Oldal létrehozása a `./public/` könyvtárba:

`hugo`

- Építsen webhelyet a "draft"-ként megjelölt oldalakkal:

`hugo --buildDrafts`

- Oldal létrehozása egy adott könyvtárba:

`hugo --destination {{path/to/destination}}`

- Oldal létrehozása, webkiszolgáló indítása a kiszolgáláshoz, és automatikus újratöltés az oldalak szerkesztésekor:

`hugo server`
