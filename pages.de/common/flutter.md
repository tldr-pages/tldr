# flutter

> Googles Cross-Platform Open-Source SDK.
> Weitere Informationen: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Initialisiere ein neues Flutter-Projekt in einem gleichnamigen Verzeichnis:

`flutter create {{Projektname}}`

- Überprüfe, ob alle externen Tools korrekt installiert sind:

`flutter doctor`

- Zeige oder wechsle Flutter Kanäle:

`flutter channel {{stable|beta|dev|master}}`

- Starte Flutter auf allen gestarteten Emulatoren und verbundenen Geräten:

`flutter run -d all`

- Starte Tests in einem Projekt vom Wurzelverzeichnes aus:

`flutter test {{test/beispiel_test.dart}}`

- Baue eine Release APK für die meisten modernen Smartphones:

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`

- Zeige Hilfe für einen bestimmten Befehl:

`flutter help {{befehl}}`
