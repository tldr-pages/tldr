# zipalign

> Zip-archívum igazító eszköz. Az Android SDK építési eszközeinek része. További információ: <https://developer.android.com/studio/command-line/zipalign>.

- Egy ZIP-fájl adatainak 4 bájtos határok mentén történő igazítása:

`zipalign {{4}} {{path/to/input.zip}} {{path/to/output.zip}}`

- Ellenőrzi, hogy egy ZIP-fájl helyesen van-e igazítva a 4-bájtos határokhoz, és az eredményeket bőbeszédűen megjeleníti:

`zipalign -v -c {{4}} {{path/to/input.zip}}`
