# fdroid

> F-Droid build tool. Az F-Droid egy telepíthető katalógus FOSS (Free and Open Source Software) alkalmazásokból az Android platformra. További információ [: https://f-droid.org/](https://f-droid.org/).

- Egy adott alkalmazás építése:

`fdroid build {{app_id}}`

- Egy adott alkalmazás építése egy build szerver VM-ben:

`fdroid build {{app_id}} --server`

- Az alkalmazás közzététele a helyi tárolóhelyen:

`fdroid publish {{app_id}}`

- Telepítse az alkalmazást minden csatlakoztatott eszközre:

`fdroid install {{app_id}}`

- Ellenőrizze, hogy a metaadatok helyesen vannak-e formázva:

`fdroid lint --format {{app_id}}`

- A formázás automatikus javítása (ha lehetséges):

`fdroid rewritemeta {{app_id}}`
