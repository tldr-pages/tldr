# web-ext

> Parancssori eszköz a webes kiterjesztések fejlesztésének irányítására. További információ: <https://github.com/mozilla/web-ext>.

- Futtassa a webbővítményt a Firefox aktuális könyvtárában:

`web-ext run`

- Webbővítmény futtatása egy adott könyvtárból a Firefoxban:

`web-ext run --source-dir {{path/to/directory}}`

- Szöveges végrehajtási kimenet megjelenítése:

`web-ext run --verbose`

- Webbővítmény futtatása Firefox Androidban:

`web-ext run --target firefox-android`

- Lint a manifeszt és a forrásfájlok hibáira:

`web-ext lint`

- A bővítmény összeállítása és csomagolása:

`web-ext build`

- Szöveges építési kimenet megjelenítése:

`web-ext build --verbose`

- Csomag aláírása saját tárhelyen történő elhelyezéshez:

`web-ext sign --api-key {{api_key}} --api-secret {{api_secret}}`
