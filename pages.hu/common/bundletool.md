# bundletool

> Parancssori eszköz az Android alkalmazáscsomagok manipulálására. Néhány alparancsnak, mint például a `bundletool validate`, saját használati dokumentációja van. További információ: <https://developer.android.com/studio/command-line/bundletool>.

- Egy alparancs súgójának megjelenítése:

`bundletool help {{subcommand}}`

- APK-k generálása egy alkalmazáscsomagból (kéri a keystore jelszavát):

`bundletool build-apks --bundle={{path/to/bundle.aab}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} --output={{path/to/file.apks}}`

- APK-k generálása egy alkalmazáscsomagból a keystore jelszó megadásával:

`bundletool build-apks --bundle={{path/to/bundle.aab}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} –ks-pass={{pass:the_password}} --output={{path/to/file.apks}}`

- Csak egyetlen APK-t tartalmazó APK-k generálása univerzális használatra:

`bundletool build-apks --bundle={{path/to/bundle.aab}} --mode={{universal}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} --output={{path/to/file.apks}}`

- Az APK-k megfelelő kombinációjának telepítése egy emulátorra vagy eszközre:

`bundletool install-apks --apks={{path/to/file.apks}}`

- Becsülje meg egy alkalmazás letöltési méretét:

`bundletool get-size total --apks={{path/to/file.apks}}`

- Eszközspecifikációs JSON fájl generálása egy emulátorhoz vagy eszközhöz:

`bundletool get-device-spec --output={{path/to/file.json}}`

- Egy csomag ellenőrzése és részletes információk megjelenítése róla:

`bundletool validate --bundle={{path/to/bundle.aab}}`
