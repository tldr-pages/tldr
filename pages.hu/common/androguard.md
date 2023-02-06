# androguard

> Visszafejtő eszköz Android alkalmazásokhoz. Python nyelven íródott. További információ: <https://github.com/androguard/androguard>.

- Android alkalmazás manifesztjének megjelenítése:

`androguard axml {{path/to/app.apk}}`

- Az alkalmazás metaadatainak (verzió és alkalmazásazonosító) megjelenítése:

`androguard apkid {{path/to/app.apk}}`

- Java kód dekompilálása egy alkalmazásból:

`androguard decompile {{path/to/app.apk}} --output {{path/to/directory}}`
