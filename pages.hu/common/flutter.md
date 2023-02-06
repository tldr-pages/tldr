# flutter

> A Google ingyenes, nyílt forráskódú és platformokon átívelő mobilalkalmazás SDK-ja. További információ: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Inicializáljon egy új Flutter projektet egy azonos nevű könyvtárban:

`flutter create {{project_name}}`

- Ellenőrizze, hogy minden külső eszköz megfelelően telepítve van-e:

`flutter doctor`

- Flutter-csatorna listázása vagy módosítása:

`flutter channel {{stable|beta|dev|master}}`

- A Flutter futtatása az összes elindított emulátoron és csatlakoztatott eszközön:

`flutter run -d all`

- A `pubspec.yaml` oldalon megadott összes csomag letöltése:

`flutter pub get`

- A tesztek futtatása terminálban a projekt gyökeréből:

`flutter test {{test/example_test.dart}}`

- Készítsen egy kiadási APK-t, amely a legtöbb modern okostelefont célozza meg:

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`

- Súgó megjelenítése egy adott parancsról:

`flutter help {{command}}`
