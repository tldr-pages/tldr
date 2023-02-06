# bundletool dump

> Parancssori eszköz az Android alkalmazáscsomagok manipulálására. További információ: <https://developer.android.com/studio/command-line/bundletool>.

- Az alapmodul `AndroidManifest.xml` megjelenítése:

`bundletool dump manifest --bundle={{path/to/bundle.aab}}`

- Egy adott érték megjelenítése a `AndroidManifest.xml` oldalról XPath segítségével:

`bundletool dump manifest --bundle={{path/to/bundle.aab}} --xpath={{/manifest/@android:versionCode}}`

- A `AndroidManifest.xml` egy adott moduljának megjelenítése:

`bundletool dump manifest --bundle={{path/to/bundle.aab}} --module={{name}}`

- Az alkalmazáscsomag összes erőforrásának megjelenítése:

`bundletool dump resources --bundle={{path/to/bundle.aab}}`

- Egy adott erőforrás konfigurációjának megjelenítése:

`bundletool dump resources --bundle={{path/to/bundle.aab}} --resource={{type/name}}`

- Egy adott erőforrás konfigurációjának és értékeinek megjelenítése az azonosító használatával:

`bundletool dump resources --bundle={{path/to/bundle.aab}} --resource={{0x7f0e013a}} --values`

- A csomag konfigurációs fájl tartalmának megjelenítése:

`bundletool dump config --bundle={{path/to/bundle.aab}}`
