# dart

> A Dart projektek kezelésének eszköze. További információ: <https://dart.dev/tools/dart-tool>.

- Új Dart projekt inicializálása egy azonos nevű könyvtárban:

`dart create {{project_name}}`

- Egy Dart fájl futtatása:

`dart run {{path/to/file.dart}}`

- Az aktuális projekt függőségeinek letöltése:

`dart pub get`

- Az aktuális projekt egységtesztjeinek futtatása:

`dart test`

- Egy elavult projekt függőségeinek frissítése a null-biztonság támogatása érdekében:

`dart pub upgrade --null-safety`

- Dart-fájl fordítása natív bináris állományba:

`dart compile exe {{path/to/file.dart}}`
