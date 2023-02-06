# aapt

> Android Asset Packaging Tool. Egy Android alkalmazás erőforrásainak összeállítása és csomagolása. További információ: <https://elinux.org/Android_aapt>.

- Az APK-archívumban található fájlok listázása:

`aapt list {{path/to/app.apk}}`

- Egy alkalmazás metaadatainak (verzió, engedélyek stb.) megjelenítése:

`aapt dump badging {{path/to/app.apk}}`

- Új APK-archívum létrehozása a megadott könyvtárból származó fájlokkal:

`aapt package -F {{path/to/app.apk}} {{path/to/directory}}`
